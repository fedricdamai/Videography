#!/bin/bash
# Re-download and trim the stock footage and music used by the Nika ripomatics.
# All clips and tracks are from Mixkit (mixkit.co), free under the Mixkit License.
# Usage: bash examples/nika-animatics/fetch-assets.sh   (needs curl and ffmpeg)
set -e
cd "$(dirname "$0")"
tmp=$(mktemp -d)
get() { [ -f "$tmp/$1.mp4" ] || curl -sfL -o "$tmp/$1.mp4" "https://assets.mixkit.co/videos/$1/$1-720.mp4"; }
cut() { # out id offset dur [width]
  get "$2"; w=${5:-1920}
  ffmpeg -v error -y -ss "$3" -t "$4" -i "$tmp/$2.mp4" -an \
    -vf "scale=$w:1080:force_original_aspect_ratio=increase,crop=$w:1080,fps=30" \
    -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p "$1"
}
mkdir -p flow-a/assets flow-b/assets flow-c/assets
A=flow-a/assets
cut $A/n01.mp4 34469 1 5.5;  cut $A/n02.mp4 41175 2 1.83; cut $A/n03.mp4 31413 2 1.83; cut $A/n04.mp4 29959 2 1.84
cut $A/n05.mp4 46700 3 8;    cut $A/n06.mp4 9607 2 1.5;   cut $A/n07.mp4 34469 9 3;    cut $A/n08.mp4 45735 3.5 2
cut $A/n09.mp4 46700 18 8
B=flow-b/assets
cut $B/z01.mp4 13109 2 1.9;  cut $B/z02.mp4 6753 3 1.7;  cut $B/z03.mp4 7674 2 1.5;  cut $B/z04.mp4 46653 3 1.4
cut $B/z05.mp4 52088 2 1.3;  cut $B/z06.mp4 14088 2 1.2; cut $B/z07.mp4 32005 4.5 7.0; cut $B/z08.mp4 34469 2 4.0
cut $B/z09.mp4 39788 2 4.4;  cut $B/z10.mp4 46378 2 1.35; cut $B/z11.mp4 43524 2 1.35; cut $B/z12.mp4 22051 3 1.35
cut $B/z13.mp4 4537 3 1.35
# Voice lines are generated locally: npx hyperframes tts (Kokoro). See flow-b/index.html for the script.
curl -sfL -o flow-a/assets/music.mp3 https://assets.mixkit.co/music/267/267.mp3   # Trap Hamza, 112 BPM
curl -sfL -o flow-b/assets/music.mp3 https://assets.mixkit.co/music/33/33.mp3     # Motivating Mornings, 123 BPM
curl -sfL -o flow-c/assets/music.mp3 https://assets.mixkit.co/music/126/126.mp3   # Trap Electro Vibes, 112 BPM
mkdir -p flow-c2/assets
curl -sfL -o flow-c2/assets/music.mp3 https://assets.mixkit.co/music/126/126.mp3
for id in 2354 2364 1492 1485 2870; do curl -sfL -o flow-c2/assets/sfx-$id.mp3 https://assets.mixkit.co/active_storage/sfx/$id/$id-preview.mp3; done
for id in 1492 2870 2364 1485; do curl -sfL -o flow-b/assets/sfx-$id.mp3 https://assets.mixkit.co/active_storage/sfx/$id/$id-preview.mp3; done
for f in a b c c2; do cp kit/kit.css kit/kit.js flow-$f/; done
# Flow B V2 (hybrid): reuses Flow B's assets, plus three real-phone shots made from green-screen stock.
# Needs: python3 with opencv-python-headless and numpy (pip install opencv-python-headless numpy).
V=flow-b-v2/assets; mkdir -p $V; cp flow-b/assets/*.mp3 flow-b/assets/z0[1-6].mp4 flow-b/assets/z08.mp4 flow-b/assets/z09.mp4 flow-b/assets/z1?.mp4 $V/
cp kit/kit.css kit/kit.js flow-b-v2/; cp kit/kit.css kit/kit.js flow-b-v2/screens/
get 36802; get 9078
curl -sfL -o "$tmp/100060.mp4" https://assets.mixkit.co/active_storage/video_items/100060/1719878673/100060-video-720.mp4
npx hyperframes render flow-b-v2/screens -o "$tmp/screens.mp4"
ffmpeg -v error -y -i "$tmp/screens.mp4" -filter_complex "[0]crop=760:1692:0:0,trim=0:2.6,setpts=PTS-STARTPTS[a];[0]crop=760:1370:760:0,trim=0:4.4,setpts=PTS-STARTPTS[b];[0]crop=760:1472:1520:0,trim=0:3.0,setpts=PTS-STARTPTS[c]" \
  -map "[a]" -crf 14 -pix_fmt yuv420p "$tmp/ui1.mp4" -map "[b]" -crf 14 -pix_fmt yuv420p "$tmp/ui2.mp4" -map "[c]" -crf 14 -pix_fmt yuv420p "$tmp/ui3.mp4"
SR=../../tools/screen_replace.py
python3 $SR comp "$tmp/36802.mp4" "$tmp/ui1.mp4" $V/r1.mp4 --start 2 --dur 2.6
python3 $SR comp "$tmp/9078.mp4" "$tmp/ui2.mp4" $V/r2.mp4 --start 0.7 --dur 4.4 --crop 167,80,1067,600
python3 $SR comp "$tmp/100060.mp4" "$tmp/ui3.mp4" $V/r3.mp4 --start 1.0 --dur 3.0 --crop 227,240,800,450
rm -rf "$tmp"; echo "assets ready"
