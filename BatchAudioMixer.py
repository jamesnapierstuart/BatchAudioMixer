# BatchAudioMixer
# 15/05/2019
# Jstuart RStack

version = 1.0
print("\n///////////////////////////////////////////////////////////////////////////////////////////")
print("BatchAudioMixer version ", version)
print("BatchAudioMixer takes audio files in a selected directory and mixes them together")
print("BatchAudioMixer supports .wav .aif .mp3")
print("\nA new 'BatchAudioMixerOutput' directory will be created in the selected directory")
print("A new 'BatchAudioMixer_DATETIME.wav' file will be placed here")
print("\nPlease select a directory containing 2 or more audio files...\n")

# Import package "pydub" if user doesn't have it
import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package]) 

import_or_install("sox")

# Sox also needs to be downloaded on the users machine
import sox
import os
import subprocess
import datetime
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()
inputDirectory = filedialog.askdirectory()

if not os.path.isdir(inputDirectory):
    print("Error: input directory doesn't exit. Exiting program")
    exit()

files = os.listdir(inputDirectory)
wavFiles = list()

for f in files:
    if f.endswith(".aif") or f.endswith(".wav") or f.endswith(".mp3"):
       wavFiles.append(os.path.join(inputDirectory, "'" + f + "'"))

if len(wavFiles) <= 1:
    print("Error: Minimum of 2 audio files needed for this tool in the input directory. Exiting program")
    exit()

outputDirectory = inputDirectory + "/BatchAudioMixerOutput"
if not os.path.isdir(outputDirectory):
    os.mkdir(outputDirectory)

command = "sox -m -S --norm"

for wavFile in wavFiles:
    command += " " + wavFile

outputFile = "mergedOutput_" + str(datetime.datetime.now().isoformat()) + ".wav"
outputPath = os.path.join(outputDirectory, outputFile)

commandSuffix = " " + outputPath
command += commandSuffix

print("Executing Sox merge...")
subprocess.run([command], shell=True)

print("\nCreated new file:", outputPath)
print("BatchAudioMixer complete.")
print("///////////////////////////////////////////////////////////////////////////////////////////")