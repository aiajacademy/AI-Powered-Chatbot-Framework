from src.nlp_processor import NLPProcessor
from src.sentiment_analysis import SentimentAnalyzer
from src.context_retention import ContextManager
from src.multi_language_support import LanguageSupport

class ChatbotEngine:
    def __init__(self):
        self.nlp_processor = NLPProcessor()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.context_manager = ContextManager()
        self.language_support = LanguageSupport()

    def get_response(self, user_input):
        # Process user input with NLP
        processed_input = self.nlp_processor.process_input(user_input)

        # Analyze sentiment
        sentiment = self.sentiment_analyzer.analyze_sentiment(processed_input)

        # Retain context
        context = self.context_manager.update_context(user_input)

        # Generate response based on input, sentiment, and context
        response = self.nlp_processor.generate_response(processed_input, sentiment, context)

        # Translate response if needed
        response = self.language_support.translate_response(response)

        return response

def main():
    chatbot = ChatbotEngine()
    while True:
        user_input = input("You: ")
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()

