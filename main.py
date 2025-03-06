import speech_recognition as sr
from datetime import datetime
import pyttsx3
import subprocess
import os
import psutil
import pyautogui
import keyboard
import webbrowser
import sys
import ollama
import threading
import gui
import json
import local_llm

greeting = "Tyler"
engine = pyttsx3.init(driverName='sapi5')

APPS_FILE = "apps.json"

def run_gui():
    subprocess.Popen(['python', 'gui.py'])

def load_apps():
    try:
        with open(APPS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

apps = load_apps()

def process_command(command):
    commands = {
        "open": lambda: open_app(command.split("open ")[1]) if  command.split()[0] == "open" else None,
        "close": lambda: close_app(command.split("close ")[1]) if command.split()[0] == "close" else None,
        "exit": lambda: close_program() if command == "exit program" else None,
        "restart": lambda: restart_computer() if command == "restart computer" else None,
        "shutdown": lambda: shutdown_computer() if command == "shutdown computer" else None,
        "lower": lambda: lower_volume() if command == "lower volume" else None,
        "raise": lambda: raise_volume() if command == "raise volume" else None,
        "free": lambda: local_llm.ai_response() if command == "free" else None,
    }
    for key, action in commands.items():
        if command.startswith(key):
            action()
            return True
    return False


def engine_volume(volume):
    engine.setProperty('volume', volume)
    

def tts(prompt):
    engine.setProperty('voice', r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    engine.setProperty('rate', 230)
    engine.say(prompt)
    engine.runAndWait()
    engine.stop()


def restart_computer():
    print("Restarting Computer...")
    tts("Restarting Computer...")
    os.system("shutdown /r /t 1")

def shutdown_computer():
    print("Shutting Down Computer...")
    tts("Shutting Down Computer...")
    os.system("shutdown /s /t 1")

def lower_volume():
    print("Lowering Volume")
    

def raise_volume():
    print("Raising Volume")

def close_program():
    os._exit(0)


def open_app(app_name):
    apps = gui.get_apps()  # Get the latest app list from app_manager
    if app_name in apps:
        subprocess.Popen(apps[app_name], shell=True)
        print(f"Opening {app_name}")
        tts(f"Opening {app_name}")
    else:
        print(f"Application {app_name} not recognized")
        tts(f"Application {app_name} not recognized")

def close_app(app_name):
    apps = gui.get_apps()  # Get the latest app list from app_manager
    if app_name in apps:
        subprocess.Popen(apps[app_name]).terminate()
        print(f"Closing {app_name}")
        tts(f"Closing {app_name}")
    else:
        print(f"Application {app_name} not recognized")
        tts(f"Application {app_name} not recognized")

def greetTime():
    current_time = int(datetime.now().strftime('%H'))
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

def listen_for_hotkeys():
    keyboard.wait()
        

keyboard.add_hotkey('esc', close_program)

hotkey_thread = threading.Thread(target=listen_for_hotkeys, daemon=True)
hotkey_thread.start()

if __name__ == "__main__":
    run_gui() 
    greetTime()

    while True:
            
            try:
                keyboard.wait("/")
                command = listen()
                if not process_command(command):
                    print("Not a valid command.")
                    tts("Not a valid command.")

            except Exception as e:
                print("Alert me when you're actually ready!")
                tts("Alert me when you're actually ready!")
                continue  
        

