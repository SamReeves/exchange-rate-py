#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 06:10:59 2019

@author: s
"""

import requests
import pendulum
import json

# Magic numbers......

API_KEY = "?access_key=7729b3a8af2ca6efe3ff51ebe767c2af"
URL = "http://data.fixer.io/api/"
TODAY = pendulum.today()
TODAY = TODAY.strftime('%Y-%m-%d')

#%%

### Available Fixer.io endpoints:
# latest -- gives all latest rates
# convert -- from = GBP, to = JPY
# historical -- date as endpoint string
# timeseries -- start_date, end_date = YYYY-MM-DD
# fluctuation -- start_date, end_date = YYYY-MM-DD

def grabData(parameters):
    response = requests.get(parameters)
    content = response.content
    return content

def getLatest(base):
    parameters = str(URL + "latest" + API_KEY)
    return grabData(parameters)

def getHist(date=TODAY, base="mmk"):
    parameters = str(URL + date + API_KEY + "&" + base)
    return grabData(parameters)

def getTS(start="2012-01-01", end=TODAY, base="mmk"):
    parameters = str(URL + "timeseries" + API_KEY + "&" + start + "&" + end)
    return grabData(parameters)

#%%
