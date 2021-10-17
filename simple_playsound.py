#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 16:50:47 2021

@author: sazamore

Demonstrates how to play a sound
Requires the playsound library, and tech.wav

                                  ---

IF YOU GET AN ERROR ABOUT THE PLAYSOUND LIBRARY

In your command line, type in:
    pip install playsound
    pip install PyObjC
    
This will download and install the necessary libaries onto your computer, so that
Python can easily find it. Once installed, run this code again.

                                  ---

SOUNDFILE MUST BE IN THE SAME FOLDER AS SCRIPT.
"""
from playsound import playsound # import just the function playsound()
# Sound file must be in the same folder as this (and your) script!

# Make sure sound file is in the same folde as this script.
sound = 'tech.wav' # replace with the name of your sound file


playsound(sound) # plays the sound
    
# You must wait until the sound finishes for anything else to happen... 

# Best used with SHORT sounds (sound effects)