import sys
sys.path.append(r"C:\Users\tyler\OneDrive\Desktop\Virtual-Assistant\Virtual-Assistant\.venv\Lib\site-packages")

import customtkinter as ctk
import settings
import main
import keyboard


class DashboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Genius")
        self.geometry("220x350")
        self.resizable(True, True) 

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1) 
        self.container.grid_columnconfigure(0, weight=1)
        
        self.frames = {} 
        for Page in (DashboardPage, HotkeysPage, AppManager):
            page = Page(parent=self.container, controller=self)
            self.frames[Page] = page
            page.grid(row=0, column=0, sticky="nsew") 

        self.show_frame(DashboardPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class DashboardPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ctk.CTkLabel(self, text="Dashboard", font=("Arial", 20))
        label.pack(pady=20)

        speak_button = ctk.CTkButton(self, width=90, height=75, text="Speak", font=("arial", 20), command=lambda: keyboard.press_and_release("/"))
        speak_button.pack(pady=30, fill="x", padx=30)

        hotkeys_button = ctk.CTkButton(self, text="Hotkeys", command=lambda: controller.show_frame(HotkeysPage))
        hotkeys_button.pack(pady=10, fill="x", padx=10)  

        app_manager_button = ctk.CTkButton(self, text="App Manager", command=lambda: controller.show_frame(AppManager))
        app_manager_button.pack(pady=10, fill="x", padx=10)  


def changeVolume(value):
    main.changeVolume(value)


class HotkeysPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ctk.CTkLabel(self, text="Hotkeys Menu", font=("Arial", 20))
        label.pack(pady=20)

        back_button = ctk.CTkButton(self, text="Back to Settings", command=lambda: controller.show_frame(DashboardPage))
        back_button.pack(pady=20)


class AppManager(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.text_list = []

        label = ctk.CTkLabel(self, text="App Manager", font=("Arial", 20))
        label.pack(pady=20)

        self.appName = ctk.CTkEntry(self, placeholder_text="Enter App Name(One word)")
        self.appName.pack(pady=5, fill="x", padx=10)

        self.appPATH = ctk.CTkEntry(self, placeholder_text="Enter App PATH")
        self.appPATH.pack(pady=5, fill="x", padx=10)

        add_button = ctk.CTkButton(self, text="Add")
        add_button.pack(pady=5, fill="x", padx=10)

        delete_button = ctk.CTkButton(self, text="Delete")
        delete_button.pack(pady=5, fill="x", padx=10)

        back_button = ctk.CTkButton(self, text="Back to Settings", command=lambda: controller.show_frame(DashboardPage))
        back_button.pack(pady=20)

    def add_app(self):
        appNameText = self.appName.get()
        appPathText = self.appPATH.get()
        if appNameText and appPathText:
            self.update_textbox()

    def delete_app(self):
        if self.text_list:
            self.text_list.pop()
            self.update_textbox()

    def update_textbox(self):
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", "\n".join(self.text_list))



if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = DashboardApp()
    app.mainloop()
