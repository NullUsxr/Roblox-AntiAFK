# Anti-AFK for ROBLOX
# NullUsxr 2022
import os
import platform
import time

start = "AntiAFK is now active"
active = "Please make ROBLOX the active window within 20 seconds"
print("[INFO] Starting...")
platform = platform.system()
if platform == 'Linux':
    import subprocess
    import pyautogui
if platform == 'Windows':
    import pydirectinput
    from plyer import notification
    print("[ALERT] Support for Windows is not complete yet and AntiAFK may not work for you")
    print("If you would like to help make Windows supported,")
    print("you can do so here: https://github.com/NullUsxr/Roblox-AntiAFK")
else:
    import pyautogui


def linuxnotify(message):
    subprocess.run(
        ["notify-send", "-u", "normal", "-t", "5000", message, "NullUsxrs AntiAFK Program"], check=True)


def macnotify(text):  # Push Notifications for macOS
    os.system("""
              osascript -e 'display notification "NullUsxrs AntiAFK Program" with title "{}"'
              """.format(text))


def winotify(text):
    notification.notify(
        title='NullUsxrs AntiAFK Program',
        message=text,
        app_icon=None,
        timeout=10,
    )


time.sleep(5)
cycle_count = 0
print("[INFO] AntiAFK is now active")
if platform == 'Darwin':
    macnotify("AntiAFK is now active")
if platform == 'Linux':
    linuxnotify("AntiAFK is now active")
if platform == 'Windows':
    winotify(start)
while 1 == 1:
    cycle_count = cycle_count + 1
    time.sleep(1000)  # 16m40s because being afk kicked over 1100.
    print("[ALERT] Please make ROBLOX the active window within 20 seconds")
    if platform == 'Windows':
        winotify(active)
        time.sleep(20)
        pydirectinput.keyDown('LEFT')
        time.sleep(1)
        pydirectinput.keyUp('LEFT')
    else:
        if platform == 'Darwin':
            macnotify(active)
        if platform == 'Linux':
            linuxnotify(active)
        time.sleep(20)
        pyautogui.keyDown('LEFT')
        time.sleep(1)
        pyautogui.keyUp('LEFT')
    print("[INFO] Cycles:", cycle_count)
