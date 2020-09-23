import pyautogui
# from tkinter import Tk
from time import sleep

# Setup
# root = Tk()
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True

# Each event that needs to be carried out
# (X-Position, Y-Position, Delay)
with open('clicks.txt') as f:
    clicks = [i.strip() for i in f.readlines()]
    moves = []
    for i in clicks:
        if i != '':
            move = i.split(', ')
            moves.append((int(move[1]), int(move[2]), float(move[3])))
sleep(1)
for move in moves:
    # print(move)
    x = move[0]
    y = move[1]
    t = move[2]
    pyautogui.moveTo(x, y)
    sleep(t)
    pyautogui.mouseDown()
    sleep(0.05)
    pyautogui.mouseUp()

