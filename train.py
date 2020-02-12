#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# All written by Sam Reeves
# s@mmk.global

import os
import datetime
import time

import pandas as pd
import numpy as np
import dill

import sklearn.model_selection
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge


os.environ['TZ'] = 'Asia/Rangoon'
time.tzset()
date = datetime.datetime.now().date()

with open('rates.pkl', 'rb') as file:
    rates = dill.load(file)
rates = rates.fillna(method='ffill')

#%%

def splitData(interval):
    X = rates[:-interval]
    y = rates[-interval:]

    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
        X, y, test_size=0.15, random_state=42)

    return X_train, X_test, y_train, y_test
#%%
    
def trainModels(X_train, X_test, y_train, y_test):
# Linear Regression
    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)
    lin_try = lin_reg.predict(X_test)

# Ridge Regression
    ridge_reg = Ridge()
    ridge_reg.fit(X_train, y_train)
    ridge_try = ridge_reg.predict(X_test)
    
    return lin_reg, ridge_reg, lin_try, ridge_try

#%%

def scoreModels(lin_reg, ridge_reg, lin_try, ridge_try, y_test):
    lin_score = lin_reg.score(y_test, lin_try)
    ridge_score = ridge_reg.score(y_test, ridge_try)
    
    return lin_score, ridge_score


#%%
# Predict the nth day
def predictInterval(interval):
    
    # Split the data
    X_train, X_test, y_train, y_test = splitData(interval)
    
    # Train the model
    lin_reg, ridge_reg, lin_try, ridge_try = trainModels(X_train, X_test, y_train, y_test)
    
    # Score the model
    lin_score, ridge_score = scoreModels(lin_reg, ridge_reg, lin_try, ridge_try, y_test)
    
    # Predict a new set of values
    linear_day = lin_reg.predict([np.array(rates.iloc[-1])])[0]
    ridge_day = ridge_reg.predict([np.array(rates.iloc[-1])])[0]
    
    # Convert the new data 
    linear_series = pd.Series(linear_day, name = date + datetime.timedelta(days = interval), index = rates.columns)
    ridge_series = pd.Series(ridge_day, name = date + datetime.timedelta(days = interval), index = rates.columns)
    
    return linear_series, ridge_series, lin_score, ridge_score
                
