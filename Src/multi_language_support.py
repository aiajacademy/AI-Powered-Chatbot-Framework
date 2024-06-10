from googletrans import Translator

class LanguageSupport:
    def __init__(self):
        self.translator = Translator()

    def translate_response(self, response, target_language='en'):
        translated_response = self.translator.translate(response, dest=target_language)
        return translated_response.text

