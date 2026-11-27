"""Replace a green phone screen in footage with a UI video, keeping fingers on top.

Usage:
  python tools/screen_replace.py track CLIP --start 0.7 --dur 4.4 [--crop x,y,w,h]
  python tools/screen_replace.py comp CLIP UI.mp4 OUT.mp4 --start 0.7 --dur 4.4 [--crop x,y,w,h] [--debug]

How it works, per frame:
  1. Green mask (HSV). Largest blob = the screen.
  2. Four sides fitted to the blob's hull (rounded corners ignored), corners = side intersections.
     Corners are smoothed over time (centered moving average) so the screen never jitters.
  3. The UI frame is warped onto the quad (slightly expanded so no green rim survives).
  4. Inside the quad, non-green blobs that touch the quad border are occluders (finger, thumb,
     bezel corners) and stay on top. Small blobs that don't touch the border (tracking markers)
     are painted over.
  5. Green spill is removed from kept pixels; the matte is feathered by 1 px.
`track` prints the occluder area per frame, which finds the tap frame (the peak).
"""
import argparse, json, subprocess, sys
import numpy as np, cv2

W, H, FPS = 1920, 1080, 30


def frames(path, start, dur, crop=None, size=(W, H)):
    vf = []
    if crop:
        x, y, w, h = crop
        vf.append(f"crop={w}:{h}:{x}:{y}")
    vf += [f"scale={size[0]}:{size[1]}:flags=lanczos", f"fps={FPS}"]
    cmd = ["ffmpeg", "-v", "error", "-ss", str(start), "-t", str(dur), "-i", path, "-vf", ",".join(vf),
           "-f", "rawvideo", "-pix_fmt", "bgr24", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    n = size[0] * size[1] * 3
    while True:
        b = p.stdout.read(n)
        if len(b) < n:
            break
        yield np.frombuffer(b, np.uint8).reshape(size[1], size[0], 3)
    p.wait()


def green_mask(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    m = cv2.inRange(hsv, (35, 70, 50), (88, 255, 255))
    b, g, r = [img[..., i].astype(np.int16) for i in range(3)]
    m &= ((g - np.maximum(r, b)) > 25).astype(np.uint8) * 255
    return m


def line_from(pts):
    vx, vy, x0, y0 = cv2.fitLine(pts.astype(np.float32), cv2.DIST_HUBER, 0, 0.01, 0.01).ravel()
    return np.array([x0, y0]), np.array([vx, vy])


def intersect(l1, l2):
    (p, r), (q, s) = l1, l2
    den = r[0] * s[1] - r[1] * s[0]
    if abs(den) < 1e-6:
        return None
    t = ((q[0] - p[0]) * s[1] - (q[1] - p[1]) * s[0]) / den
    return p + t * r


def order(c):
    c = np.array(c, np.float32)
    cen = c.mean(0)
    ang = np.arctan2(c[:, 1] - cen[1], c[:, 0] - cen[0])
    c = c[np.argsort(ang)]  # clockwise in image coords, starting from about -180 deg (left)
    # rotate so index 0 is top-left: smallest x+y
    i = int(np.argmin(c[:, 0] + c[:, 1]))
    return np.roll(c, -i, axis=0)  # TL, TR, BR, BL


def quad(mask):
    m = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if not cs:
        return None
    c = max(cs, key=cv2.contourArea)
    if cv2.contourArea(c) < 2000:
        return None
    hull = cv2.convexHull(c)
    peri = cv2.arcLength(hull, True)
    approx = None
    for e in np.linspace(0.01, 0.12, 40):
        a = cv2.approxPolyDP(hull, e * peri, True)
        if len(a) == 4:
            approx = a.reshape(4, 2)
            break
    if approx is None:
        x, y, w, h = cv2.boundingRect(c)
        return order([(x, y), (x + w, y), (x + w, y + h), (x, y + h)])
    corners = order(approx)
    # refine: fit each side to the dense contour points near the middle of that side
    pts = hull.reshape(-1, 2).astype(np.float32)
    dense = []
    for i in range(len(pts)):
        a, b = pts[i], pts[(i + 1) % len(pts)]
        k = max(2, int(np.linalg.norm(b - a) / 3))
        dense.append(np.linspace(a, b, k, endpoint=False))
    dense = np.concatenate(dense)
    lines = []
    for i in range(4):
        a, b = corners[i], corners[(i + 1) % 4]
        ab = b - a
        L = np.linalg.norm(ab)
        u = ab / L
        nrm = np.array([-u[1], u[0]])
        rel = dense - a
        t = rel @ u
        d = np.abs(rel @ nrm)
        sel = dense[(t > 0.2 * L) & (t < 0.8 * L) & (d < 0.04 * L + 4)]
        lines.append(line_from(sel) if len(sel) > 5 else (a, u))
    out = []
    for i in range(4):
        p = intersect(lines[i - 1], lines[i])
        out.append(p if p is not None else corners[i])
    out = np.array(out, np.float32)
    if np.abs(out - corners).max() > 60:  # refinement went wild; keep the coarse quad
        return corners
    return out


def sides(q):
    return np.array([np.linalg.norm(q[(i + 1) % 4] - q[i]) for i in range(4)])


def smooth(qs, win=5, tol=0.03):
    qs = np.array([q if q is not None else np.full((4, 2), np.nan) for q in qs], np.float32)
    # The phone is rigid: a frame whose side lengths drift from the clip's median was bent by a
    # finger crossing an edge. Drop it and interpolate from the clean frames around it.
    ok = [i for i in range(len(qs)) if not np.isnan(qs[i]).any()]
    if ok:
        med = np.median([sides(qs[i]) for i in ok], axis=0)
        for i in ok:
            if (np.abs(sides(qs[i]) / med - 1) > tol).any():
                qs[i] = np.nan
    good = [i for i in range(len(qs)) if not np.isnan(qs[i]).any()]
    if good and len(good) < len(qs):
        t = np.arange(len(qs))
        flat = qs.reshape(len(qs), 8)
        for j in range(8):
            flat[:, j] = np.interp(t, good, flat[good, j])
        qs = flat.reshape(len(qs), 4, 2)
    # fill gaps
    for i in range(len(qs)):
        if np.isnan(qs[i]).any():
            j = next((k for k in range(i, len(qs)) if not np.isnan(qs[k]).any()), None)
            k = next((k for k in range(i, -1, -1) if not np.isnan(qs[k]).any()), None)
            qs[i] = qs[j] if j is not None else qs[k]
    out = qs.copy()
    h = win // 2
    for i in range(len(qs)):
        out[i] = np.median(qs[max(0, i - h): i + h + 1], axis=0) * 0.5 + qs[max(0, i - h): i + h + 1].mean(0) * 0.5
    return out


def expand(q, px):
    c = q.mean(0)
    out = []
    for p in q:
        v = p - c
        out.append(p + v / np.linalg.norm(v) * px)
    return np.array(out, np.float32)


def matte(img, q):
    """Return alpha (0..1) of pixels to replace with UI."""
    g = green_mask(img)
    g = cv2.dilate(g, np.ones((3, 3), np.uint8))
    inside = np.zeros(g.shape, np.uint8)
    cv2.fillConvexPoly(inside, q.astype(np.int32), 255)
    band = inside - cv2.erode(inside, np.ones((9, 9), np.uint8))
    non = cv2.bitwise_and(inside, cv2.bitwise_not(g))
    n, lab, stats, _ = cv2.connectedComponentsWithStats(non, 8)
    keep = np.zeros(g.shape, np.uint8)
    touch = np.unique(lab[band > 0])
    for k in touch:
        if k == 0:
            continue
        if stats[k, cv2.CC_STAT_AREA] > 150:
            keep[lab == k] = 255
    rep = cv2.bitwise_and(inside, cv2.bitwise_not(keep))
    a = cv2.GaussianBlur(rep.astype(np.float32) / 255.0, (3, 3), 0.8)
    occ = int((keep > 0).sum())
    return a, keep, occ


def despill(img, region):
    f = img.astype(np.int16)
    b, g, r = f[..., 0], f[..., 1], f[..., 2]
    lim = np.maximum(r, b)
    sp = (g > lim) & (region > 0)
    f[..., 1] = np.where(sp, lim, g)
    return f.astype(np.uint8)


def parse_crop(s):
    return tuple(int(v) for v in s.split(",")) if s else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["track", "comp"])
    ap.add_argument("clip")
    ap.add_argument("ui", nargs="?")
    ap.add_argument("out", nargs="?")
    ap.add_argument("--start", type=float, default=0)
    ap.add_argument("--dur", type=float, required=True)
    ap.add_argument("--crop")
    ap.add_argument("--expand", type=float, default=4)
    ap.add_argument("--gain", type=float, default=0.94, help="screen brightness vs UI render")
    ap.add_argument("--debug", action="store_true")
    a = ap.parse_args()
    crop = parse_crop(a.crop)

    qs, occs = [], []
    for img in frames(a.clip, a.start, a.dur, crop):
        q = quad(green_mask(img))
        qs.append(q)
    sq = smooth(qs)
    if a.mode == "track":
        for i, img in enumerate(frames(a.clip, a.start, a.dur, crop)):
            _, _, occ = matte(img, expand(sq[i], a.expand))
            occs.append(occ)
        base = np.percentile(occs, 10)
        for i, o in enumerate(occs):
            print(f"{i/FPS:6.2f}s  occ {o - base:8.0f}  quad {sq[i].round().astype(int).tolist()}")
        print(json.dumps({"tap_s": round(int(np.argmax(occs)) / FPS, 2)}))
        return

    # read the UI video at its native size
    probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height",
                            "-of", "csv=p=0", a.ui], capture_output=True, text=True).stdout.strip().split(",")
    uw, uh = int(probe[0]), int(probe[1])
    ui_iter = frames(a.ui, 0, a.dur, None, size=(uw, uh))
    src = np.array([(0, 0), (uw, 0), (uw, uh), (0, uh)], np.float32)
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}",
                            "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "17", "-pix_fmt", "yuv420p",
                            "-movflags", "+faststart", a.out], stdin=subprocess.PIPE)
    last_ui = None
    for i, img in enumerate(frames(a.clip, a.start, a.dur, crop)):
        try:
            last_ui = next(ui_iter)
        except StopIteration:
            pass
        q = expand(sq[i], a.expand)
        M = cv2.getPerspectiveTransform(src, q)
        warped = cv2.warpPerspective(last_ui, M, (W, H), flags=cv2.INTER_LINEAR)
        warped = (warped.astype(np.float32) * a.gain)
        alpha, keep, _ = matte(img, q)
        region = cv2.dilate((alpha > 0).astype(np.uint8) * 255, np.ones((15, 15), np.uint8))
        clean = despill(img, region).astype(np.float32)
        out = warped * alpha[..., None] + clean * (1 - alpha[..., None])
        out = np.clip(out, 0, 255).astype(np.uint8)
        if a.debug:
            cv2.polylines(out, [q.astype(np.int32)], True, (0, 0, 255), 2)
        enc.stdin.write(out.tobytes())
    enc.stdin.close()
    enc.wait()
    print("wrote", a.out)


if __name__ == "__main__":
    main()
