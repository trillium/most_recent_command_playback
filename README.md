# most_recent_command_playback

This repository provides scripts and Talon command files for playing back recent .flac audio files, typically used for voice command playback and debugging in Talon Voice environments.

## Requirements

- [Talon Voice](https://talonvoice.com/) (macOS, Windows, or Linux)
- [ffplay](https://ffmpeg.org/ffplay.html) (part of ffmpeg, used for audio playback)

## Installation

1. Ensure you have Talon Voice installed and running on your system. You can download Talon Voice from the [official website](https://talonvoice.com/). Follow the installation instructions for your operating system (macOS, Windows, or Linux).
   - For additional Talon scripts and community support, visit the [TalonHub Community Repository](https://github.com/talonhub/community).
2. Install ffmpeg (which includes ffplay) if it is not already installed. On macOS, you can use Homebrew:
   ```sh
   brew install ffmpeg
   ```
3. Copy or symlink this repository (the `most_recent_command_playback` folder) into your Talon user directory, typically located at:
   - macOS: `~/.talon/user/`
   - Windows: `%USERPROFILE%\.talon\user\`
   - Linux: `~/.talon/user/`
4. Restart Talon or reload your Talon user scripts.

## Usage

After installation, you can use the following Talon voice commands:

- **"playback now"**: Plays back the 5 most recent .flac recordings captured by Talon.
- **"playback <number_small>"**: Plays back the specified number of recent .flac recordings (replace `<number_small>` with a number, e.g., "playback 3").

---

For more details, see the individual Python scripts and Talon command files in this repository.
