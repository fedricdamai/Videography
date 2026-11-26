"""Measure the flow of one or more videos: cut rhythm, loudness, tempo,
whether cuts lock to the beat, and how energy moves across the film.

Use it on reference films and on our own drafts, then compare.

    python3 -m venv .venv && .venv/bin/pip install librosa matplotlib
    .venv/bin/python tools/flow_report.py draft.mp4 refs/*.mp4 --chart flow.png

Needs ffmpeg and ffprobe on PATH.
"""
import argparse, json, os, re, subprocess, sys, tempfile

import librosa
import numpy as np


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stderr


def hard_cuts(path, thresh=0.25, merge=0.2):
    log = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-an", "-vf",
               f"scale=480:-1,select=gt(scene\\,{thresh}),showinfo", "-f", "null", "-"])
    cuts = []
    for t in sorted(float(x) for x in re.findall(r"pts_time:([\d.]+)", log)):
        if not cuts or t - cuts[-1] > merge:  # drop glitch flashes
            cuts.append(t)
    return cuts


def loudness(path):
    log = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128", "-f", "null", "-"])
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", log)
    lra = re.findall(r"LRA:\s+([\d.]+) LU", log)
    return (float(i[-1]) if i else None), (float(lra[-1]) if lra else None)


def analyze(path):
    probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type:format=duration",
                            "-of", "json", path], capture_output=True, text=True).stdout
    meta = json.loads(probe)
    has_audio = any(s.get("codec_type") == "audio" for s in meta.get("streams", []))
    sr = 22050
    if has_audio:
        with tempfile.TemporaryDirectory() as tmp:
            wav = os.path.join(tmp, "a.wav")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-ac", "1", "-ar", str(sr), wav], check=True)
            y, sr = librosa.load(wav, sr=sr)
    else:  # silent render: keep the cut analysis, skip the audio analysis
        y = np.zeros(int(float(meta["format"]["duration"]) * sr), dtype=np.float32)
    dur = len(y) / sr
    cuts = hard_cuts(path)
    lufs, lra = loudness(path) if has_audio else (None, None)
    if has_audio:
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr, units="time")
        tempo = float(np.atleast_1d(tempo)[0])
    else:
        tempo, beats = 0.0, np.array([])

    pts = [0.0] + cuts + [dur]
    shots = sorted(b - a for a, b in zip(pts, pts[1:]) if b - a > 0.05)

    # Beat lock: where inside the beat does each cut land? Rayleigh test on the phase.
    lock = None
    inner = [c for c in cuts if len(beats) > 8 and beats[0] < c < beats[-1]]
    if len(inner) >= 4:
        ph = []
        for c in inner:
            i = np.searchsorted(beats, c) - 1
            ph.append((c - beats[i]) / (beats[i + 1] - beats[i]))
        z = np.mean(np.exp(2j * np.pi * np.array(ph)))
        R = abs(z)
        lock = dict(R=round(R, 2), p=round(float(np.exp(-len(ph) * R * R)), 3),
                    phase=round(float((np.angle(z) / (2 * np.pi)) % 1), 2))

    # Energy envelope in 0.5s steps, in dB below the loudest moment.
    hop = int(sr * 0.5)
    rms = librosa.feature.rms(y=y, frame_length=hop * 2, hop_length=hop)[0]
    db = librosa.amplitude_to_db(rms + 1e-9, ref=max(float(np.max(rms)), 1e-9))
    t = np.arange(len(db)) * 0.5
    med = float(np.median(db))
    quiet = [float(x) for x, v in zip(t, db) if v < med - 12 and 1 < x < dur - 4]
    thirds = [(dur * k / 3, dur * (k + 1) / 3) for k in range(3)]
    energy = [round(float(np.mean(db[(t >= a) & (t < b)])), 1) for a, b in thirds]
    cut_rate = [round(sum(a <= c < b for c in cuts) / (b - a), 2) for a, b in thirds]
    beat_len = 60 / tempo if tempo else None

    return dict(file=os.path.basename(path), duration=round(dur, 2), cuts=len(cuts),
                median_shot=round(shots[len(shots) // 2], 2), shortest=round(shots[0], 2), longest=round(shots[-1], 2),
                median_shot_beats=round(shots[len(shots) // 2] / beat_len, 1) if beat_len else None,
                lufs=lufs, lra=lra, tempo=round(tempo, 1), beat_lock=lock, quiet_moments=quiet,
                energy_by_third_db=energy, cuts_per_s_by_third=cut_rate,
                last_third_slows=cut_rate[2] < max(cut_rate[:2]),
                _env=(t.tolist(), db.tolist()), _cuts=cuts)


def verdict(r):
    out = []
    if r["lufs"] is None:
        out.append("no audio track: cut rhythm only")
    elif abs(r["lufs"] + 14) > 2:
        out.append(f"loudness {r['lufs']} LUFS (house target -14)")
    if not r["last_third_slows"]:
        out.append("last third does not slow down (every reference film does)")
    if r["median_shot"] > 1.6 and r["duration"] < 45:
        out.append(f"median shot {r['median_shot']}s is slow for a short spot (refs: 1.1 to 1.5s)")
    if r["lufs"] is not None and not r["quiet_moments"]:
        out.append("no near-silence anywhere (fine for loud spots like Cero; quiet spots use one before the key line)")
    return out or ["in range of the reference films"]


def chart(results, out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    blue, ink, ink2, grid, quiet = "#257de0", "#191919", "#666666", "#e7e7e7", "#efefef"
    fig, axes = plt.subplots(len(results), 1, figsize=(11, 1.35 * len(results)), dpi=200, squeeze=False)
    for ax, r in zip(axes[:, 0], results):
        t, db = r["_env"]
        for q in r["quiet_moments"]:
            ax.axvspan(q - 0.25, q + 0.25, color=quiet, lw=0, zorder=0)
        ax.plot(t, db, color=blue, lw=1.6, zorder=3)
        for c in r["_cuts"]:
            ax.plot([c, c], [-42, -37], color=ink2, lw=0.8)
        ax.set_xlim(0, r["duration"]); ax.set_ylim(-42, 3); ax.set_yticks([-30, -15, 0])
        ax.tick_params(colors=ink2, length=0, labelsize=7); ax.grid(axis="y", color=grid, lw=0.6)
        for s in ax.spines.values():
            s.set_visible(False)
        ax.set_title(f"{r['file']}  ·  {r['duration']:.0f}s  ·  {r['cuts']} cuts", loc="left",
                     color=ink, fontsize=9.5, fontweight="bold", pad=3)
    fig.text(0.01, 0.995, "Energy (dB below peak) and hard cuts (ticks). Grey: near-silence.",
             color=ink2, fontsize=8.5, va="top")
    fig.tight_layout(rect=(0, 0, 1, 0.985), h_pad=0.6)
    fig.savefig(out, facecolor="#ffffff")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("videos", nargs="+")
    ap.add_argument("--chart")
    ap.add_argument("--json")
    a = ap.parse_args()
    results = [analyze(v) for v in a.videos]
    for r in results:
        lock = r["beat_lock"]
        lock_s = "n/a" if not lock else (
            f"locked to beat (p={lock['p']}, lands at {lock['phase']} of the beat)" if lock["p"] < 0.05
            else f"not locked (p={lock['p']}), cuts follow action")
        print(f"\n== {r['file']}  {r['duration']}s")
        print(f"   cuts {r['cuts']} | median shot {r['median_shot']}s ({r['median_shot_beats']} beats) | {r['shortest']}-{r['longest']}s")
        print(f"   loudness {r['lufs']} LUFS, range {r['lra']} LU | tempo {r['tempo']} BPM | {lock_s}")
        print(f"   cuts/s by third {r['cuts_per_s_by_third']} | energy dB by third {r['energy_by_third_db']} | quiet at {r['quiet_moments'][:5]}")
        for v in verdict(r):
            print(f"   -> {v}")
    if a.chart:
        chart(results, a.chart)
    if a.json:
        json.dump([{k: v for k, v in r.items() if not k.startswith("_")} for r in results], open(a.json, "w"), indent=2)
