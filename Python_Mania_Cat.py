from tkinter import PhotoImage,Canvas, Tk
import json

import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Window(Tk):

    def __init__(self)->None:

        self.config_file = open("config.json", 'r')
        
        super(Window, self).__init__()

        self.win_width = 1189
        self.win_height = 669

        self.background_img = PhotoImage(file="4k/base.png")
        self.key1_pressed_img = PhotoImage(file="4k/base_0001.png")
        self.key2_pressed_img = PhotoImage(file="4k/base_0010.png")
        self.key3_pressed_img = PhotoImage(file="4k/base_0100.png")
        self.key4_pressed_img = PhotoImage(file="4k/base_1000.png")
        self.key12_pressed_img = PhotoImage(file="4k/base_0011.png")
        self.key34_pressed_img = PhotoImage(file="4k/base_1100.png")
        self.left_paw_img = PhotoImage(file="4k/base_right.png")
        self.right_paw_img = PhotoImage(file="4k/base_left.png")

        self.paws = {
            "key1_pressed":False,
            "key2_pressed":False,
            "key3_pressed":False,
            "key4_pressed":False,
        }

        self.config: dict = json.load(self.config_file)
        self.key1: dict = {"key": self.config['key1']}
        self.key2: dict = {"key": self.config['key2']}
        self.key3: dict = {"key": self.config['key3']}
        self.key4: dict = {"key": self.config['key4']}
        self.valid_keys = [self.key1["key"],self.key2["key"],self.key3["key"],self.key4["key"]]

        self.one = self.valid_keys[0]
        self.two = self.valid_keys[1]
        self.three = self.valid_keys[2]
        self.four = self.valid_keys[3]

        self.bind("<KeyPress>",self.event_handle)
        self.bind("<KeyRelease>",self.event_handle)

        self.bind("<Escape>", self.exit_app)

        self.resizable(False,False)
        self.iconphoto(False, PhotoImage(file=resource_path("favicon.png")))
        self.title("4k Mania Cat")

        self.frame = Canvas(self,width=self.win_width,height=self.win_height)
        self.frame.pack()
        self.frame.focus_set()

        self.canvas = Canvas(self.frame,bg="black", width=self.win_width, height=self.win_height)

        self.background = self.canvas.create_image(self.win_width/2,self.win_height/2,image=self.background_img)

        self.keys_right = self.canvas.create_image(self.win_width/2,self.win_height/2,image=self.right_paw_img)
        self.keys_left = self.canvas.create_image(self.win_width/2,self.win_height/2,image=self.left_paw_img)

        self.canvas.place(x=0,y=0)

    def event_handle(self,event):
        key_pressed = event.keysym
        pressed_check = not(int(event.type)-2) # event.type returns "2" for press or "3" for release. converts to true false

        if key_pressed not in self.valid_keys:
            return

        if pressed_check:
            if key_pressed == self.one:
                self.paws["key1_pressed"] = True
            elif key_pressed == self.two:
                self.paws["key2_pressed"] = True
            elif key_pressed == self.three:
                self.paws["key3_pressed"] = True
            elif key_pressed == self.four:
                self.paws["key4_pressed"] = True
            self.change_paw(self.paws)

        if not pressed_check:
            if key_pressed == self.one:
                self.paws["key1_pressed"] = False
            elif key_pressed == self.two:
                self.paws["key2_pressed"] = False
            elif key_pressed == self.three:
                self.paws["key3_pressed"] = False
            elif key_pressed == self.four:
                self.paws["key4_pressed"] = False
            self.change_paw(self.paws)

        print(pressed_check, " ", key_pressed)

    def exit_app(self,event):
        self.destroy()
        
    def change_paw(self,keys):

        if(keys["key1_pressed"] == True) and (keys["key2_pressed"] == False):
            self.canvas.itemconfig(self.keys_left, image=self.key1_pressed_img)
        elif(keys["key1_pressed"] == False) and (keys["key2_pressed"] == True):
            self.canvas.itemconfig(self.keys_left, image=self.key2_pressed_img)
        elif(keys["key1_pressed"] == True) and (keys["key2_pressed"] == True):
            self.canvas.itemconfig(self.keys_left, image=self.key12_pressed_img)
        elif(keys["key1_pressed"] == False) and (keys["key2_pressed"] == False):
            self.canvas.itemconfig(self.keys_left, image=self.left_paw_img)

        if(keys["key3_pressed"] == True) and (keys["key4_pressed"] == False):
            self.canvas.itemconfig(self.keys_right, image=self.key3_pressed_img)
        elif(keys["key3_pressed"] == False) and (keys["key4_pressed"] == True):
            self.canvas.itemconfig(self.keys_right, image=self.key4_pressed_img)
        elif(keys["key3_pressed"] == True) and (keys["key4_pressed"] == True):
            self.canvas.itemconfig(self.keys_right, image=self.key34_pressed_img)
        elif(keys["key3_pressed"] == False) and (keys["key4_pressed"] == False):
            self.canvas.itemconfig(self.keys_right, image=self.right_paw_img)



def main():
    window = Window()
    window.mainloop()


if __name__=="__main__":
    main()