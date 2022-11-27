# resource path for pyninstaller
import sys
import os

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

from tkinter import PhotoImage,Canvas, Tk, NW
from PIL import Image,ImageTk
import json
from pynput import keyboard

from typing import TextIO

class Window(Tk):

    def __init__(self)->None:

        super(Window, self).__init__()

        # init window resolution
        self.win_width: int = 476
        self.win_height: int = 268

        # init all used images
        self.background_img: PhotoImage = ImageTk.PhotoImage(
            Image.open("4k/base.png").resize((self.win_width+5,self.win_height+5),Image.Resampling.LANCZOS))
        
        self.key1_pressed_img: PhotoImage = ImageTk.PhotoImage(
            Image.open("4k/base_0001.png").resize((self.win_width+5,self.win_height+5),Image.Resampling.LANCZOS))
        
        self.key2_pressed_img: PhotoImage = ImageTk.PhotoImage(
            Image.open("4k/base_0010.png").resize((self.win_width+5,self.win_height+5),Image.Resampling.LANCZOS))

        self.key3_pressed_img: PhotoImage = ImageTk.PhotoImage(
            Image.open("4k/base_0100.png").resize((self.win_width+5,self.win_height+5),Image.Resampling.LANCZOS))

        self.key4_pressed_img: PhotoImage = ImageTk.PhotoImage(
            Image.open("4k/base_1000.png").resize((self.win_width+5,self.win_height+5),Image.Resampling.LANCZOS))

        self.key12_pressed_img: PhotoImage = ImageTk.PhotoImage(
            Image.open("4k/base_0011.png").resize((self.win_width+5,self.win_height+5),Image.Resampling.LANCZOS))

        self.key34_pressed_img: PhotoImage = ImageTk.PhotoImage(
            Image.open("4k/base_1100.png").resize((self.win_width+5,self.win_height+5),Image.Resampling.LANCZOS))

        self.left_paw_img: PhotoImage = ImageTk.PhotoImage(
            Image.open("4k/base_right.png").resize((self.win_width+5,self.win_height+5),Image.Resampling.LANCZOS))

        self.right_paw_img: PhotoImage = ImageTk.PhotoImage(
            Image.open("4k/base_left.png").resize((self.win_width+5,self.win_height+5),Image.Resampling.LANCZOS))

        # init pressed dictionary
        """ used in change_paw func to update canvases"""
        self.paws: dict = {
            "key1_pressed":False,
            "key2_pressed":False,
            "key3_pressed":False,
            "key4_pressed":False,
        }

        self.config_file: TextIO = open("config.json", 'r')
        self.config: dict = json.load(self.config_file)
        self.key1: dict = {"key": self.config['key1']}
        self.key2: dict = {"key": self.config['key2']}
        self.key3: dict = {"key": self.config['key3']}
        self.key4: dict = {"key": self.config['key4']}
        self.valid_keys: list = [self.key1["key"],self.key2["key"],self.key3["key"],self.key4["key"]]

        self.one: str = self.valid_keys[0]
        self.two: str = self.valid_keys[1]
        self.three: str = self.valid_keys[2]
        self.four: str = self.valid_keys[3]

        # Keybind handlers
        self.bind("<Escape>", self.exit_app)
        self.protocol("WM_DELETE_WINDOW",self.on_close)
        self.listener = keyboard.Listener(on_press=self.key_press,on_release=self.key_release)
        self.listener.start()

        self.resizable(False,False)
        self.iconphoto(False, PhotoImage(file=resource_path("favicon.png")))
        self.title("4k Mania Cat")

        # base frame
        self.main_canvas: Canvas = Canvas(self,width=self.win_width,height=self.win_height)
        self.main_canvas.pack()
        self.main_canvas.focus_set()

        # canvas to handle the handles images
        self.canvas: Canvas = Canvas(self.main_canvas,bg="black", width=self.win_width, height=self.win_height)

        # background image
        self.background = self.canvas.create_image(0,0, anchor=NW,image=self.background_img)

        # cat's right paw
        self.keys_right = self.canvas.create_image(0,0, anchor=NW,image=self.right_paw_img)

        # cat's left paw
        self.keys_left = self.canvas.create_image(0,0, anchor=NW,image=self.left_paw_img)

        self.canvas.place(x=0,y=0)

    def key_press(self,key)->None:

        # set key to a string if possible
        key: str = self.get_char(key)
        
        # if key is valid then update paws dict
        if key in self.valid_keys:
            self.update_keys(key=key,pressed=True)
        else:
            return

    def key_release(self,key)->None:
        
        # set key to a string if possible
        key: str = self.get_char(key)

        # if key is valid then update paws dict
        if key in self.valid_keys:
            self.update_keys(key=key,pressed=False)
        else:
            return

    def update_keys(self,key: str,pressed: bool)->None:

        match(key):
            case self.one:
                self.paws["key1_pressed"] = pressed
            case self.two:
                self.paws["key2_pressed"] = pressed
            case self.three:
                self.paws["key3_pressed"] = pressed
            case self.four:
                self.paws["key4_pressed"] = pressed
        
        self.change_paw(self.paws)

    
    def change_paw(self,keys)->None:

        match(keys["key1_pressed"],keys["key2_pressed"]):
            case True, False:
                self.canvas.itemconfig(self.keys_left, image=self.key1_pressed_img)
            case False, True:
                self.canvas.itemconfig(self.keys_left, image=self.key2_pressed_img)
            case True, True:
                self.canvas.itemconfig(self.keys_left, image=self.key12_pressed_img)
            case False, False:
                self.canvas.itemconfig(self.keys_left, image=self.left_paw_img)
        
        match(keys["key3_pressed"],keys["key4_pressed"]):
            case True, False:
                self.canvas.itemconfig(self.keys_right, image=self.key3_pressed_img)
            case False, True:
                self.canvas.itemconfig(self.keys_right, image=self.key4_pressed_img)
            case True, True:
                self.canvas.itemconfig(self.keys_right, image=self.key34_pressed_img)
            case False, False:
                self.canvas.itemconfig(self.keys_right, image=self.right_paw_img)

    def exit_app(self,event):
        self.listener.stop()
        self.destroy()

    def on_close(self):
        self.listener.stop()
        self.destroy()

    def get_char(self,key):
        try:
            key: str = key.char
            return key
        except:
            return key

def main()->None:
    
    window = Window()
    window.mainloop()

    window.listener.join()

if __name__=="__main__":
    main()