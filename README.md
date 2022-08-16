
A scalable flask webapp to forecast cryptocurrency prices. The forecasting model is built using stacked LSTM for one-to-one sequence 
of the timeseries.

## Requirements
* binance api
```
$ python -m pip install python-binance
```
* tensorflow 1.x / keras 2.2.5 
* flask
* numpy
* pandas
* matplotlib

## Running the webapp
```
$ cd webapp
$ python3 app.py
Open your internet browser and search for "localhost:5000" in the URL box.
```
## Snapshots


### Realtime deployment
* add/replace trained models in webapp/cryptoviz/models/
* use API intergration for extracting prices until current timestamp to predict for future(binance lets you extract prices until 3 hours ago...best case)
* automate the prediction for continous forecast
