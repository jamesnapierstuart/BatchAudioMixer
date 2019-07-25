"""
BatchAudioMixer
22/07/2019
Jstuart RStack SDoyle
"""

# Useful pathlib tutorial:
# https://tinyurl.com/ybetcgb6
# https://realpython.com/python-pathlib/

# Known bugs:
# Spaces in directory names cause the subprocess sox call to fail

import os
import subprocess
from datetime import datetime
from tkinter import Tk, filedialog
from pathlib import Path # Prefer Pathlib over os.path.join

version = 1.1
print("\n///////////////////////////////////////////////////////////////////////////////////////////")
print("BatchAudioMixer version ", version)
print("BatchAudioMixer takes audio files in a selected directory and mixes them together")
print("BatchAudioMixer supports .wav .aif .mp3")
print("\nA new 'BatchAudioMixerOutput' directory will be created in the selected directory")
print("A new 'BatchAudioMixer_DATETIME.wav' file will be placed here")
print("\nPlease select a directory containing 2 or more audio files...\n")

root = Tk()
root.withdraw()
dialog_in_dir = filedialog.askdirectory()
in_dir = Path(dialog_in_dir)

if not dialog_in_dir or not in_dir.exists():
    print("Error: input directory doesn't exit. Exiting program")
    exit(2)

ext = ['.aif', '.wav', '.mp3']
wav_files = [f'"{str(Path(f))}" '
             for f in in_dir.iterdir() if f.suffix in ext]

if len(wav_files) < 2:
    print("Error: Minimum of 2 audio files needed for this tool in the input directory. Exiting program")
    exit(2)

out_dir = in_dir / "BatchAudioMixerOutput"
if not out_dir.exists():
    Path.mkdir(out_dir)

out_file = "mergedOutput_" + str(datetime.now().isoformat()) + ".wav"
out_file = out_dir / out_file

cmd = "sox -m -S --norm " + ' '.join(wav_files)
cmd += f' {str(Path(out_file))}'

print(cmd)

print("Executing Sox merge...")
try:
    subprocess.run(cmd, shell=True)
except FileNotFoundError:
    print('Sox executable not found, ensure sox is installed on user machine')
    exit(2)
