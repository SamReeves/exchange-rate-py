#!/usr/bin/env python3

import time
import requests
import datetime
import pandas as pd
import dill

# Define some useful variables. It appears that the db
# starts in 2018.
url_base = 'https://forex.cbm.gov/mm/api/history/'
currencies = 'http://forex.cbm.gov.mm/api/currencies'
date = pd.to_datetime('today')

# Return a day's json from the CBM website
def getDay(date):
    response = requests.get(url_base + date.strftime('%d-%m-%Y'))
    if response.content is None:
        return [date, None]
    else:
        web_content = response.content
        json_str = web_content.decode()
        return [date, json_str]

# Local data   [ { date : json_str }, {}, ...]
local_data = []
null_count = 0

# Loop across the set, storing data
while null_count <= 100:
    local_data.insert(0, getDay(date))
    date = date - datetime.timedelta(days=1)
    if (local_data[1][1] and local_data[0][1]) == None:
        null_count +=1
    else:
        null_count = 0
    time.sleep(3)

# Write out the data
dill.dump(local_data, open('local_data.p', "w"))
