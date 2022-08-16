from flask import Flask
import numpy as np
import pandas as pd
from binance.client import Client
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle


def data_extract1(sym, start, end):
    #API_KEY = 'QQw1C8spEaQWOvao9vgy8YSF1H0Ac4zoLl3C4DyxERYOrY1BJtYA5udNDtzmeVJ7'
    #SECRET_KEY = 'B0o7kgGeFjGxIrsVNX9Qp9ZxkVKDei9KpzjlKoT8jjy6PK6OL7YladmnTx2VuvmZ'
    client = Client('API_KEY', 'SECRET_KEY')
    if end =="":
        cryptocurrency = client.get_historical_klines(symbol=sym, interval=Client.KLINE_INTERVAL_1MONTH, start_str=start)
    else:
        cryptocurrency = client.get_historical_klines(symbol=sym, interval=Client.KLINE_INTERVAL_1MONTH, start_str=start, end_str=end)

    cryptocurrency = pd.DataFrame(cryptocurrency, columns=['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'])
    cryptocurrency['Open time'] = pd.to_datetime(cryptocurrency['Open time'], unit='ms')
    cryptocurrency.set_index('Open time', inplace=True)
    #print(CRYPTOCURRENCY.head())
    return cryptocurrency

# Select main columns to be used in training





#skf = StratifiedKFold(n_splits = 10,shuffle=True,random_state=199)
# Split data into train and test sets

