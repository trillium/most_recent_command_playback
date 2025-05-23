from find_recent_folder import find_most_recent_yyyymm_folder
from get_recent_flacs import get_most_recent_flac_files
from check_ffplay import check_ffplay_available
from play_flacs import play_flac_files
import sys

RECORDINGS_DIR = "~/.talon/recordings"
N = 10  # Number of files to play

def main():
    if not check_ffplay_available():
        print("ffplay is NOT available. Please install ffmpeg.")
        sys.exit(1)
    recent_folder = find_most_recent_yyyymm_folder(RECORDINGS_DIR)
    if not recent_folder:
        print("No YYYY-MM folders found.")
        sys.exit(1)
    flac_files = get_most_recent_flac_files(recent_folder, N)
    if not flac_files:
        print(f"No .flac files found in {recent_folder}")
        sys.exit(1)
    play_flac_files(flac_files)

if __name__ == "__main__":
    main()
