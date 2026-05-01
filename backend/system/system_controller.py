import subprocess
import os
import glob
import platform


class SystemController:
    """
    Handles Windows system-level commands such as
    opening applications, shutdown, restart, etc.
    """

    def __init__(self):
        self.os_name = platform.system().lower()

        # Known Windows system apps
        self.system_apps = {
            "file explorer": "explorer",
            "explorer": "explorer",
            "calculator": "calc",
            "calc": "calc",
            "notepad": "notepad",
            "command prompt": "cmd",
            "cmd": "cmd",
            "powershell": "powershell",
            "settings": "start ms-settings:",
            "copilot": "start ms-copilot:",
            "co pilot": "start ms-copilot:",
            "teams": "start ms-teams:",
            "edge": "start msedge",
            "camera": "start microsoft.windows.camera:",
            "control panel": "control"
        }

    # ---------------------------
    # OPEN APPLICATION
    # ---------------------------
    def open_app(self, app_name: str):

        try:
            app = app_name.strip().lower()

            # 1️⃣ Check known Windows apps
            if app in self.system_apps:

                subprocess.Popen(self.system_apps[app], shell=True)

                return {
                    "status": "success",
                    "message": f"Opening {app_name}"
                }

            # 2️⃣ Search Start Menu shortcuts
            start_menu_paths = [
                r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
                os.path.expandvars(
                    r"%APPDATA%\Microsoft\Windows\Start Menu\Programs")
            ]

            for path in start_menu_paths:

                matches = glob.glob(
                    os.path.join(path, f"**\\*{app}*.lnk"), recursive=True)

                if matches:

                    subprocess.Popen(matches[0], shell=True)

                    return {
                        "status": "success",
                        "message": f"Opening {app_name}"
                    }

            # 3️⃣ Fallback launcher
            subprocess.Popen(f'start "" "{app}"', shell=True)

            return {
                "status": "success",
                "message": f"Trying to open {app_name}"
            }

        except Exception as e:

            return {
                "status": "error",
                "message": f"Could not open {app_name}: {str(e)}"
            }

    # ---------------------------
    # OPEN CALENDAR
    # ---------------------------
    def open_calendar(self):

        try:

            subprocess.Popen("start outlookcal:", shell=True)

            return {
                "status": "success",
                "message": "Opening calendar"
            }

        except Exception as e:

            return {
                "status": "error",
                "message": str(e)
            }

    # ---------------------------
    # SHUTDOWN SYSTEM
    # ---------------------------
    def shutdown(self):

        try:

            os.system("shutdown /s /t 5")

            return {
                "status": "success",
                "message": "Shutting down the system"
            }

        except Exception as e:

            return {
                "status": "error",
                "message": str(e)
            }

    # ---------------------------
    # RESTART SYSTEM
    # ---------------------------
    def restart(self):

        try:

            os.system("shutdown /r /t 5")

            return {
                "status": "success",
                "message": "Restarting the system"
            }

        except Exception as e:

            return {
                "status": "error",
                "message": str(e)
            }

    # ---------------------------
    # LOCK SYSTEM
    # ---------------------------
    def lock(self):

        try:

            os.system("rundll32.exe user32.dll,LockWorkStation")

            return {
                "status": "success",
                "message": "Locking the system"
            }

        except Exception as e:

            return {
                "status": "error",
                "message": str(e)
            }