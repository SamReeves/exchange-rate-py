#!/usr/bin/env python3

# All written by Sam Reeves
# s@mmk.global

from urllib.request import urlopen
import datetime
import json
from os import path
import ast

date = datetime.datetime.now().date()
url_base = 'https://forex.cbm.gov.mm/api/history/'

# Get and save the list of currencies
if path.exists('currencies.dict'):
    currencies = open('currencies.dict', 'r').read()
    currencies = ast.literal_eval(currencies)
else:
    currencies  = urlopen('http://forex.cbm.gov.mm/api/currencies')
    currencies = json.loads(currencies.read())
    currencies = currencies['currencies']
    f = open('currencies.dict', "w")
    f.write(str(currencies))
    f.close()


#%%
# Return a day's json from the CBM website

def getDay(date):
    response = urlopen(url_base + date.strftime('%d-%m-%Y'))
    response = response.read()
    data = json.loads(response)
    data = data['rates']
    return [data]


#%%
# Loop across the set, storing data

for i in range(3650):
    if path.exists(str(date)+'.json') == False:
        day = str(getDay(date))
        if day != '[[]]':
            f = open(str(date)+'.json', "w")
            f.write(str(day))
            f.close()
    date = date - datetime.timedelta(days=1)

