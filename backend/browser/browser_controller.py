import webbrowser
import urllib.parse
import pywhatkit


class BrowserController:

    # ------------------------
    # OPEN ANY WEBSITE
    # ------------------------
    def open_website(self, site):
        try:
            url = f"https://{site}"
            webbrowser.open(url)

            return {
                "status": "success",
                "message": f"Opening {site}"
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }


    # ------------------------
    # GOOGLE SEARCH
    # ------------------------
    def search_google(self, query):
        try:
            query = urllib.parse.quote(query)
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)

            return {
                "status": "success",
                "message": f"Searching Google for {query}"
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }


    # ------------------------
    # OPEN YOUTUBE
    # ------------------------
    def open_youtube(self):
        try:
            webbrowser.open("https://www.youtube.com")

            return {
                "status": "success",
                "message": "Opening YouTube"
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }


    # ------------------------
    # SEARCH YOUTUBE
    # ------------------------
    def search_youtube(self, query):
        try:
            query = urllib.parse.quote(query)
            url = f"https://www.youtube.com/results?search_query={query}"

            webbrowser.open(url)

            return {
                "status": "success",
                "message": f"Searching YouTube for {query}"
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }


    # ------------------------
    # PLAY YOUTUBE VIDEO
    # ------------------------
    def play_youtube(self, query):
        try:
            pywhatkit.playonyt(query)

            return {
                "status": "success",
                "message": f"Playing {query} on YouTube"
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }