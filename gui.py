import tkinter as tk
from tkinter import messagebox
import json
import os

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

class AppManagerGUI(tk.Tk):  # Inherit from tk.Frame instead of tk.Tk
    def __init__(self):
        super().__init__(self)  # Pass parent to tk.Frame
        self.apps = load_apps()
        
        self.app_listbox = tk.Listbox(self)
        self.app_listbox.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        self.update_app_listbox()

        self.name_label = tk.Label(self, text="App Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        self.path_label = tk.Label(self, text="App Path:")
        self.path_label.pack(pady=5)
        self.path_entry = tk.Entry(self)
        self.path_entry.pack(pady=5)

        self.add_button = tk.Button(self, text="Add App", command=self.add_app)
        self.add_button.pack(pady=10)

        self.delete_button = tk.Button(self, text="Delete App", command=self.delete_app)
        self.delete_button.pack(pady=10)

    def update_app_listbox(self):
        self.app_listbox.delete(0, tk.END)
        for app in self.apps:
            self.app_listbox.insert(tk.END, app)

    def add_app(self):
        name = self.name_entry.get()
        path = self.path_entry.get()
        if name and path:
            add_app(name, path)
            self.apps = load_apps()
            self.update_app_listbox()
            self.name_entry.delete(0, tk.END)
            self.path_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Input Error", "Please enter both name and path.")

    def delete_app(self):
        selected_app = self.app_listbox.curselection()
        if selected_app:
            app_name = self.app_listbox.get(selected_app[0])
            delete_app(app_name)
            self.apps = load_apps() 
            self.update_app_listbox()
        else:
            messagebox.showerror("Selection Error", "Please select an app to delete.")


if __name__ == "__main__":
    app = GeniusBot()
    app.mainloop()