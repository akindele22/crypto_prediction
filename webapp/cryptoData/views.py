from re import M
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from flask import Flask, render_template, request
from cryptoData.util import data_extract, plot_graph
from cryptoData.util2 import data_extract1
from cryptoData import *
from sklearn.model_selection import train_test_split

    
# method to predict cryptocurrency price and render the plot on home/predict
@flaskapp.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == "POST":
        crypto = request.form.get('crypto')
        start = request.form.get('start')
        end = request.form.get('end')
        #print(crypto,end,end)

        if crypto == "bitcoin":
            sym  = "BTCUSDT"
        elif crypto == "ethereum":
            sym = "ETHUSDT"
        elif crypto == "ripple":
            sym = "XRPUSDT"
        elif crypto == "litecoin":
            sym = "LTCUSDT"
        elif crypto == "avax":
            sym = "AVAXUSDT"
        elif crypto == "ada":
            sym = "ADAUSDT"
        elif crypto == "tron":
            sym = "TRXUSDT"
        elif crypto == "bnb":
            sym = "BNBUSDT"
        elif crypto == "bch":
            sym = "BCHUSDT"
        elif crypto == "doge":
            sym = "DOGEUSDT"
        elif crypto == "dot":
            sym = "DOGEUSDT"
        elif crypto == "ftt":
            sym = "FTTUSDT"
        elif crypto == "link":
            sym = "LINKUSDT"
        elif crypto == "luna":
            sym = "LUNAUSDT"
        elif crypto == "matic":
            sym = "MATICUSDT"
        elif crypto == "near":
            sym = "NEARUSDT"
        elif crypto == "sol":
            sym = "SOLUSDT"
        elif crypto == "uni":
            sym = "UNIUSDT"
        elif crypto == "usdc":
            sym = "USDCUSDT"
        elif crypto == "etc":
            sym = "ETCUSDT"
        elif crypto == "atom":
            sym = "ATOMUSDT"
            print("cryptocurrency not available")
            return render_template("home.html")
        # add other cryptocurrencies here

        # fetch data
        data = data_extract(sym,start,end)
        df = data_extract1(sym,start,end)
        #print(data)

        X = df
        y = df
        X_train, X_test2, y_train, y_test2 = train_test_split(X,y,test_size=0.2, random_state=42)
        # preprocessing the data
        scaler= MinMaxScaler()
        data = scaler.fit_transform(data)
        #print(data)

        # reshaping data
        X_test = data[0:len(data)-1]
        y_test = data[1:len(data)]
        X_test = np.reshape(X_test, (len(X_test), 1, X_test.shape[1]))
        #X_test2 = df[0:len(data)-1]
        #X_test2 = np.reshape(X_test2,(len(X_test2), 1,  X_test2.shape[1]))
        
        #X_test2 = data[len(data)-1:]
        predicted_price = 0
        cls =''
        # Perform predictions on test data
        if crypto == "bitcoin":
            predicted_price = btc_model.predict(X_test)
            if (pred_clf_btc().predict(X_test2) == 1).any():
                cls = 'Buy'
            elif (pred_clf_btc().predict(X_test2) == -1).any():
                cls = 'Sell'
            else:
                cls = 'ranging'
        elif crypto == "ethereum":
            predicted_price = ethM_model.predict(X_test)
        elif crypto == "ripple":
            predicted_price = xrp_model.predict(X_test)
        elif crypto == "ada":
            predicted_price = adaM_model.predict(X_test)
        elif crypto == "avax":
            predicted_price = avaxM_model.predict(X_test)
        elif crypto == "tron":
            predicted_price = trxM_model.predict(X_test)
        elif crypto == "ltc":
            predicted_price = ltcM_model.predict(X_test)
        elif crypto == "bnb":
            predicted_price = bnbM_model.predict(X_test)
        elif crypto == "bch":
            predicted_price = bchM_model.predict(X_test)
        elif crypto == "doge":
            predicted_price = dogeM_model.predict(X_test)
        elif crypto == "dot":
            predicted_price = dotM_model.predict(X_test)
        elif crypto == "etc":
            predicted_price = etcM_model.predict(X_test)
        elif crypto == "ftt":
            predicted_price = fttM_model.predict(X_test)
        elif crypto == "link":
            predicted_price = linkM_model.predict(X_test)
        elif crypto == "luna":
            predicted_price = lunaM_model.predict(X_test)
        elif crypto == "matic":
            predicted_price = maticM_model.predict(X_test)
        elif crypto == "near":
            predicted_price = nearM_model.predict(X_test)
        elif crypto == "sol":
            predicted_price = solM_model.predict(X_test)
        elif crypto == "usdc":
            predicted_price = usdcM_model.predict(X_test)
        elif crypto == "uni":
            predicted_price = uniM_model.predict(X_test)
        elif crypto == "atom":
            predicted_price = atomM_model.predict(X_test)
        else:
            print('Not in the pair coin')
        # add other models here

        predicted_price = scaler.inverse_transform(predicted_price)
        real_price = scaler.inverse_transform(y_test)
        prediction = predicted_price[:1]
        
        #cls = scaler.inverse_transform(bbb)
        #pred = scaler.inverse_transform(cls)
        prediction1 = cls

        # plot graph
        p_url = plot_graph(crypto, predicted_price, real_price)

    return render_template("predict.html",plot_url='data:image/png;base64,{}'.format(p_url),prediction = prediction, prediction1 = prediction1)


# Home page that is rendered for every web call
@flaskapp.route("/")
def home():
    return render_template("home.html")
