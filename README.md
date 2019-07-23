## BatchAudioMixer
BatchAudioMixer mixes n number of audio files in a directory to a single audio file  
  
## Credits
Built by Jamie Stuart, Ross Stack & Sam Doyle
  
## Overview
BatchAudioMixer takes audio files in a selected directory and mixes them together  
BatchAudioMixer supports .wav .aif .mp3  
A new 'BatchAudioMixerOutput' directory will be created in the selected directory  
A new 'BatchAudioMixer_DATETIME.wav' file will be placed here  
  
The mixed audio file will be normalised  
  
## Installation
Requires Python 3 or later  
Requires Sox  
  
From the terminal / command prompt run the following command in the same directory as the python script:  
  
python3 BatchAudioMixer.py  
  
## Known Issues
Input files must have the same sample-rate  
tkinter crashes on Linux - Need to investigate  
We don't user the Sox wrapper module for Python  
Can't install pip modules without root user priviledges - should use pip freeze instead  
