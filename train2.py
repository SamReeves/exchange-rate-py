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
n = 1

# Load the history
with open('rates.pkl', 'rb') as file:
    rates = dill.load(file)
rates = rates.fillna(method='ffill')

X = np.array(rates[:-n])[0].reshape(-1,1)
y = np.array(rates[n:])[0]
    
# Train / Test Split
#    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y)

# Set lower and upper quantiles
# To show prediction intervals, we must make 3 separate models
LOWER_ALPHA = 0.2
UPPER_ALPHA = 0.8

lower_model = GradientBoostingRegressor(loss="quantile", alpha=LOWER_ALPHA).fit(X,y)
mid_model = GradientBoostingRegressor(loss="ls").fit(X,y)
upper_model = GradientBoostingRegressor(loss="quantile", alpha=UPPER_ALPHA).fit(X,y)

predictions = pd.DataFrame(y)
predictions['lower'] = lower_model.predict(X)
predictions['mid'] = mid_model.predict(X)
predictions['upper'] = upper_model.predict(X)
