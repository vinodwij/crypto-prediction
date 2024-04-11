# Importing the required libraries
import json
import requests
import time
import csv

# Defining the API endpoint
url = "https://api.binance.com/api/v3/ticker/24hr"

while True:
    # Requesting data from the API endpoint
    data = requests.get(url)
    data = data.json()

    # Filtering the data for BTCUSDT
    btcusdt_data = next((d for d in data if d['symbol'] == 'BTCUSDT'), None)

    if btcusdt_data:
        with open("Dataset/crypto.csv", "a", newline="") as cryptocsv:
            csv_write = csv.writer(cryptocsv)
            btc_data_list = []
            btc_data_list = [btcusdt_data['bidPrice'], btcusdt_data['askPrice'], btcusdt_data['openPrice'], btcusdt_data['highPrice'], btcusdt_data['lowPrice'], btcusdt_data['volume'], btcusdt_data['count'], btcusdt_data['lastPrice']]
            csv_write.writerow(btc_data_list)

    # Waiting for 60 seconds before making the next request
    time.sleep(5)