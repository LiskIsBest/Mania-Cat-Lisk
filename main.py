from tkinter import *
import json

FILENAME: str = "config.json"

config_file = open(FILENAME, 'r')

config: dict = json.load(config_file)
key1: dict = {"key": config['key1']}
key2: dict = {"key": config['key2']}
key3: dict = {"key": config['key3']}
key4: dict = {"key": config['key4']}
valid_keys = [key1["key"],key2["key"],key3["key"],key4["key"]]
win_width = 1189
win_height = 669


def event_handle(event):
    char_pressed = event.keysym
    pressed_check = int(event.type) # "2" is press "3" is release

    if char_pressed not in valid_keys:
        return

    print(pressed_check, " ", char_pressed)

    left_set = [False, False]
    right_set = [False, False]

    # left
    match(pressed_check, char_pressed):
        case 2,'s':
            left_set[0] = True
        case 2, 'd':
            left_set[1] = True
        case _,_:
            try:
                left_set[0] = False
            except:
                pass 
            try:
                left_set[1] = False
            except:
                pass
            # canvas.itemconfig(key1_pressed, image=left_paw)
            # canvas.itemconfig(key2_pressed, image=left_paw)

    match(left_set[0],left_set[1]):
        case True,True:
            canvas.itemconfig(key12_pressed, image=key12_pressed_img)
            canvas.itemconfig(key1_pressed, image=blank)
            canvas.itemconfig(key2_pressed, image=blank)
        case True,False:
            canvas.itemconfig(key12_pressed, image=blank)
            canvas.itemconfig(key1_pressed, image=key1_pressed_img)
            canvas.itemconfig(key2_pressed, image=blank)
        case False,True:
            canvas.itemconfig(key12_pressed, image=blank)
            canvas.itemconfig(key1_pressed, image=blank)
            canvas.itemconfig(key2_pressed, image=key2_pressed_img)


    match(pressed_check, char_pressed):
        case 2,'l':
            canvas.itemconfig(key3_pressed, image=key3_pressed_img)
        case 2, 'semicolon':
            canvas.itemconfig(key4_pressed, image=key4_pressed_img)
        case _,_:
            canvas.itemconfig(key3_pressed, image=right_paw)
            canvas.itemconfig(key4_pressed, image=right_paw)

    # match(pressed_check,char_pressed):
        # case 2, ''

root = Tk()
root.resizable(False,False)
root.iconphoto(False, PhotoImage(file="favicon.png"))
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
left_paw = PhotoImage(file="4k/base_right.png")
right_paw = PhotoImage(file="4k/base_left.png")
blank = PhotoImage(file="4k/base_blank.png")

canvas = Canvas(frame,bg="black", width=win_width, height=win_height)

background = canvas.create_image(win_width/2,win_height/2,image=background_img)

key1_pressed = canvas.create_image(win_width/2,win_height/2,image=left_paw)
key2_pressed = canvas.create_image(win_width/2,win_height/2,image=left_paw)
key3_pressed = canvas.create_image(win_width/2,win_height/2,image=right_paw)
key4_pressed = canvas.create_image(win_width/2,win_height/2,image=right_paw)
key12_pressed = canvas.create_image(win_width/2,win_height/2,image=blank)
key23_pressed = canvas.create_image(win_width/2,win_height/2,image=blank)



canvas.place(x=0,y=0)

# frame2 = Frame(root,width=win_width,height=win_height)
# frame.bind("<KeyPress>",event_handle)
# frame.bind("<KeyRelease>",event_handle)
# frame.pack()

# key1_pressed_canvas = Canvas(frame, width=win_width, height=win_height)
# key1_pressed_canvas.place(x=0,y=0)

root.mainloop()
