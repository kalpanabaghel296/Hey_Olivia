# backend/nlp_engine.py
from groq import Groq
import json
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def clean_text(text):
    text = text.lower().strip()
    # only if you use single-shot wake word:
    text = text.replace("olivia", "")
    return text

def build_prompt(user_input):
    return f"""
You are an AI system that extracts actionable commands from user input.

Your task is to determine whether the input contains executable system actions.

-------------------------------------
INSTRUCTIONS:
-------------------------------------

1. If the input contains CLEAR executable actions, extract them.

2. If the input is:
   - a general question
   - informational query
   - conversation
   - or does NOT require any system/browser/automation action

   THEN return:
   {{"actions": []}}

-------------------------------------
SUPPORTED ACTION TYPES:
-------------------------------------

- open_app (e.g., open notepad, open chrome)
- open_website (e.g., open google.com)
- search_google (e.g., search AI news)
- open_youtube
- search_youtube
- play_youtube (e.g., play song on youtube)
- scroll_down / scroll_up
- type_text
- press_enter
- close_tab
- switch_tab
- shutdown / restart

-------------------------------------
OUTPUT FORMAT (STRICT):
-------------------------------------

Return ONLY valid JSON.

{{
  "actions": [
    {{
      "intent": "",
      "app": "",
      "site": "",
      "platform": "",
      "query": "",
      "text": ""
    }}
  ]
}}

-------------------------------------
EXAMPLES:
-------------------------------------

Input: "open youtube and play pani pani song"
Output:
{{
  "actions": [
    {{"intent": "open_youtube"}},
    {{"intent": "play_youtube", "query": "pani pani song"}}
  ]
}}

Input: "search google for AI news"
Output:
{{
  "actions": [
    {{"intent": "search_google", "query": "AI news"}}
  ]
}}

Input: "what is artificial intelligence"
Output:
{{"actions": []}}

Input: "who is Elon Musk"
Output:
{{"actions": []}}

-------------------------------------
USER INPUT:
"{user_input}"
"""

def extract_actions(user_input):
    cleaned = clean_text(user_input)
    prompt = build_prompt(cleaned)

    try:
        res = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        text = res.choices[0].message.content.strip()
        data = json.loads(text)
        return data

    except Exception as e:
        print("NLP extraction error:", e)
        return None