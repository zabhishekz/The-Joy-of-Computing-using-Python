# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 17:12:48 2021

@author: Abhishek
"""

import speech_recognition as sr

AUDIO_FILE=("recording.wav")

r=sr.Recognizer()#initialize the recogniser
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
#read the audio file
try:
    print("audio file contains "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError:
    print("couldn't get the results from google speech recognition")
    