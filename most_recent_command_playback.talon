^playback now$:
    # Plays back the 5 most recent .flac recordings by default
    user.play_recent_recordings()

^playback <number_small>$:
    user.play_recent_recordings(number_small)
