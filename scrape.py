#!/usr/bin/env python3

# All written by Sam Reeves
# s@mmk.global



import time
from urllib.request import urlopen
import datetime
import pandas as pd
import json
from os import path
import ast

date = pd.to_datetime('today')
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


# Local data   [ [date, dump], [], ... ]
local_data = []
null_count = 0

#%%
# Loop across the set, storing data

while null_count <= 100:
    day = {date : getDay(date)}
    local_data.insert(0, day)
    date = date - datetime.timedelta(days=1)
    
    if local_data[1] and local_data[0] == []:
        null_count +=1
        
    else:
        null_count = 0
    time.sleep(3)

#%%
# Write out the data
    
