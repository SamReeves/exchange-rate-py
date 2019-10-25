#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# All written by Sam Reeves
# s@mmk.global
import pandas as pd
import numpy as np
import dill
import sklearn.model_selection
import datetime
import time, os

os.environ['TZ'] = 'Asia/Rangoon'
time.tzset()
date = datetime.datetime.now().date()

with open('rates.pkl', 'rb') as file:
    rates = dill.load(file)
rates = rates.fillna(method='ffill')

def predictN(n):
    X = rates[:-n]
    y = rates[n:]

# Train / Test Split
# X, y
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y)

# Train Linear Regression
    from sklearn.linear_model import LinearRegression
    reg = LinearRegression().fit(X,y)

# Train Ridge Regression
    #from sklearn.linear_model import Ridge
    #ridge = Ridge().fit(X,y)
     
# Scoring the algorithms
    print(reg.score(X,y))
    #print(ridge.score(X,y))


# Predict the nth day
    nth_day = reg.predict([np.array(rates.iloc[-1])])[0]
    return pd.Series(nth_day, name=date+datetime.timedelta(days=n), index=rates.columns)