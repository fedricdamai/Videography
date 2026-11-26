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
cut $A/a01.mp4 35540 3 2.6;  cut $A/a02.mp4 34469 2 5.4;  cut $A/a03.mp4 20311 4 1.5;  cut $A/a04.mp4 46700 6 7.5
cut $A/a05.mp4 45735 1 4.0 960; cut $A/a06.mp4 9607 2 4.0 960; cut $A/a07.mp4 8657 5 2.5; cut $A/a08.mp4 8211 10 3.0
cut $A/a09.mp4 39800 1 4.5;  cut $A/a10.mp4 43241 2 3.33; cut $A/a11.mp4 51611 4 3.34; cut $A/a12.mp4 32043 2 3.33
cut $A/a13.mp4 46702 5 3.0;  cut $A/a14.mp4 46612 2 4.7
B=flow-b/assets
cut $B/b01.mp4 13109 2 5.0;  cut $B/b02.mp4 39535 3 1.5;  cut $B/b03.mp4 6753 3 1.5;   cut $B/b04.mp4 7674 2 1.5
cut $B/b05.mp4 5188 2 1.5;   cut $B/b06.mp4 17601 3 1.75; cut $B/b07.mp4 15875 1 1.75; cut $B/b08.mp4 27760 2 1.75
cut $B/b09.mp4 15167 3 1.75; cut $B/b10.mp4 24352 4 2.55; cut $B/b11.mp4 11529 2 2.3
curl -sfL -o flow-a/assets/music.mp3 https://assets.mixkit.co/music/267/267.mp3   # Trap Hamza, 112 BPM
curl -sfL -o flow-b/assets/music.mp3 https://assets.mixkit.co/music/33/33.mp3     # Motivating Mornings, 123 BPM
curl -sfL -o flow-c/assets/music.mp3 https://assets.mixkit.co/music/126/126.mp3   # Trap Electro Vibes, 112 BPM
for f in a b c; do cp kit/kit.css kit/kit.js flow-$f/; done
rm -rf "$tmp"; echo "assets ready"
