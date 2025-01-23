from transformers import pipeline
from django.conf import settings

class SentimentAnalyzer:
    def __init__(self):
        self.model_name = settings.SENTIMENT_MODEL
        self.analyzer = pipeline('sentiment-analysis', model=self.model_name)

    def analyze_sentiment(self, text):
        result = self.analyzer(text)
        return result[0]['label'], result[0]['score']
