from tkinter import *
import json

import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

FILENAME: str = "config.json"

config_file = open(FILENAME, 'r')

config: dict = json.load(config_file)
key1: dict = {"key": config['key1']}
key2: dict = {"key": config['key2']}
key3: dict = {"key": config['key3']}
key4: dict = {"key": config['key4']}
valid_keys = [one:=key1["key"],two:=key2["key"],three:=key3["key"],four:=key4["key"]]
win_width = 1189
win_height = 669


paws = {
    "key1_pressed":False,
    "key2_pressed":False,
    "key3_pressed":False,
    "key4_pressed":False,
}

def change_paw(keys):

        if(keys["key1_pressed"] == True) and (keys["key2_pressed"] == False):
            canvas.itemconfig(keys_left, image=key1_pressed_img)
        elif(keys["key1_pressed"] == False) and (keys["key2_pressed"] == True):
            canvas.itemconfig(keys_left, image=key2_pressed_img)
        elif(keys["key1_pressed"] == True) and (keys["key2_pressed"] == True):
            canvas.itemconfig(keys_left, image=key12_pressed_img)
        elif(keys["key1_pressed"] == False) and (keys["key2_pressed"] == False):
            canvas.itemconfig(keys_left, image=left_paw_img)

        if(keys["key3_pressed"] == True) and (keys["key4_pressed"] == False):
            canvas.itemconfig(keys_right, image=key3_pressed_img)
        elif(keys["key3_pressed"] == False) and (keys["key4_pressed"] == True):
            canvas.itemconfig(keys_right, image=key4_pressed_img)
        elif(keys["key3_pressed"] == True) and (keys["key4_pressed"] == True):
            canvas.itemconfig(keys_right, image=key34_pressed_img)
        elif(keys["key3_pressed"] == False) and (keys["key4_pressed"] == False):
            canvas.itemconfig(keys_right, image=right_paw_img)

def event_handle(event):
    key_pressed = event.keysym
    pressed_check = not(int(event.type)-2) # event.type returns "2" for press or "3" for release. converts to true false

    if key_pressed not in valid_keys:
        return

    if pressed_check:
        if key_pressed == one:
            paws["key1_pressed"] = True
        elif key_pressed == two:
            paws["key2_pressed"] = True
        elif key_pressed == three:
            paws["key3_pressed"] = True
        elif key_pressed == four:
            paws["key4_pressed"] = True
        change_paw(paws)

    if not pressed_check:
        if key_pressed == one:
            paws["key1_pressed"] = False
        elif key_pressed == two:
            paws["key2_pressed"] = False
        elif key_pressed == three:
            paws["key3_pressed"] = False
        elif key_pressed == four:
            paws["key4_pressed"] = False
        change_paw(paws)

    print(pressed_check, " ", key_pressed)


root = Tk()
root.resizable(False,False)
root.iconphoto(False, PhotoImage(file=resource_path("favicon.png")))
root.title("4k Mania Cat")

frame = Canvas(root,width=win_width,height=win_height)
frame.bind("<KeyPress>",event_handle)
frame.bind("<KeyRelease>",event_handle)
frame.pack()
frame.focus_set()

background_img = PhotoImage(file="4k/base.png")
key1_pressed_img = PhotoImage(file="4k/base_0001.png")
key2_pressed_img = PhotoImage(file="4k/base_0010.png")
key3_pressed_img = PhotoImage(file="4k/base_0100.png")
key4_pressed_img = PhotoImage(file="4k/base_1000.png")
key12_pressed_img = PhotoImage(file="4k/base_0011.png")
key34_pressed_img = PhotoImage(file="4k/base_1100.png")
left_paw_img = PhotoImage(file="4k/base_right.png")
right_paw_img = PhotoImage(file="4k/base_left.png")

canvas = Canvas(frame,bg="black", width=win_width, height=win_height)

background = canvas.create_image(win_width/2,win_height/2,image=background_img)

# key1_pressed = canvas.create_image(win_width/2,win_height/2,image=left_paw)
# key2_pressed = canvas.create_image(win_width/2,win_height/2,image=left_paw)
# key3_pressed = canvas.create_image(win_width/2,win_height/2,image=right_paw)
# key4_pressed = canvas.create_image(win_width/2,win_height/2,image=right_paw)
# key12_pressed = canvas.create_image(win_width/2,win_height/2,image=blank)
# key23_pressed = canvas.create_image(win_width/2,win_height/2,image=blank)

keys_right = canvas.create_image(win_width/2,win_height/2,image=right_paw_img)
keys_left = canvas.create_image(win_width/2,win_height/2,image=left_paw_img)

canvas.place(x=0,y=0)

# frame2 = Frame(root,width=win_width,height=win_height)
# frame.bind("<KeyPress>",event_handle)
# frame.bind("<KeyRelease>",event_handle)
# frame.pack()

# key1_pressed_canvas = Canvas(frame, width=win_width, height=win_height)
# key1_pressed_canvas.place(x=0,y=0)

root.mainloop()
