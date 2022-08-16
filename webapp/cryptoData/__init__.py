from flask import Flask
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.models import load_model
import pickle

def model_definition():
    model= Sequential()
    model.add(LSTM(256, return_sequences=True, input_shape=(1,1)))
    model.add(LSTM(256))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


btc_model = model_definition()
btc_model.load_weights("cryptoData/models/btc_model.h5")
btc_model.make_predict_function()

ltcM_model = model_definition()
ltcM_model.load_weights("cryptoData/models/ltcM_model.h5")
ltcM_model.make_predict_function()

xrp_model = model_definition()
xrp_model.load_weights("cryptoData/models/xrp_model.h5")
xrp_model.make_predict_function()

adaM_model = model_definition()
adaM_model.load_weights("cryptoData/models/adaM_model.h5")
adaM_model.make_predict_function()

avaxM_model = model_definition()
avaxM_model.load_weights("cryptoData/models/avaxM_model.h5")
avaxM_model.make_predict_function()

trxM_model = model_definition()
trxM_model.load_weights("cryptoData/models/trxM_model.h5")
trxM_model.make_predict_function()

atomM_model = model_definition()
atomM_model.load_weights("cryptoData/models/atomM_model.h5")
atomM_model.make_predict_function()

bchM_model = model_definition()
bchM_model.load_weights("cryptoData/models/bchM_model.h5")
bchM_model.make_predict_function()

bnbM_model = model_definition()
bnbM_model.load_weights("cryptoData/models/bnbM_model.h5")
bnbM_model.make_predict_function()

dogeM_model = model_definition()
dogeM_model.load_weights("cryptoData/models/dogeM_model.h5")
dogeM_model.make_predict_function()

dotM_model = model_definition()
dotM_model.load_weights("cryptoData/models/dotM_model.h5")
dotM_model.make_predict_function()

etcM_model = model_definition()
etcM_model.load_weights("cryptoData/models/etcM_model.h5")
etcM_model.make_predict_function()

ethM_model = model_definition()
ethM_model.load_weights("cryptoData/models/ethM_model.h5")
ethM_model.make_predict_function()

fttM_model = model_definition()
fttM_model.load_weights("cryptoData/models/fttM_model.h5")
fttM_model.make_predict_function()

linkM_model = model_definition()
linkM_model.load_weights("cryptoData/models/linkM_model.h5")
linkM_model.make_predict_function()

ltcM_model = model_definition()
ltcM_model.load_weights("cryptoData/models/ltcM_model.h5")
ltcM_model.make_predict_function()

lunaM_model = model_definition()
lunaM_model.load_weights("cryptoData/models/lunaM_model.h5")
lunaM_model.make_predict_function()

maticM_model = model_definition()
maticM_model.load_weights("cryptoData/models/maticM_model.h5")
maticM_model.make_predict_function()

nearM_model = model_definition()
nearM_model.load_weights("cryptoData/models/nearM_model.h5")
nearM_model.make_predict_function()

solM_model = model_definition()
solM_model.load_weights("cryptoData/models/solM_model.h5")
solM_model.make_predict_function()

uniM_model = model_definition()
uniM_model.load_weights("cryptoData/models/uniM_model.h5")
uniM_model.make_predict_function()

usdcM_model = model_definition()
usdcM_model.load_weights("cryptoData/models/usdcM_model.h5")
usdcM_model.make_predict_function()

def pred_clf_ada():
    loaded_model = pickle.load(open("cryptoData/models/new/ADAUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_atom():
    loaded_model = pickle.load(open("cryptoData/models/new/ATOMUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_avax():
    loaded_model = pickle.load(open("cryptoData/models/new/AVAXUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_bch():
    loaded_model = pickle.load(open("cryptoData/models/new/BCHUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_bnb():
    loaded_model = pickle.load(open("cryptoData/models/new/BNBUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_btc():
    loaded_model = pickle.load(open("cryptoData/models/new/BTCUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_doge():
    loaded_model = pickle.load(open("cryptoData/models/new/DOGEUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_dot():
    loaded_model = pickle.load(open("cryptoData/models/new/DOTUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_etc():
    loaded_model = pickle.load(open("cryptoData/models/new/ETCUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_eth():
    loaded_model = pickle.load(open("cryptoData/models/new/ETHUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_ftt():
    loaded_model = pickle.load(open("cryptoData/models/new/FTTUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_link():
    loaded_model = pickle.load(open("cryptoData/models/new/LINKUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_ltc():
    loaded_model = pickle.load(open("cryptoData/models/new/LTCUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_luna():
    loaded_model = pickle.load(open("cryptoData/models/new/LUNAUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_matic():
    loaded_model = pickle.load(open("cryptoData/models/new/MATICUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_near():
    loaded_model = pickle.load(open("cryptoData/models/new/NEARUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_sol():
    loaded_model = pickle.load(open("cryptoData/models/new/SOLUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_trx():
    loaded_model = pickle.load(open("cryptoData/models/new/TRXUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_uni():
    loaded_model = pickle.load(open("cryptoData/models/new/UNIUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_usdc():
    loaded_model = pickle.load(open("cryptoData/models/new/USDCUSDmc_model.pkl", "rb"))
    return loaded_model
def pred_clf_xrp():
    loaded_model = pickle.load(open("cryptoData/models/new/XRPUSDmc_model.pkl", "rb"))
    return loaded_model

flaskapp = Flask(__name__)

import cryptoData.views
