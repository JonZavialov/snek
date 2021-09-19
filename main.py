from snake import *
from board import *
from game import *
import os
import threading
from pynput.keyboard import Key, Listener
import time

snake = snake()
board = board(24,10)
game = game(snake,board)

def listener():
    """Collect events until released"""
    def on_press(key):
        snake.parseMove(key)

    with Listener(on_press=on_press) as listener:
        listener.join()

def runner():
    game.genSnake()
    board.render()

listenerThread = threading.Thread(target=listener)
listenerThread.start()
runner()