import shutil

def check_ffplay_available() -> bool:
    """
    Returns True if ffplay is available in PATH, False otherwise.
    """
    ffplay_path = shutil.which("ffplay")
    print(f"[DEBUG] ffplay path: {ffplay_path}")
    return ffplay_path is not None
# doin it