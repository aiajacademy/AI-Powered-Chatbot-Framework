# Usage Guide

## Basic Usage

1. Import the chatbot framework:
   ```python
   from src.chatbot_engine import ChatbotEngine

   chatbot = ChatbotEngine()
   response = chatbot.get_response("Hello, how are you?")
   print(response)
