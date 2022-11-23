import tkinter as tk

def event_handle(event):
    pressed_check = "pressed" if event.type == "2" else "released"
    print(new_text := f"Key: {event.keysym} was {pressed_check}")
    label1["text"] = new_text + " - Press Esc to quit."
    return

def exit_app(event):
    root.destroy()

root = tk.Tk()
root.bind("<KeyPress>",event_handle)
root.bind("<KeyRelease>",event_handle)
root.bind("<Escape>", exit_app)

label1 = tk.Label(root, text="Start typing - Press Esc to quit.",font=("Arial",25))
label1.pack()

root.mainloop()