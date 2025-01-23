import requests
from django.conf import settings

class NewsAPIAdapter:
    BASE_URL = 'https://newsapi.org/v2/everything'

    def __init__(self):
        self.api_key = settings.NEWS_API_KEY

    def fetch_news(self, query, from_date, to_date):
        params = {
            'q': query,
            'from': from_date,
            'to': to_date,
            'apiKey': self.api_key
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()
        return self._normalize_data(data['articles'])

    def _normalize_data(self, articles):
        normalized_articles = []
        for article in articles:
            normalized_article = {
                'source': article['source']['name'],
                'author': article['author'],
                'title': article['title'],
                'description': article['description'],
                'url': article['url'],
                'published_at': article['publishedAt'],
                'content': article['content']
            }
            normalized_articles.append(normalized_article)
        return normalized_articles
