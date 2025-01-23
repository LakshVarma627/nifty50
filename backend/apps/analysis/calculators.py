import talib
import numpy as np

class TechnicalIndicators:
    def __init__(self, close_prices):
        self.close_prices = np.array(close_prices)

    def calculate_rsi(self, window=14):
        return talib.RSI(self.close_prices, timeperiod=window)

    def calculate_sma(self, window=30):
        return talib.SMA(self.close_prices, timeperiod=window)

    def calculate_ema(self, window=30):
        return talib.EMA(self.close_prices, timeperiod=window)

    def calculate_macd(self, fastperiod=12, slowperiod=26, signalperiod=9):
        macd, macdsignal, macdhist = talib.MACD(self.close_prices, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)
        return macd, macdsignal, macdhist

    def calculate_bbands(self, window=20, nbdevup=2, nbdevdn=2, matype=0):
        upperband, middleband, lowerband = talib.BBANDS(self.close_prices, timeperiod=window, nbdevup=nbdevup, nbdevdn=nbdevdn, matype=matype)
        return upperband, middleband, lowerband
