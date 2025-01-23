import requests
import pandas as pd
from django.conf import settings

class AlphaVantageAdapter:
    BASE_URL = 'https://www.alphavantage.co/query'

    def __init__(self):
        self.api_key = settings.ALPHA_VANTAGE_KEY

    def fetch_daily_data(self, symbol):
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': symbol,
            'apikey': self.api_key
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()
        return self._normalize_data(data['Time Series (Daily)'])

    def _normalize_data(self, data):
        df = pd.DataFrame.from_dict(data, orient='index')
        df.index = pd.to_datetime(df.index)
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        df = df.astype(float)
        return df
