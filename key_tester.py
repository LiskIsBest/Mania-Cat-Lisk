import tkinter as tk
import json
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

dump_json = open("dump.json", "w")

class Window:
    def __init__(self,root):
        self.to_dump = dict()
        self.icon = resource_path("favicon.ico")
        root.title("Key Tester")
        root.iconbitmap(self.icon)
        root.bind("<KeyPress>",self.event_handle)
        root.bind("<KeyRelease>",self.event_handle)
        root.bind("<Escape>", self.exit_app)

        self.label1 = tk.Label(root, text="Start typing - Press Esc to quit.",font=("Arial",25))
        self.label1.pack()

    def event_handle(self,event):
        pressed_key = event.keysym
        pressed_check = "pressed" if event.type == "2" else "released"
        new_text = f"Key: {pressed_key} was {pressed_check}"
        self.to_dump[f"{pressed_key}"] = pressed_key
        self.label1["text"] = new_text + " - Press Esc to quit."
        return

    def exit_app(self,event):
        json.dump(self.to_dump, dump_json, indent=2)
        dump_json.close()
        root.destroy()

root = tk.Tk()
Window = Window(root=root)
root.mainloop()

