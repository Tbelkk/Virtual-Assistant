import speech_recognition as sr
from tkinter import *
from datetime import datetime
import pyttsx3
import subprocess
import os
import psutil
import pyautogui
import pyaudio
import keyboard
import webbrowser
import sys
import ollama

current_time_str = datetime.now().strftime('%H')
current_time = int(current_time_str)

greeting = "Tyler"
engine = pyttsx3.init(driverName='sapi5')

engine.setProperty('voice', r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
engine.setProperty('rate', 230)
engine.setProperty('volume', 1)


def ai_response():

    prompt = listen()

    response = ollama.chat(model='llama3.2', messages=[
        {
            'role': 'system',
            'content': 'Respond with very short and seriously to questions but make sure to say what you have done, but feel free to add snide remarks when appropriate but dont preface the remark by saying it is a snide remark. When given a command, make sure to mention whether it was completed or not—no fluff unless youre in the mood for sarcasm, if the info is not accessible it will be given in prompt and if not say that you are not able to access it or it was not provided.',
        },
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    print(response['message']['content'])
    tts(response['message']['content'])


def process_command(command):
    commands = {
        "open": lambda: open_app(command.split("open ")[1]) if  command.split()[0] == "open" else None,
        "close": lambda: close_app(command.split("close ")[1]) if command.split()[0] == "close" else None,
        "exit": lambda: close_program() if command == "exit program" else None,
        "window": lambda: open_gui() if command == "window" else None,
        #"restart": lambda: restart_computer() if command == "restart computer" else None,
        #"shutdown": lambda: shutdown_computer() if command == "shutdown computer" else None,
        # "lower": lambda: lower_volume() if command == "lower volume" else None,
        # "raise": lambda: raise_volume() if command == "raise volume" else None,
        "ask": lambda: ai_response() if command == "ask ai" else None,
    }
    for key, action in commands.items():
        if command.startswith(key):
            action()
            return True
    return False


def tts(prompt):
    engine.say(prompt)
    engine.runAndWait()
    engine.stop()


def open_gui():
    root = Tk()
    root.title("Genius Bot")
    root.geometry('350x200')
    root.mainloop()

def close_program():
    sys.exit(0)

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
            tts(f"Opening {app_name}")
        else:
            print(f"Application {app_name} not recognized")
            tts(f"Application {app_name} not recognized")

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
            os.system(f"taskkill /im {apps[app_name]} /f")
            print(f"Closing {app_name}")
            tts(f"Closing {app_name}")
        else:
            print(f"Application {app_name} not recognized")
            tts(f"Application {app_name} not recognized")

def greetTime():
    if current_time >= 4 and current_time <= 11:
        print(f"Good Morning, I hope you are doing well {greeting}! ")
        tts(f"Good Morning, I hope you are doing well {greeting}!")
    elif current_time >= 12 and current_time <= 16:
        print(f"Good Afternoon, I hope you are doing well {greeting}!")
        tts(f"Good Afternoon, I hope you are doing well {greeting}!")
    else:
        print(f"Good Evening, I hope you are doing well {greeting}!")
        tts(f"Good Evening, I hope you are doing well {greeting}!")

def listen():
    r = sr.Recognizer()
    command = ""
    try:
        with sr.Microphone() as mic:
            print("Listening...")
            tts("Listening...")
            audio = r.listen(mic, timeout=None)
            command = r.recognize_google(audio).lower()
            print(command)
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.") 
        tts("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Sorry, I couldn't connect to the service.") 
        tts(f"Sorry, I couldn't connect to the service{greeting}.")

    return command.lower()
        

if __name__ == "__main__":
    greetTime()

    while True:
            
            try:
                if keyboard.is_pressed("/"):
                    command = listen()
                    if(process_command(command)):
                        process_command(command)
                    else:
                        print("Not a valid command.")
                        tts("Not a valid command.") 

            except Exception as e:
                print("Alert me when you're actually ready!")
                tts("Alert me when you're actually ready!")
                continue  
        

