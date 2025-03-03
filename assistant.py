import speech_recognition as sr
import pyttsx3
import subprocess
import os
import psutil
import pyautogui
import pyaudio
import wave
import keyboard
from pocketsphinx import LiveSpeech
from datetime import datetime

hot_key = keyboard.is_pressed("#")
key_phrase = "Bot"
current_time_str = datetime.now().strftime('%H')
current_time = int(current_time_str)

recognizer = sr.Recognizer()
engine = pyttsx3.init(driverName='sapi5')

engine.setProperty('voice', r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")

def greetTime():
    if current_time >= 4 and current_time <= 11:
        print("Good Morning!")
        engine.say("Good Morning!")
        engine.runAndWait()
        engine.stop()
    elif current_time >= 12 and current_time <= 16:
        print("Good Afternoon!")
        engine.say("Good Afternoon!")
        engine.runAndWait()
        engine.stop()
    else:
        print("Good Night!")
        engine.say("Good Night!")
        engine.runAndWait()
        engine.stop()

if __name__ == "__main__":
    greetTime()

        
