import math
import os
import time
from threading import Thread

import keyboard
import pyautogui

upExaust = False
leftExaust = False
rightExaust = False
def goUP():
    global upExaust, leftExaust, rightExaust
    if upExaust == False:
        if not (pyautogui.pixelMatchesColor(1277, 1007, (164, 185, 80), tolerance=10) and pyautogui.pixelMatchesColor(1306, 986, (166, 186, 75), tolerance=10)):
            pyautogui.press('up')
            upExaust = True
            leftExaust = False
            rightExaust = False
        #time.sleep(.1)
def goLeft():
    global upExaust, leftExaust, rightExaust
    if leftExaust == False:
        if not (pyautogui.pixelMatchesColor(1022, 1209, (129, 161, 65), tolerance=10) and pyautogui.pixelMatchesColor(1048, 1237, (124, 161, 63), tolerance=10)):
            pyautogui.press('left')
            upExaust = False
            leftExaust = True
            rightExaust = False
        #time.sleep(.1)
def goRight():
    global upExaust, leftExaust, rightExaust
    if rightExaust == False:
        if not (pyautogui.pixelMatchesColor(1537, 1210, (145, 172, 77), tolerance=10) and pyautogui.pixelMatchesColor(1510, 1238, (140, 172, 71), tolerance=10)):
            pyautogui.press('right')
            upExaust = False
            leftExaust = False
            rightExaust = True
        #time.sleep(.1)

reset = False
count = 0
xp = 348814
turns = 1
def xpCounter():
    global reset, count, turns
    while turns>0 and stop == False:
        currentxp = xp + count*36
        turns = math.floor((547351 - currentxp) / 36)
        if pyautogui.pixelMatchesColor(1444, 93, (255, 255, 255), tolerance=10) and reset == False:# WHITE LVL UP
            count += 1
            reset = True
        if pyautogui.pixelMatchesColor(1422, 92, (55, 140, 239), tolerance=10) and reset == True:# BLUE MEANING NOTHING
            reset = False
        os.system('cls')
        print(count, "| XP: ", currentxp, " | Need to get to 547351 XP | Levels left: ", turns, "")
    print("DONE")

    #TEST1 TURNS:50 PROGRAM:255507 ACTUAL:266551

button = "p"
stop = False
def onkeypress(event):
    global stop
    if event.name == button:
        stop = True

print("Hasnt Started Yet")
time.sleep(5)
print("Started")

keyboard.on_press(onkeypress)

xpThread = Thread(target=xpCounter)
xpThread.start()

while True:
    if stop:
        print("Done")
        break
    
    upThread = Thread(target=goUP)
    leftThread = Thread(target=goLeft)
    rightThread = Thread(target=goRight)

    upThread.start()
    leftThread.start()
    rightThread.start()

    upThread.join()
    leftThread.join()
    rightThread.join()

xpThread.join()
