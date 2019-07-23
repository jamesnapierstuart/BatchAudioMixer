"""
BatchAudioMixer
22/07/2019
Jstuart RStack SDoyle
"""

import os
import subprocess
from datetime import datetime
from tkinter import Tk, filedialog

version = 1.0
print("\n///////////////////////////////////////////////////////////////////////////////////////////")
print("BatchAudioMixer version ", version)
print("BatchAudioMixer takes audio files in a selected directory and mixes them together")
print("BatchAudioMixer supports .wav .aif .mp3")
print("\nA new 'BatchAudioMixerOutput' directory will be created in the selected directory")
print("A new 'BatchAudioMixer_DATETIME.wav' file will be placed here")
print("\nPlease select a directory containing 2 or more audio files...\n")

root = Tk()
root.withdraw()
in_dir = filedialog.askdirectory()

if not in_dir or not os.path.isdir(in_dir):
    print("Error: input directory doesn't exit. Exiting program")
    exit(2)

ext = ['.aif', '.wav', '.mp3']
wav_files = [os.path.join(in_dir, f"'{f}'")
             for f in os.listdir(in_dir) if os.path.splitext(f)[-1] in ext]

if len(wav_files) < 2:
    print("Error: Minimum of 2 audio files needed for this tool in the input directory. Exiting program")
    exit(2)

out_dir = os.path.join(in_dir, "BatchAudioMixerOutput")
if not os.path.isdir(out_dir):
    os.mkdir(out_dir)

out_file = "mergedOutput_" + str(datetime.now().isoformat()) + ".wav"
out_path = os.path.join(out_dir, out_file)

cmd = "sox -m -S --norm " + ' '.join(wav_files)
cmd += f' {out_path}'

print("Executing Sox merge...")
try:
    subprocess.run([cmd], shell=True)
except FileNotFoundError:
    print('Sox executable not found, ensure sox is installed on user machine')
    exit(2)

print("\nCreated new file:", out_path)
print("BatchAudioMixer complete.")
print("///////////////////////////////////////////////////////////////////////////////////////////")
