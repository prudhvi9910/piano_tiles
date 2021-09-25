import pyautogui
import time
import keyboard
import random
import win32api, win32con
from constants import T1_XPOSITION, T2_XPOSITION, T3_XPOSITION, T4_XPOSITION, T_YPOSITION

# T1: X:342 Y:700
# T2: X:442 Y:700
# T3: X:542 Y:700
# T4: X:642 Y:700

def click(x, y):
    """
    """
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(T1_XPOSITION, T_YPOSITION)[0] == 0:
        click(T1_XPOSITION, T_YPOSITION) 
    if pyautogui.pixel(T2_XPOSITION, T_YPOSITION)[0] == 0:
        click(T2_XPOSITION, T_YPOSITION) 
    if pyautogui.pixel(T3_XPOSITION, T_YPOSITION)[0] == 0:
        click(T3_XPOSITION, T_YPOSITION) 
    if pyautogui.pixel(T4_XPOSITION, T_YPOSITION)[0] == 0:
        click(T4_XPOSITION, T_YPOSITION) 