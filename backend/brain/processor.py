from backend.system.system_controller import SystemController
from backend.browser.browser_controller import BrowserController
from backend.automation.automation_controller import AutomationController

import datetime
import os
import subprocess

system = SystemController()
browser = BrowserController()
automation = AutomationController()

def process_command(text):

    text = text.lower().strip()

    # ---------------- IDENTITY ----------------
    if "name" in text or "what is your name" in text:
        return "IDENTITY", "Hello! My name is Olivia, your AI desktop assistant."

    if "doing" in text or "what are you doing" in text:
        return "STATUS", "I am here to help you with your work."

    if "created" in text or "who made you" in text:
        return "CREATOR", "I was developed to be your personal smart assistant."

    if "hello" in text or "hi" in text:
        return "GREETING", "Hello, how can I help you?"

    # ---------------- TIME ---------------- 
    if "time" in text:
        now = datetime.datetime.now().strftime("%H:%M")
        return "TIME", f"The current time is {now}"

    # ---------------- OPEN APPLICATION ----------------
    if text.startswith("open "):

        if "youtube" in text:
            result = browser.open_youtube()
            return "OPEN_YOUTUBE", result["message"]

        app_name = text.replace("open ", "").strip()
        result = system.open_app(app_name)

        return "OPEN_APP", result["message"]

    # ---------------- SHUTDOWN ----------------
    if "shutdown" in text:
        result = system.shutdown()
        return "SHUTDOWN", result["message"]

    # ---------------- RESTART ----------------
    if "restart" in text:
        result = system.restart()
        return "RESTART", result["message"]

    # ---------------- LOCK ----------------
    if "lock" in text:
        result = system.lock()
        return "LOCK", result["message"]

    # ---------------- GOOGLE SEARCH ----------------
    if text.startswith("search "):
        query = text.replace("search ", "").strip()
        result = browser.search_google(query)

        return "SEARCH_GOOGLE", result["message"]

    # ---------------- YOUTUBE SEARCH ----------------
    if text.startswith("play "):
        query = text.replace("play ", "").strip()
        result = browser.search_youtube(query)

        return "YOUTUBE_SEARCH", result["message"]

    # ---------------- AUTOMATION ----------------
    if "scroll down" in text:
        result = automation.scroll_down()
        return "SCROLL_DOWN", result["message"]

    if "scroll up" in text:
        result = automation.scroll_up()
        return "SCROLL_UP", result["message"]

    if text.startswith("type "):
        message = text.replace("type ", "").strip()
        result = automation.type_text(message)

        return "TYPE_TEXT", result["message"]

    if "press enter" in text:
        result = automation.press_enter()
        return "ENTER", result["message"]

    if "switch tab" in text:
        result = automation.switch_tab()
        return "SWITCH_TAB", result["message"]

    if "close tab" in text:
        result = automation.close_tab()
        return "CLOSE_TAB", result["message"]

    # Special handling for Microsoft Teams
    if "teams" in app:
        teams_paths = [
            os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Teams\Update.exe --processStart Teams.exe"),
            os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Teams\current\Teams.exe")
        ]

    for path in teams_paths:
        try:
            subprocess.Popen(path, shell=True)
            return {
                "status": "success",
                "message": "Opening Microsoft Teams"
            }
        except:
            pass

    if "search" in text and "youtube" in text:
        query = text.replace("search", "").replace("on youtube", "")
        return browser.browser_controller.search_youtube(query)

    elif "play" in text:
        query = text.replace("play", "")
        return browser.browser_controller.play_youtube(query)        
    # ---------------- FALLBACK ----------------
    return "UNKNOWN", "Sorry, I did not understand that."