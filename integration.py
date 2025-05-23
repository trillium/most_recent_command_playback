# Talon integration for playing most recent .flac recordings
from talon import Module, actions, app
from pathlib import Path
import os

from utils.find_recent_folder import find_most_recent_yyyymm_folder
from utils.get_recent_flacs import get_most_recent_flac_files
from utils.check_ffplay import check_ffplay_available
from utils.play_flacs import play_flac_files

mod = Module()



@mod.action_class
class Actions:
    def play_recent_recordings(n: int = 5):
        """Play the N most recent .flac recordings from the most recent folder"""
        recordings_dir = Path.home() / ".talon" / "recordings"
        if not recordings_dir.exists():
            app.notify("No recordings directory found.")
            return
        folder = find_most_recent_yyyymm_folder(recordings_dir)
        if not folder:
            app.notify("No recent folder found.")
            return
        files = get_most_recent_flac_files(folder, n)
        if not files:
            app.notify("No .flac files found.")
            return
        # if not che# doin it
        play_flac_files(files)
        app.notify(f"Playing {len(files)} recent recordings.")
