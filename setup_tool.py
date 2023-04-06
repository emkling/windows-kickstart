import ctypes.wintypes
import os
import subprocess
import time

def get_notepad_window_handle():
    try:
        return ctypes.windll.user32.FindWindowW(None, "Notepad")
    except Exception as e:
        print(f"Error getting Notepad window handle: {e}")
        return None

def get_window_position_and_size(hwnd):
    try:
        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.GetWindowRect(hwnd, ctypes.pointer(rect))
        return rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top
    except Exception as e:
        print(f"Error getting window position and size: {e}")
        return None, None, None, None

def window_locater():
    try:
        app_process = subprocess.Popen("C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2302.26.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe")
    except Exception as e:
        print(f"Error launching Notepad: {e}")
        return

    time.sleep(4)  # Wait for the application to open

    hwnd = get_notepad_window_handle()

    if not hwnd:
        print("Notepad window not found.")
        return

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        left, top, width, height = get_window_position_and_size(hwnd)
        if left is not None and top is not None and width is not None and height is not None:
            print(f"Notepad Window Position and Size:")
            print(f"Left: {left}")
            print(f"Top: {top}")
            print(f"Width: {width}")
            print(f"Height: {height}")
        print("Press enter to refresh window position and 'q' to quit.")
        time.sleep(0.1)

        if 'q' in input():  # Wait for the user to press 'q'
            break

window_locater()