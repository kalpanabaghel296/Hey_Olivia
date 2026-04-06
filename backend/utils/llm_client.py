from groq import Groq
import os


class GroqClient:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")

        if not self.api_key:
            raise ValueError("GROQ_API_KEY not set in environment variables")

        self.client = Groq(api_key=self.api_key)

    def generate(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",   # ✅ FINAL WORKING MODEL
                messages=[
                    {"role": "system", "content": 
                    "You are Olivia, a smart AI voice assistant. "
                    "Always give short, clear, and direct answers in 1-2 sentences. "
                    "Do not give long paragraphs unless asked. "
                    "Speak like a human assistant."},
                    {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500,
        )

            return response.choices[0].message.content.strip()

        except Exception as e:
            return f"LLM Error: {str(e)}"