#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# All written by Sam Reeves
# s@mmk.global

import dill
import sklearn.model_selection
with open('rates.pkl', 'rb') as file:
    rates = dill.load(file)
import numpy as np

    
rates = rates.fillna(method='ffill')
        
X = rates[:-1]
y = rates[1:]

#%%

# Train / Test Split
# X, y

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y)

#%%

# Linear Regression

from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit(X,y)



#%%
    
# Ridge Regression
from sklearn.linear_model import Ridge
ridge = Ridge().fit(X,y)
    
#%%
    
# Scoring the algorithms

print(reg.score(X,y))
print(ridge.score(X,y))

#%%

# Predict tomorrow
tomorrow = reg.predict([np.array(rates.iloc[-1])])[0]
tomorrow = pd.Series(tomorrow, index = rates.columns, name = datetime.datetime.now().date())

with open('pastPredictions.pkl', 'rb') as f:
    past = dill.load(f)
past.loc[tomorrow.name] = tomorrow