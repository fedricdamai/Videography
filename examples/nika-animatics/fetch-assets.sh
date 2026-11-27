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
cut $B/b01.mp4 13109 2 5.0;  cut $B/b02.mp4 39535 3 1.5;  cut $B/b03.mp4 6753 3 1.5;   cut $B/b04.mp4 7674 2 1.5
cut $B/b05.mp4 5188 2 1.5;   cut $B/b06.mp4 17601 3 1.75; cut $B/b07.mp4 15875 1 1.75; cut $B/b08.mp4 27760 2 1.75
cut $B/b09.mp4 15167 3 1.75; cut $B/b10.mp4 24352 4 2.5;  cut $B/b11.mp4 11529 2 4.0
cut $B/b12.mp4 17464 2 6.5
curl -sfL -o flow-a/assets/music.mp3 https://assets.mixkit.co/music/267/267.mp3   # Trap Hamza, 112 BPM
curl -sfL -o flow-b/assets/music.mp3 https://assets.mixkit.co/music/33/33.mp3     # Motivating Mornings, 123 BPM
curl -sfL -o flow-c/assets/music.mp3 https://assets.mixkit.co/music/126/126.mp3   # Trap Electro Vibes, 112 BPM
mkdir -p flow-c2/assets
curl -sfL -o flow-c2/assets/music.mp3 https://assets.mixkit.co/music/126/126.mp3
for id in 2354 2364 1492 1485 2870; do curl -sfL -o flow-c2/assets/sfx-$id.mp3 https://assets.mixkit.co/active_storage/sfx/$id/$id-preview.mp3; done
for id in 1492 2870 2364; do curl -sfL -o flow-b/assets/sfx-$id.mp3 https://assets.mixkit.co/active_storage/sfx/$id/$id-preview.mp3; done
for f in a b c c2; do cp kit/kit.css kit/kit.js flow-$f/; done
rm -rf "$tmp"; echo "assets ready"
