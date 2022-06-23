# Anti-AFK for ROBLOX
# NullUsxr 2022
import time
import pyautogui
import os


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


print("Starting...")
time.sleep(5)
cyclecount = 0
notify("NullUsxrs AntiAFK Program", "AntiAFK is now active")
print("AntiAFK is now active")
while 1 == 1:
    cyclecount = cyclecount + 1
    tt = 20 * cyclecount
    time.sleep(1210)
    notify("NullUsxrs AntiAFK Program", "Please make ROBLOX the active window within 20 seconds")
    time.sleep(20)
    pyautogui.keyDown("DOWN")
    time.sleep(1)
    pyautogui.keyUp("DOWN")
    print("Cycles:", cyclecount)
    print("Time:", tt)
