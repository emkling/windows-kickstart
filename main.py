import json
import os
import subprocess
from pywinauto import Application, Desktop
import time

def read_json_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: {file_name} contains invalid JSON.")
        return None

def open_and_position_apps(app_data):
    if app_data is None:
        return

    monitors = app_data.get("monitors", {})
    apps = app_data.get("apps", [])

    for app in apps:
        path = app.get("path", "")
        position = app.get("position", {})
        monitor = monitors.get(position.get("monitor", ""), {})
        title = position.get("title", "")

        if not path or not position or not monitor:
            print("Error: Invalid app configuration.")
            continue

        try:
            subprocess.Popen(path)
        except FileNotFoundError:
            print(f"Error: Application not found at {path}.")
            continue

        attempts = 10
        while attempts > 0:
            attempts -= 1
            time.sleep(1)
            try:
                app_instance = Application(backend="uia").connect(title=title)
                app_window = app_instance.top_window()
                if app_window:
                    app_window.move_window(position.get("left", 0) + monitor.get("left", 0), position.get("top", 0) + monitor.get("top", 0))
                    app_window.resize(position.get("width", 0), position.get("height", 0))
                    break
            except Exception as e:
                print(f"Error: {e}")
                continue

if __name__ == "__main__":
    config_file = "config.json"
    app_data = read_json_file(config_file)
    open_and_position_apps(app_data)