from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import speech_recognition as sr
from datetime import datetime
import pyttsx3
import subprocess
import os
import keyboard
import threading
import llm


greeting = "User"
engine = pyttsx3.init(driverName='sapi5')

def process_command(command):
    commands = {
        "open": lambda: open_app(command.split("open ")[1]) if  command.split()[0] == "open" else None,
        "close": lambda: close_app(command.split("close ")[1]) if command.split()[0] == "close" else None,
        "exit": lambda: close_program() if command == "exit program" else None,
        "restart": lambda: restart_computer() if command == "restart computer" else None,
        "shutdown": lambda: shutdown_computer() if command == "shutdown computer" else None,
        "change": lambda: change_volume() if command == "change volume" else None,
        "free": lambda: llm.ai_response() if command == "free" else None,
    }
    for key, action in commands.items():
        if command.startswith(key):
            action()
            return True
    return False
    

def tts(prompt):
    engine.setProperty('voice', r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    engine.setProperty('rate', 230)
    engine.say(prompt)
    engine.runAndWait()
    engine.stop()


def changeVolume(value):
    return value

def restart_computer():
    print("Restarting Computer...")
    tts("Restarting Computer...")
    os.system("shutdown /r /t 1")

def shutdown_computer():
    print("Shutting Down Computer...")
    tts("Shutting Down Computer...")
    os.system("shutdown /s /t 1")

def change_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)

    print("What would you like to change the volume to?")
    tts("What would you like to change the volume to?")
    volumeLevel = listen()

    if volumeLevel.isdigit():
        volumeLevel = int(volumeLevel)
    else:
        volumeLevel = is_number_in_words(volumeLevel)
    if volumeLevel != -1:
        if 0 <= volumeLevel <= 100:
            volume.SetMasterVolumeLevelScalar(volumeLevel / 100, None)
            print(f"Volume set to {volumeLevel}")
            tts(f"Volume set to {volumeLevel}")
        else:
            print("Error, invalid volume level!")
            tts("Error, invalid volume level!")


def is_number_in_words(words):
    word_to_number = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty": 80, "ninety": 90, "hundred": 100
    }

    total = 0
    for word in words:
        if word in word_to_number:
            total += word_to_number[word]
        else:
            return -1
    
    return total
    

def raise_volume():
    print("Raising Volume")

def close_program():
    os._exit(0)


def open_app(app_name):
    apps = {
        "google": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "spotify": r"C:\Users\User\AppData\Roaming\Spotify\Spotify.exe",
        "visual studio code": r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "discord": r"C:\Users\User\AppData\Local\Discord\Update.exe --processStart Discord.exe",
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "steam": r"C:\Program Files (x86)\Steam\Steam.exe",
        "github": r"C:\Users\User\AppData\Local\GitHubDesktop\GitHubDesktop.exe",
        "file": "explorer.exe"
    }

    if app_name in apps:
        subprocess.Popen(apps[app_name], shell=True)
        print(f"Opening {app_name}")
        tts(f"Opening {app_name}")
    else:
        print(f"Application {app_name} not recognized")
        tts(f"Application {app_name} not recognized")

def close_app(app_name):
    apps = {
        "google": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "spotify": r"C:\Users\tyler\AppData\Roaming\Spotify\Spotify.exe",
        "visual studio code": r"C:\Users\tyler\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "discord": r"C:\Users\tyler\AppData\Local\Discord\Update.exe --processStart Discord.exe",
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "steam": r"C:\Program Files (x86)\Steam\Steam.exe",
        "github": r"C:\Users\tyler\AppData\Local\GitHubDesktop\GitHubDesktop.exe",
        "file": "explorer.exe"
    }

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
    greetTime()

    while True: 
        keyboard.wait("/")
        command = listen()
        if not process_command(command):
            print("Not a valid command.")
            tts("Not a valid command.") 
        

