import pyautogui, sys, time
import win32gui
from datetime import datetime
from pyscreeze import ImageNotFoundException


# Functions
def anvil_deposit():
    time.sleep(0.1)
    pyautogui.press("c") # codex
    time.sleep(0.1)
    pyautogui.click(1180, 200) # quick ref
    time.sleep(0.1)
    pyautogui.click(922, 356) # anvil
    time.sleep(0.1)
    pyautogui.click(1000, 200) # produce
    time.sleep(0.1)
    pyautogui.click(866, 214) # deposit
    pyautogui.press("esc")

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def activate_game():
    if __name__ == "__main__":
        results = []
        top_windows = []
        win32gui.EnumWindows(windowEnumerationHandler, top_windows)
        for i in top_windows:
            if "legends" in i[1].lower(): # find legends of idleon
                print (i)
                win32gui.ShowWindow(i[0],5)
                win32gui.SetForegroundWindow(i[0])
                time.sleep(0.3)
                break

def claim_afk():
    time.sleep(0.1)
    startloop_time = datetime.now()
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen('images/claim.png', confidence=0.8) # locate claim afk gains button
            pyautogui.click(x,y)
            break
        except TypeError:
            time_delta = datetime.now() - startloop_time
            if time_delta.total_seconds() >= 5:
                print("Could not find the required screen. Document creating for this order aborted")
                break
            pass

def claim_traps():
    time.sleep(0.1)
    pyautogui.press("q")
    time.sleep(0.2)
    pyautogui.click(1589, 968)
    time.sleep(0.15)
    pyautogui.click(1320, 179)
    time.sleep(0.1)
    pyautogui.press("esc")
    time.sleep(0.1)


def select_player(player):
    time.sleep(0.1)
    pyautogui.click(1666, 987) # click "players" in bottom right
    time.sleep(0.1)

    if player < 7:
        pyautogui.click(598, 776) # click left arrow in player selection
    else:
        pyautogui.click(1419, 776) # click right arrow in player selection

    time.sleep(0.1)
    if player == 1 or player == 7:
        pyautogui.click(645, 272) # click player 1 or 7 loc (same coords, different page)
        time.sleep(0.1)
    elif player == 2 or player == 8:
        pyautogui.click(973, 296) # click player 2 or 8 loc (same coords, different page)
        time.sleep(0.1)
    elif player == 3:
        pyautogui.click(1384, 283) # click player 3 loc
        time.sleep(0.1)
    elif player == 4:
        pyautogui.click(658, 582) # click player 4 loc
        time.sleep(0.1)
    elif player == 5:
        pyautogui.click(1000, 617) # click player 5 loc
        time.sleep(0.1)
    elif player == 6:
        pyautogui.click(1351, 617) # click player 6 loc
        time.sleep(0.1)

    time.sleep(0.1)
    pyautogui.click(1000, 780) # click select player
    time.sleep(0.1)

def loot():
    x, y = pyautogui.locateCenterOnScreen('images/player_loc.png', confidence=0.9) # find guild tag
    pyautogui.moveTo(x-350, y-70) # move mouse to loot position
    time.sleep(1) # sleep 1 sec to wait for loot
    pyautogui.drag(900, 0, 0.6, button='left') # drag 900 pixles to the right to loot
    time.sleep(0.1)

def chest_deposit():
    time.sleep(0.1)
    pyautogui.press("q") # open spell bar
    time.sleep(0.3)
    pyautogui.click(1723, 973) # click deposit chest
    time.sleep(0.1)
    pyautogui.press("q") # close spell bar
    time.sleep(0.2)

def claim_arcade():
    time.sleep(0.1)
    pyautogui.press("c") # open codex
    time.sleep(0.1)
    pyautogui.click(1180, 200) # quick ref
    time.sleep(0.1)
    pyautogui.click(1313, 562) # arcade
    time.sleep(0.2)
    pyautogui.click(1564, 70) # claim
    time.sleep(0.1)
    pyautogui.click(1814, 71) # exit
    time.sleep(0.1)

activate_game()
for i in range(1,9):
    anvil_deposit()
    if i == 1: # if first itteration claim arcade balls and dont loot
        claim_arcade()
    else:
        loot()
    chest_deposit()
    select_player(i)
    claim_afk()
    if i == 6:
        claim_traps()
    if i == 8:
        anvil_deposit()
        loot()
        chest_deposit()