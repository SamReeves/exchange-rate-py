#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:11:02 2019
@author: s
"""

import pandas as pd
import dill
import sklearn
from sklearn.ensemble import GradientBoostingRegressor
import datetime
import time, os

# Magic numbers.........

os.environ['TZ'] = 'Asia/Rangoon'
time.tzset()
date = datetime.datetime.now().date()

# Set lower and upper quantiles
# To show prediction intervals, we must make 3 separate models

LOWER_ALPHA = 0.1
UPPER_ALPHA = 0.9

lower_model = GradientBoostingRegressor(loss="quantile", alpha=LOWER_ALPHA)
mid_model = GradientBoostingRegressor(loss="ls")
upper_model = GradientBoostingRegressor(loss="quantile", alpha=UPPER_ALPHA)

# Load the history
with open('rates.pkl', 'rb') as file:
    rates = dill.load(file)
rates = rates.fillna(method='ffill')
#%%

def predictN(n):
    X = rates[:-n]
    y = rates[n:]
# Train / Test Split
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y)

# Linear regression with intervals
    lower_model.fit(X_train, y_train)
    mid_model.fit(X_train, y_train)
    upper_model.fit(X_train, y_train)

    predictions = pd.DataFrame(y_test)
    predictions['lower'] = lower_model.predict(X_test)
    predictions['mid'] = mid_model.predict(X_test)
    predictions['upper'] = upper_model.predict(X_test)

