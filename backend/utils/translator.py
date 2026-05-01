

try:
    from deep_translator import GoogleTranslator
except Exception:
    GoogleTranslator = None


def to_english(text: str) -> str:
    try:
        if not GoogleTranslator:
            return text  # fallback

        translated = GoogleTranslator(source='auto', target='en').translate(text)
        return translated

    except Exception as e:
        print("Translator error (EN):", e)
        return text  # fallback


def to_hindi(text: str) -> str:
    try:
        if not GoogleTranslator:
            return text  # fallback

        translated = GoogleTranslator(source='auto', target='hi').translate(text)
        return translated

    except Exception as e:
        print("Translator error (HI):", e)
        return text  # fallback