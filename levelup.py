import pyautogui, os, math
reset = False
count = 0
xp = 236599
turns = 1

while turns>0:
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