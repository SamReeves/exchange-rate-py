#!/usr/bin/env python3

# All written by Sam Reeves
# s@mmk.global

from urllib.request import urlopen
import datetime, time, os
import json
import dill
import pandas as pd

os.environ['TZ'] = 'Asia/Rangoon'
time.tzset()
date = datetime.datetime.now().date()
url_base = 'https://forex.cbm.gov.mm/api/history/'

# Load data
with open('rates.pkl', 'rb') as file:
    rates = dill.load(file)


# Return a day's JSON from the CBM website

def getDay(date):
    response = urlopen(url_base + date.strftime('%d-%m-%Y'))
    response = response.read()
    data = json.loads(response)
    data = pd.Series(data['rates'], name=date)
    for i in range(len(data)):
        data.iloc[i] = data.iloc[i].replace(',','')
    return data


# Search the db for records.  If no record is
# found, try to get it from the web.  If it 
# returns empty, append a list of None.

def checkDay(date):
        day = pd.Series(getDay(date), name=date)
        # If the query returns data
        if day.isnull().values.any():
            day = pd.Series([None]*38, name=date)
        return day

#
# DONT FORGET
#
# Range of days defaults to 90!
for i in range(90):
    if date not in rates.index:
        day = checkDay(date)
        rates = rates.append(day)
    date = date - datetime.timedelta(days=1)


rates = rates.sort_index()
first = rates.first_valid_index()
rates = rates.loc[first:]

with open('rates.pkl', 'wb') as f:
    dill.dump(rates, f)