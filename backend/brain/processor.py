from backend.system.system_controller import SystemController
from backend.browser.browser_controller import BrowserController
from backend.automation.automation_controller import AutomationController
from backend.utils.llm_client import GroqClient
from backend.run_command import run_command

import datetime
import os
import subprocess

system = SystemController()
browser = BrowserController()
automation = AutomationController()

llm = GroqClient()

def process_command(text):

    try:
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
                return "OPEN_YOUTUBE", result.get("message", "Opening YouTube")

            if "teams" in text:
                teams_paths = [
                    os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Teams\current\Teams.exe"),
                    r"C:\Program Files\Microsoft Teams\current\Teams.exe"
                ]

                for path in teams_paths:
                    if os.path.exists(path):
                        subprocess.Popen(path, shell=True)
                        return "OPEN_TEAMS", "Opening Microsoft Teams"

                return "OPEN_TEAMS", "Microsoft Teams not found"

            app_name = text.replace("open ", "").strip()
            result = system.open_app(app_name)

            return "OPEN_APP", result.get("message", f"Opening {app_name}")

        # ---------------- SHUTDOWN ----------------
        if "shutdown" in text:
            result = system.shutdown()
            return "SHUTDOWN", result.get("message", "Shutting down")

        # ---------------- RESTART ----------------
        if "restart" in text:
            result = system.restart()
            return "RESTART", result.get("message", "Restarting")

        # ---------------- LOCK ----------------
        if "lock" in text:
            result = system.lock()
            return "LOCK", result.get("message", "Locking system")

        # ---------------- GOOGLE SEARCH ----------------
        if text.startswith("search ") and "youtube" not in text:
            query = text.replace("search ", "").strip()
            result = browser.search_google(query)
            return "SEARCH_GOOGLE", result.get("message", f"Searching {query}")

        # ---------------- YOUTUBE SEARCH ----------------
        if text.startswith("play "):
            query = text.replace("play ", "").strip()
            result = browser.search_youtube(query)
            return "YOUTUBE_SEARCH", result.get("message", f"Playing {query}")

        if "search" in text and "youtube" in text:
            query = text.replace("search", "").replace("on youtube", "").strip()
            result = browser.search_youtube(query)
            return "YOUTUBE_SEARCH", result.get("message", f"Searching YouTube for {query}")

        # ---------------- AUTOMATION ----------------
        if "scroll down" in text:
            result = automation.scroll_down()
            return "SCROLL_DOWN", result.get("message", "Scrolling down")

        if "scroll up" in text:
            result = automation.scroll_up()
            return "SCROLL_UP", result.get("message", "Scrolling up")

        if text.startswith("type "):
            message = text.replace("type ", "").strip()
            result = automation.type_text(message)
            return "TYPE_TEXT", result.get("message", "Typing text")

        if "press enter" in text:
            result = automation.press_enter()
            return "ENTER", result.get("message", "Pressed enter")

        if "switch tab" in text:
            result = automation.switch_tab()
            return "SWITCH_TAB", result.get("message", "Switched tab")

        if "close tab" in text:
            result = automation.close_tab()
            return "CLOSE_TAB", result.get("message", "Closed tab")

        words = text.split()
        for word in words:
            if run_command(word):
                return "CUSTOM_COMMAND", "Executing your saved command"
        # ---------------- 🧠 LLM FALLBACK ----------------
        print("🤖 Sending to Groq...")

        response = llm.generate(text)   # ✅ FIXED (important)
        return "LLM_RESPONSE", response

    except Exception as e:
        print("❌ Processor Error:", e)
        return "ERROR", f"Something went wrong: {str(e)}"
