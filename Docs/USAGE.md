# Usage Guide

## Basic Usage

1. Import the chatbot framework:
    ```python
    from src.chatbot_engine import ChatbotEngine

    chatbot = ChatbotEngine()
    response = chatbot.get_response("Hello, how are you?")
    print(response)
    ```

## Advanced Usage

### Sentiment Analysis
The framework uses a BERT model for sentiment analysis:
    ```python
    from src.sentiment_analysis import SentimentAnalyzer

    analyzer = SentimentAnalyzer()
    sentiment = analyzer.analyze_sentiment("I am happy")
    print(sentiment)
    ```

### Context Retention
The context manager retains context over multiple interactions:
    ```python
    from src.context_retention import ContextManager

    manager = ContextManager()
    context = manager.update_context("Hello")
    context = manager.update_context("How are you?")
    print(manager.get_context())
    ```

### Multi-language Support
The framework supports multiple languages:
    ```python
    from src.multi_language_support import LanguageSupport

    translator = LanguageSupport()
    response = translator.translate_response("Hello, how are you?", target_language='es')
    print(response)
    ```

