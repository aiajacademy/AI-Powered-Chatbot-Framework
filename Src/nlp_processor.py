import spacy

class NLPProcessor:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def process_input(self, user_input):
        doc = self.nlp(user_input)
        processed_input = [token.lemma_ for token in doc]
        return processed_input

    def generate_response(self, processed_input, sentiment, context):
        # Generate a simple response based on the processed input, sentiment, and context
        if 'hello' in processed_input:
            return "Hi there! How can I help you today?"
        elif 'bye' in processed_input:
            return "Goodbye! Have a great day!"
        else:
            return "I'm not sure how to respond to that."

