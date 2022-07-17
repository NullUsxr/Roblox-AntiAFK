# Anti-AFK for ROBLOX
# NullUsxr 2022
import os
import platform
import time
start = "AntiAFK is now active"
active = "Please make ROBLOX the active window within 20 seconds"
print("[INFO] Starting...")
platform = platform.system()

if platform.lower == 'windows':
    import pydirectinput
    from plyer import notification

else:
    import pyautogui
    
if platform.lower == 'linux':
    import subprocess

def linuxnotif(message):
    subprocess.run(
        ["notify-send", "-u", "normal", "-t", "5000", message, "NullUsxrs AntiAFK Program"], check=True)


def notify(text):  # Push Notifications for macOS
    os.system("""
              osascript -e 'display notification "NullUsxrs AntiAFK Program" with title "{}"'
              """.format(text))


time.sleep(5)
cycle_count = 0
print("[INFO] AntiAFK is now active")
if platform.lower() == 'darwin':
    notify("AntiAFK is now active")
if platform.lower() == 'linux':
    linuxnotif("AntiAFK is now active")
while 1 == 1:
    cycle_count = cycle_count + 1
    time.sleep(1000)  # 16m40s because being afk kicked over 1100.
    print("[ALERT] Please make ROBLOX the active window within 20 seconds")
    if platform.lower() == 'windows':
        notification.notify(
            title='NullUsxrs AntiAFK Program',
            message=active,
            app_icon=None,
            timeout=10,
        )
        time.sleep(20)
        pydirectinput.keyDown('LEFT')
        time.sleep(1)
        pydirectinput.keyUp('LEFT')
    else:
        if platform.lower() == 'darwin':
            notify(active)
        if platform.lower() == 'linux':
            linuxnotif(active)
        time.sleep(20)
        pyautogui.keyDown('LEFT')
        time.sleep(1)
        pyautogui.keyUp('LEFT')
    print("[INFO] Cycles:", cycle_count)
