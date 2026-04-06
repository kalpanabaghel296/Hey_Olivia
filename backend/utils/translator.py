try:
    from googletrans import Translator as GoogleTranslator
except Exception:
    GoogleTranslator = None


# initialize safely
translator = GoogleTranslator() if GoogleTranslator else None


def to_english(text: str) -> str:
    try:
        if not translator:
            return text  # fallback

        result = translator.translate(text, dest="en")
        return result.text

    except Exception as e:
        print("Translator error (EN):", e)
        return text  # fallback


def to_hindi(text: str) -> str:
    try:
        if not translator:
            return text  # fallback

        result = translator.translate(text, dest="hi")
        return result.text

    except Exception as e:
        print("Translator error (HI):", e)
        return text  # fallback