import requests
import pandas as pd
from celery import shared_task
from django.conf import settings
from .models import TimeSeriesModel

@shared_task
def fetch_and_process_data():
    # Fetch data from AlphaVantage API
    response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NIFTY50&apikey={settings.ALPHA_VANTAGE_KEY}')
    data = response.json()

    # Normalize data using Pandas
    df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
    df.index = pd.to_datetime(df.index)
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    df = df.astype(float)

    # Save data to the database
    for index, row in df.iterrows():
        TimeSeriesModel.objects.create(
            date=index,
            open=row['open'],
            high=row['high'],
            low=row['low'],
            close=row['close'],
            volume=row['volume']
        )
