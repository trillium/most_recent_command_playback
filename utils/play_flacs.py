import os
import subprocess
import shutil
from pathlib import Path
from typing import List
import threading

def _play_flacs_thread(files: List[Path], ffplay_path: str, env):
    for f in files:
        proc = subprocess.Popen([ffplay_path, "-autoexit", "-nodisp", str(f)], env=env)
        proc.wait()

def play_flac_files(files: List[Path]):
    """
    Plays each .flac file in the list using ffplay with -autoexit and -nodisp, sequentially, in a background thread (non-blocking for Talon).
    """
    # Find ffplay path, trying common locations if not found in PATH
    ffplay_path = shutil.which("ffplay")
    if not ffplay_path:
        # Try /homebrew/bin/ffplay directly
        alt_paths = ["/homebrew/bin/ffplay", "/opt/homebrew/bin/ffplay", "/usr/local/bin/ffplay"]
        for alt in alt_paths:
            if os.path.isfile(alt) and os.access(alt, os.X_OK):
                ffplay_path = alt
                break
    if not ffplay_path:
        return
    env = os.environ.copy()
    # Prepend all common Homebrew and local bin paths if not already present
    extra_paths = ["/homebrew/bin", "/opt/homebrew/bin", "/usr/local/bin"]
    for p in extra_paths:
        if p not in env["PATH"]:
            env["PATH"] = f"{p}:" + env["PATH"]
    threading.Thread(target=_play_flacs_thread, args=(files, ffplay_path, env), daemon=True).start()