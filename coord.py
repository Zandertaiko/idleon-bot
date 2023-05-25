import pyautogui, sys, time

# find coordinates of mouse
try:
    while True:
        time.sleep(2)
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr + "\n", end='')
except KeyboardInterrupt:
    print('\n')


