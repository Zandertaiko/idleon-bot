import pyautogui, sys, time

time.sleep(3)
x, y = pyautogui.locateCenterOnScreen('images/player_loc.png', confidence=0.9)
print(x, " ", y)