import pyautogui, sys, time
import win32gui
from datetime import datetime
from pyscreeze import ImageNotFoundException


# Functions
def anvil_deposit():
    time.sleep(0.1)
    pyautogui.press("c")
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
            if "idleon" in i[1].lower():
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
            x, y = pyautogui.locateCenterOnScreen('E:/Users/The Beast/Desktop/Programmering/idleon/images/claim.png', confidence=0.8)
            pyautogui.click(x,y)
            break
        except TypeError:
            time_delta = datetime.now() - startloop_time
            if time_delta.total_seconds() >= 5:
                print("Could not find the required screen. Document creating for this order aborted")
                break
            pass


    

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
        pyautogui.click(645, 272) # click player 1 loc
        time.sleep(0.1)
    elif player == 2 or player == 8:
        pyautogui.click(973, 296) # click player 2 loc
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
    x, y = pyautogui.locateCenterOnScreen('E:/Users/The Beast/Desktop/Programmering/idleon/images/player_loc.png', confidence=0.9)
    pyautogui.moveTo(x-350, y-70)
    time.sleep(0.4)
    pyautogui.drag(900, 0, 0.6, button='left')
    time.sleep(0.1)

def chest_deposit():
    print("TODO")
    #todo: code this function


activate_game()
for i in range(1,9):
    anvil_deposit()
    loot()
    # Todo: create chest deposit function
    select_player(i)
    claim_afk()
    if i == 6:
        anvil_deposit()
        loot()