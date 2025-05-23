from pathlib import Path
from typing import List

def get_most_recent_flac_files(folder: Path, n: int = 10) -> List[Path]:
    """
    Returns the n most recently modified .flac files in the folder, sorted oldest to newest.
    """
    flac_files = list(folder.glob('*.flac'))
    if not flac_files:
        return []
    # Sort by mtime descending, take n, then reverse for oldest-to-newest
    flac_files = sorted(flac_files, key=lambda f: f.stat().st_mtime, reverse=True)[:n]
    return list(reversed(flac_files))
