"""Transcribe videos with timestamps, to study a reference script or check our own VO.

    .venv/bin/pip install faster-whisper
    .venv/bin/python tools/transcribe.py video.mp4 [more.mp4 ...]

Writes video.txt next to each file: one line per phrase, "[start_seconds] text".
First run downloads the small.en speech model (about 250 MB).
"""
import subprocess, sys

import numpy as np
from faster_whisper import WhisperModel

model = WhisperModel("small.en", device="cpu", compute_type="int8")
for path in sys.argv[1:]:
    # Decode with ffmpeg ourselves; avoids PyAV version clashes.
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    segments, _ = model.transcribe(np.frombuffer(raw, dtype=np.float32), vad_filter=True)
    out = path.rsplit(".", 1)[0] + ".txt"
    with open(out, "w") as f:
        for s in segments:
            f.write(f"[{s.start:6.1f}] {s.text.strip()}\n")
    print("wrote", out)
