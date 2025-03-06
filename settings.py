import json

APPS_FILE = "apps.json"

def load_apps():
    try:
        with open(APPS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_apps(apps):
    with open(APPS_FILE, "w") as file:
        json.dump(apps, file, indent=4)

def add_app(name, path):
    apps = load_apps()
    apps[name.lower()] = path
    save_apps(apps)

def delete_app(name):
    apps = load_apps()
    if name.lower() in apps:
        del apps[name.lower()]
        save_apps(apps)

def get_apps():
    return load_apps()