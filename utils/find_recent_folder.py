import re
from pathlib import Path
from typing import Optional

def find_most_recent_yyyymm_folder(recordings_dir: str) -> Optional[Path]:
    """
    Finds the most recent folder in recordings_dir matching YYYY-MM pattern.
    Returns the Path object or None if not found.
    """
    folder_pattern = re.compile(r"^\d{4}-\d{2}$")
    base = Path(recordings_dir).expanduser()
    folders = [f for f in base.iterdir() if f.is_dir() and folder_pattern.match(f.name)]
    if not folders:
        return None
    return sorted(folders)[-1]
