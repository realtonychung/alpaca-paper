import os, csv
import talib
import yfinance as yf
import pandas
import json

from patterns import candlestick_patterns

filtered_patterns = dict()
# for each one of the patterns
# if it doesn't match any of the csvs you listed, we'll exclude
for (key, value) in candlestick_patterns.items():
    for filename in os.listdir('datasets/daily'):
        df = pandas.read_csv('datasets/daily/{}'.format(filename))
        pattern_function = getattr(talib, key)
        symbol = filename.split('.')[0]

        try:
            results = pattern_function(df['Open'], df['High'], df['Low'], df['Close'])
            last = results.tail(1).values[0]

            if last == 0:
                continue
            else:
                filtered_patterns[key] = value
        except Exception as e:
            print('failed on filename: ', filename)

json.dump(filtered_patterns, open("filtered_patterns.txt", "w"))
print("operation complete")
