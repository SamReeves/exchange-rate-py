#!/usr/bin/env python3

# All written by Sam Reeves
# s@mmk.global

from urllib.request import urlopen
import datetime
import json
import dill
import pandas as pd

date = datetime.datetime.now().date()
url_base = 'https://forex.cbm.gov.mm/api/history/'

# Load data
with open('rates.pkl', 'rb') as file:
    rates = dill.load(file)


# Return a day's json from the CBM website

def getDay(date):
    response = urlopen(url_base + date.strftime('%d-%m-%Y'))
    response = response.read()
    data = json.loads(response)
    data = data['rates']
    return data


#%%
# Search the db for records.  If no record is
# found, try to get it from the web.  If it 
# returns empty, append a list of None.

def checkDay(date):
    if (date in rates.index):
        return
    else:
        day = getDay(date)
        # If the query returns data
        if str(day) != '[[]]':
            day = pd.Series(day, name=date)
        else:
            day = pd.Series([None]*38, name=date)
        return day

#%%

for i in range(5000):
    day = checkDay(date)
    rates = rates.append(day)
    date = date - datetime.timedelta(days=1)
    
rates.sort_index()

#%%

with open('rates.pkl', 'wb') as f:
    dill.dump(rates, f)