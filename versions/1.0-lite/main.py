# NullUsxr 2022 | Roblox AntiAFK program
import time
import pyautogui
print("Starting...")
time.sleep(5)
print("[INFO] AntiAFK is now active")
while 1 == 1:
    time.sleep(1000)
    print("[ALERT] Please make Roblox the active window")
    time.sleep(20)
    pyautogui.keyDown('LEFT')
    time.sleep(1)
    pyautogui.keyUp('LEFT')
    print("[INFO] Completed a cycle")
