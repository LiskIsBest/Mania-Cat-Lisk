import tkinter as tk
from pynput.keyboard import Key, Listener
import sounddevice as sd
import numpy as np

# def on_press(key):
#     print('{0} pressed'.format(
#         key))

# def on_release(key):
#     print('{0} release'.format(
#         key))
#     if key == Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

# ################################

# def print_sound(indata, frames, time, status):
#     volume_norm = np.linalg.norm(indata)*10
#     # print ("|" * int(volume_norm))
#     print(int(volume_norm))

# with sd.Stream(callback=print_sound):
#     sd.sleep(10000)