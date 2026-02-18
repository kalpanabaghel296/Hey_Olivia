from googletrans import Translator

translator = Translator()

def to_english(text):
    return translator.translate(text, dest="en").text

def to_hindi(text):
    return translator.translate(text, dest="hi").text
