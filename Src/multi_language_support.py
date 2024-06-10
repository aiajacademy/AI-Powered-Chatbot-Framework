from googletrans import Translator

class LanguageSupport:
    def __init__(self):
        self.translator = Translator()

    def translate_response(self, response, target_language='en'):
        # Translate response to the target language (default is English)
        translated_response = self.translator.translate(response, dest=target_language)
        return translated_response.text

