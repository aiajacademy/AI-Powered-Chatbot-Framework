import unittest
from src.chatbot_engine import ChatbotEngine

class TestChatbotEngine(unittest.TestCase):
    def setUp(self):
        self.chatbot = ChatbotEngine()

    def test_get_response(self):
        self.assertEqual(self.chatbot.get_response("hello"), "Hi there! How can I help you today?")
        self.assertEqual(self.chatbot.get_response("bye"), "Goodbye! Have a great day!")
        self.assertEqual(self.chatbot.get_response("unknown input"), "I'm not sure how to respond to that.")

if __name__ == "__main__":
    unittest.main()

