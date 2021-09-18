from board import *
import os
import threading
from snake import *
from pynput.keyboard import Key, Listener
import time

snake = snake()
board = board(5)

def listener():
    """Collect events until released"""
    def on_press(key):
        snake.parseMove(key)

    with Listener(on_press=on_press) as listener:
        listener.join()

def game():
    board.render()
        
    while True:
        print('seouse')
        time.sleep(1)

listenerThread = threading.Thread(target=listener)
listenerThread.start()
gameThread = threading.Thread(target=game)
gameThread.start()