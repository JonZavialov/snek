from board import *
import os
from snake import *
from pynput.keyboard import Key, Listener

snake = snake()

def on_press(key):
    snake.move(key)

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()