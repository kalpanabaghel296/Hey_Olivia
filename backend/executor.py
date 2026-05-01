# backend/executor.py
from backend.browser.browser_controller import BrowserController
from backend.system.system_controller import SystemController
from backend.automation.automation_controller import AutomationController

class ActionExecutor:
    def __init__(self):
        self.browser = BrowserController()
        self.system = SystemController()
        self.automation = AutomationController()

        # 🔑 Intent → (controller, method)
        self.intent_map = {
            "open_app": (self.system, "open_app"),
            "shutdown": (self.system, "shutdown"),
            "restart": (self.system, "restart"),

            "open_website": (self.browser, "open_website"),
            "search_google": (self.browser, "search_google"),
            "open_youtube": (self.browser, "open_youtube"),
            "search_youtube": (self.browser, "search_youtube"),
            "play_youtube": (self.browser, "play_youtube"),

            "scroll_down": (self.automation, "scroll_down"),
            "scroll_up": (self.automation, "scroll_up"),
            "type_text": (self.automation, "type_text"),
            "press_enter": (self.automation, "press_enter"),
            "close_tab": (self.automation, "close_tab"),
            "switch_tab": (self.automation, "switch_tab"),
        }

    def execute(self, action_data):
        results = []

        if not action_data or "actions" not in action_data:
            return ["No valid actions"]

        for action in action_data["actions"]:
            intent = action.get("intent")
            mapping = self.intent_map.get(intent)

            if not mapping:
                results.append(f"Unknown intent: {intent}")
                continue

            controller, method_name = mapping
            method = getattr(controller, method_name, None)

            try:
                if intent == "open_app":
                    res = method(action.get("app"))

                elif intent == "open_website":
                    res = method(action.get("site"))

                elif intent in ["search_google", "search_youtube", "play_youtube"]:
                    res = method(action.get("query"))

                elif intent == "type_text":
                    res = method(action.get("text"))

                else:
                    res = method()

                if isinstance(res, dict):
                        results.append(res.get("message", ""))

            except Exception as e:
                results.append(str(e))

        return results