# most_recent_command_playback

This repository provides scripts and Talon command files for playing back recent .flac audio files, typically used for voice command playback and debugging in Talon Voice environments.

## Requirements

- [Talon Voice](https://talonvoice.com/) (macOS, Windows, or Linux)
- [ffplay](https://ffmpeg.org/ffplay.html) (part of ffmpeg, used for audio playback)

## Installation

Prerequisite: Requires the [community](https://github.com/talonhub/community) repository to be installed as a sibling in the same directory.

1. Open your Talon user scripts folder, typically located at:
   - macOS: `~/.talon/user/`
   - Windows: `%USERPROFILE%\.talon\user\`
   - Linux: `~/.talon/user/`
2. Clone this repository into your Talon user scripts folder:
   ```sh
   git clone https://github.com/trillium/most_recent_command_playback.git
   ```
3. Ensure the `community` folder is present in the same directory as this repo.
4. Install ffmpeg (which includes ffplay) if it is not already installed. On macOS, you can use Homebrew:
   ```sh
   brew install ffmpeg
   ```
5. Restart Talon or reload your Talon user scripts.

## Usage

After installation, you can use the following Talon voice commands:

- **"playback now"**: Plays back the 5 most recent .flac recordings captured by Talon.
- **"playback <number_small>"**: Plays back the specified number of recent .flac recordings (replace `<number_small>` with a number, e.g., "playback 3").

---

For more details, see the individual Python scripts and Talon command files in this repository.
