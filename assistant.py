import speech_recognition as sr
import pyttsx3
import subprocess
import os
import psutil
import pyautogui
import pyaudio
import wave
import keyboard
from datetime import datetime

hot_key = keyboard.is_pressed('#')
current_time_str = datetime.now().strftime('%H')
current_time = int(current_time_str)

greeting = "Tyler"
r = sr.Recognizer()
engine = pyttsx3.init(driverName='sapi5')

engine.setProperty('voice', r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
engine.setProperty('rate', 180)
engine.setProperty('volume', 0.9)


def tts(prompt):
    engine.say(prompt)
    engine.runAndWait()
    engine.stop()

def open_app(app_name):
        apps = {
            "google": "chrome.exe",
            "spotify": "spotify.exe",
            "visual studio code": "vscode.exe",
            "discord": "discord.exe",
            "notepad": "notepad.exe",
            "calculator": "calculator.exe",
            "steam": "steam.exe",
            "github desktop": "githubdesktop.exe",
            "file explorer": "fileexplorer.exe"

        }

        if app_name in apps:
            os.system(f"start {apps[app_name]}")
            print(f"Opening {app_name}")
        else:
            print(f"Application {app_name} not recognized")

def close_app(app_name):
        apps = {
            "google": "chrome.exe",
            "spotify": "spotify.exe",
            "visual studio code": "visualstudiocode.exe",
            "discord": "discord.exe",
            "notepad": "notepad.exe",
            "calculator": "calculator.exe",
            "steam": "steam.exe",
            "github desktop": "githubdesktop.exe",
            "file explorer": "fileexplorer.exe"

        }

        if app_name in apps:
            os.system(f"taskkill {apps[app_name]}")
            print(f"Opening {app_name}")
        else:
            print(f"Application {app_name} not recognized")

def greetTime():
    if current_time >= 4 and current_time <= 11:
        print("Good Morning, I hope you are doing well!")
        tts(f"Good Morning, I hope you are doing well{greeting}!")
    elif current_time >= 12 and current_time <= 16:
        print("Good Afternoon, I hope you are doing well!")
        tts(f"Good Afternoon, I hope you are doing well{greeting}!")
    else:
        print("Good Evening, I hope you are doing well!")
        tts(f"Good Evening, I hope you are doing well{greeting}!")

def listen():
    command = ""
    with sr.Microphone() as source:
        print("Listening...")

        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, timeout=None)
        
        try:
            command = r.recognize_google(audio).lower()
            print(command)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.") 
        except sr.RequestError:
            print("Sorry, I couldn't connect to the service.") 
            tts(f"Sorry, I couldn't connect to the service{greeting}.")
        return command.lower()
        

if __name__ == "__main__":
    greetTime()

    while True:
            command = listen()

            app_name = command.split("open ")[1]

            #command for this is Open app {app name}
            if command.split()[0] == "open":
                open_app(app_name)

            #command for this is Close app {app name}
            if command.split()[0] == "close":
                close_app(app_name)

            """
            #command for this is Exit genius bot
            if command == "exit genius bot":
                close_program()

            #command for this is Restart Computer
            if command == "restart computer":
                restart_computer()

            #command for this is Shutdown Computer
            if command.split() == "shutdown computer":
                shutdown_computer()

            #command for this is Lower Volume
            if command == "lower volume":
                lower_volume()

            #command for this is Raise Volume
            if command == "raise volume":
                raise_volume()

            #command for this is Ask Ai
            if command == "ask ai":
                ask_chatgpt()
            """
        

