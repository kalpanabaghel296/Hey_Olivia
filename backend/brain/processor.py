def process_command(text):
    text = text.lower()

    # 1. Identity Command (What is your name)
    if "name" in text or "what is your name" in text:
        return "IDENTITY", "Hello! My name is Olivia, an AI desktop assistant, created to make your life easier."

    if "doing" in text or "what are you doing" in text:
        return "STATUS", "I am here for you to help with your work and manage your tasks efficiently."

    if "created" in text or "who made you" in text:
        return "CREATOR", "I was developed to be your personal smart assistant."

    if "time" in text:
        return "TIME", "The current time feature will be added soon."

    if "hello" in text or "hi" in text:
        return "GREETING", "Hello, how can I help you?"

    if "weather" in text:
        return "WEATHER", "Weather feature will be added soon."
    
    return "UNKNOWN", "Sorry, I did not understand that."