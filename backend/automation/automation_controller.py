import pyautogui


class AutomationController:

    # -----------------------
    # SCROLL DOWN
    # -----------------------
    def scroll_down(self):
        try:
            pyautogui.scroll(-500)

            return {
                "status": "success",
                "message": "Scrolling down"
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

    # -----------------------
    # SCROLL UP
    # -----------------------
    def scroll_up(self):
        try:
            pyautogui.scroll(500)

            return {
                "status": "success",
                "message": "Scrolling up"
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

    # -----------------------
    # TYPE TEXT
    # -----------------------
    def type_text(self, text):
        try:
            pyautogui.write(text, interval=0.05)

            return {
                "status": "success",
                "message": f"Typing {text}"
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

    # -----------------------
    # PRESS ENTER
    # -----------------------
    def press_enter(self):
        try:
            pyautogui.press("enter")

            return {
                "status": "success",
                "message": "Pressed enter"
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

    # -----------------------
    # CLOSE TAB
    # -----------------------
    def close_tab(self):
        try:
            pyautogui.hotkey("ctrl", "w")

            return {
                "status": "success",
                "message": "Closing tab"
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

    # -----------------------
    # SWITCH TAB
    # -----------------------
    def switch_tab(self):
        try:
            pyautogui.hotkey("ctrl", "tab")

            return {
                "status": "success",
                "message": "Switching tab"
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }