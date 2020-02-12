#!/usr/bin/env python3

# All written by Sam Reeves
# samtreeves@gmail.com

from urllib.request import urlopen
import datetime
import time
import os
import json
import dill
import pandas as pd

url_base = 'https://forex.cbm.gov.mm/api/history/'

def setTZandDate():
    os.environ['TZ'] = 'Asia/Rangoon'
    time.tzset()
    date = datetime.datetime.now().date()
    return date


# Load data from Python3 dill
def loadArchive():
    with open('rates.pkl', 'rb') as file:
        rates = dill.load(file)
    return rates


# Check archive for records.  If no record exists, try to get it from the web.
# If it returns empty, append a list of None.
def checkArchive(date):
    day = pd.Series(downloadData(date), name=date)
    if day.isnull().values.any():
        day = pd.Series([None]*38, name=date)
    return day


# Return a day's JSON from the CBM website.
def downloadData(date, url_base):
    response = urlopen(url_base + date.strftime('%d-%m-%Y'))
    response = response.read()
    
    data = json.loads(response)
    data = pd.Series(data['rates'], name=date)
    
    for i in range(len(data)):
        data.iloc[i] = data.iloc[i].replace(',', '')
    return data

# Ouput any new information scraped from the web.
def updateArchive(span=365):
    date = setTZandDate()
    rates = loadArchive()
    
    for i in range(span):
        if date not in rates.index:
            day = checkArchive(date)
            rates = rates.append(day)
            date = date - datetime.timedelta(days=1)

    rates = rates.sort_index()
    first = rates.first_valid_index()
    rates = rates.loc[first:]

    with open('rates.pkl', 'wb') as f:
        dill.dump(rates, f)
    return

# Test to see if the archive matches the info from the web.
def reconcileArchive():
    return
    
