#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:11:02 2019
@author: s
"""

import pandas as pd
import numpy as np
import dill
#import sklearn
from sklearn.ensemble import GradientBoostingRegressor
import datetime
import time, os

# Magic numbers.........
os.environ['TZ'] = 'Asia/Rangoon'
time.tzset()
date = datetime.datetime.now().date()

# Load the history
with open('rates.pkl', 'rb') as file:
    rates = dill.load(file)
rates = rates.fillna(method='ffill')

# Set lower and upper quantiles
# To show prediction intervals, we must make 3 separate models

LOWER_ALPHA = 0.1
UPPER_ALPHA = 0.9

lower_model = GradientBoostingRegressor(loss="quantile", alpha=LOWER_ALPHA)
mid_model = GradientBoostingRegressor(loss="ls")
upper_model = GradientBoostingRegressor(loss="quantile", alpha=UPPER_ALPHA)


#%%

def predictN(n=1):
    X = rates[:-n]
    y = rates[n:]
# Train / Test Split
#    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y)

# Linear regression fit with intervals
    lower_model.fit(X, y)
    mid_model.fit(X, y)
    upper_model.fit(X, y)

    predictions = pd.DataFrame(y)
    predictions['lower'] = lower_model.predict(X)
    predictions['mid'] = mid_model.predict(X)
    predictions['upper'] = upper_model.predict(X)

# Predict new values
    new_values = pd.DataFrame()
    new_values['lower'] = lower_model.predict([np.array(rates.iloc[-1])])[0]
    new_values['mid'] = mid_model.predict([np.array(rates.iloc[-1])])[0]
    new_values['upper'] = upper_model.predict([np.array(rates.iloc[-1])])[0]
    
    return new_values