# Anti-AFK for ROBLOX
# NullUsxr 2022
import os
import platform
import time
print("Starting...")
platform = platform.system()
if platform.lower == 'windows':
    import pydirectinput
    print("NOTICE: At this time, push notifications are not available for Windows.")
else:
    import pyautogui


def notify(title, text):  # Push Notifications for macOS
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


time.sleep(5)
cycle_count = 0
if platform.lower() == 'linux':
    print("Unsupported Operating System.")
    exit(1)
print("AntiAFK is now active")
if platform.lower() == 'darwin':
    notify("NullUsxrs AntiAFK Program", "AntiAFK is now active")
while 1 == 1:
    cycle_count = cycle_count + 1
    time.sleep(1000)  # 16m40s because being afk kicked over 1100.
    if platform.lower() == 'darwin':
        notify("NullUsxrs AntiAFK Program", "Please make ROBLOX the active window within 20 seconds")
        time.sleep(20)
        pyautogui.keyDown("DOWN")
        time.sleep(1)
        pyautogui.keyUp("DOWN")
    if platform.lower() == 'Windows':
        print("Please make ROBLOX the active window within 20 seconds")
        time.sleep(20)
        pydirectinput.keyDown("DOWN")
        time.sleep(1)
        pydirectinput.keyUp("DOWN")
    print("Cycles:", cycle_count)
