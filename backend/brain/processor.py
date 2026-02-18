def process_command(text):
    text = text.lower()

    if "time" in text:
        return "TIME", "The current time feature will be added soon."

    if "hello" in text or "hi" in text:
        return "GREETING", "Hello, how can I help you?"

    if "weather" in text:
        return "WEATHER", "Weather feature will be added soon."

    return "UNKNOWN", "Sorry, I did not understand that."
