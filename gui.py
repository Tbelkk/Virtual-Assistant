import sys
sys.path.append(r"C:\Users\tyler\OneDrive\Desktop\Virtual-Assistant\Virtual-Assistant\.venv\Lib\site-packages")

import customtkinter as ctk
import settings
import main


class DashboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Dashboard")
        self.geometry("220x350")
        self.resizable(False, False) 

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)
        
        self.frames = {} 
        for Page in (DashboardPage, HotkeysPage, TextManagerPage):
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

        volume_label = ctk.CTkLabel(self, text="Volume:")
        volume_label.pack(pady=5)
        self.volume_slider = ctk.CTkSlider(self, from_=0, to=5)
        self.volume_slider.pack(pady=5, fill="x", padx=10)  

        hotkeys_button = ctk.CTkButton(self, text="Hotkeys", command=lambda: controller.show_frame(HotkeysPage))
        hotkeys_button.pack(pady=10, fill="x", padx=10)  

        text_manager_button = ctk.CTkButton(self, text="Manage Text", command=lambda: controller.show_frame(TextManagerPage))
        text_manager_button.pack(pady=10, fill="x", padx=10)  



class HotkeysPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ctk.CTkLabel(self, text="Hotkeys Menu", font=("Arial", 20))
        label.pack(pady=20)

        back_button = ctk.CTkButton(self, text="Back to Settings", command=lambda: controller.show_frame(DashboardPage))
        back_button.pack(pady=20)


class TextManagerPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.text_list = []

        label = ctk.CTkLabel(self, text="Text Manager", font=("Arial", 20))
        label.pack(pady=20)

        self.entry = ctk.CTkEntry(self, placeholder_text="Enter text")
        self.entry.pack(pady=5, fill="x", padx=10)

        add_button = ctk.CTkButton(self, text="Add", command=self.add_text)
        add_button.pack(pady=5, fill="x", padx=10)

        self.textbox = ctk.CTkTextbox(self, height=100)
        self.textbox.pack(pady=5, fill="both", padx=10, expand=True)

        delete_button = ctk.CTkButton(self, text="Delete", command=self.delete_text)
        delete_button.pack(pady=5, fill="x", padx=10)

        back_button = ctk.CTkButton(self, text="Back to Settings", command=lambda: controller.show_frame(DashboardPage))
        back_button.pack(pady=20)

    def add_text(self):
        text = self.entry.get()
        if text:
            self.text_list.append(text)
            self.entry.delete(0, 'end')
            self.update_textbox()

    def delete_text(self):
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
