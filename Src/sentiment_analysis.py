import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification

class SentimentAnalyzer:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased')

    def analyze_sentiment(self, text):
        inputs = self.tokenizer(text, return_tensors="tf")
        outputs = self.model(inputs)
        logits = outputs.logits
        sentiment = tf.nn.softmax(logits, axis=-1)
        return sentiment.numpy()

