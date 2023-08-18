import os
import shutil
import platform

def clean_temp_folders():
    temp_folders = [
        os.path.join(os.environ.get("TEMP"), "Temporary Internet Files"),
        os.path.join(os.environ.get("TEMP"), "Temp"),
        os.path.join(os.environ.get("USERPROFILE"), "AppData", "Local", "Temp")
    ]

    for folder in temp_folders:
        if os.path.exists(folder):
            print(f"Cleaning {folder}...")
            try:
                shutil.rmtree(folder)
                print(f"{folder} cleaned.")
            except Exception as e:
                print(f"Error cleaning {folder}: {e}")

def clean_browser_cache():
    browsers_cache = {
        "Chrome": os.path.join(os.environ.get("LOCALAPPDATA"), "Google", "Chrome", "User Data"),
        "Edge": os.path.join(os.environ.get("LOCALAPPDATA"), "Microsoft", "Edge", "User Data"),
        "Firefox": os.path.join(os.environ.get("LOCALAPPDATA"), "Mozilla", "Firefox", "Profiles")
    }

    for browser, cache_path in browsers_cache.items():
        if os.path.exists(cache_path):
            print(f"Cleaning {browser} cache...")
            try:
                shutil.rmtree(cache_path)
                print(f"{browser} cache cleaned.")
            except Exception as e:
                print(f"Error cleaning {browser} cache: {e}")

def clean_system_logs():
    if platform.system() == "Windows":
        event_logs_path = os.path.join(os.environ.get("SystemRoot"), "System32", "winevt", "Logs")
        if os.path.exists(event_logs_path):
            print("Cleaning system event logs...")
            try:
                for log_file in os.listdir(event_logs_path):
                    if log_file.endswith(".evtx"):
                        log_file_path = os.path.join(event_logs_path, log_file)
                        os.remove(log_file_path)
                print("System event logs cleaned.")
            except Exception as e:
                print(f"Error cleaning system event logs: {e}")

def main():
    print("Starting disk cleanup...")

    clean_temp_folders()
    clean_browser_cache()
    clean_system_logs()

    print("Disk cleanup completed.")

if __name__ == "__main__":
    main()
