import tkinter as tk
import json

dump_json = open("dump.json", "w")

to_dump = dict()

def event_handle(event):
    pressed_key = event.keysym
    pressed_check = "pressed" if event.type == "2" else "released"
    print(new_text := f"Key: {pressed_key} was {pressed_check}")
    to_dump[f"{pressed_key}"] = pressed_key
    label1["text"] = new_text + " - Press Esc to quit."
    return

def exit_app(event):
    json.dump(to_dump, dump_json, indent=2)
    root.destroy()

root = tk.Tk()
root.bind("<KeyPress>",event_handle)
root.bind("<KeyRelease>",event_handle)
root.bind("<Escape>", exit_app)

label1 = tk.Label(root, text="Start typing - Press Esc to quit.",font=("Arial",25))
label1.pack()

root.mainloop()