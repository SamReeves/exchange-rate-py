#!/usr/bin/env python3

# All written by Sam Reeves
# s@mmk.global

import os
import datetime
import ast
import pandas as pd
import numpy as np
import dill


db = []

# Read in the files
for filename in os.listdir(os.getcwd()):
    date = datetime.datetime.strptime(os.path.splitext(filename)[0], '%Y-%m-%d')
    date = date.date()
    
    f = open(filename, "r")
    content = f.read()
    content.strip("[]")
    content = pd.DataFrame(ast.literal_eval(content))
    db.append((date, content))
    
    
#%%

# Create a clean dataframe with index and column names
db = sorted(db)
currencies = list(db[0][1].keys())
index = []
rates = []

for item in db:
    index.append(item[0])
    day = np.ndarray.tolist(item[1].values)
    for i in day:
        rates.append(i)
    
df = pd.DataFrame(rates, index= index, columns= currencies)
#%%


# Write out the data
df.to_pickle("db.pkl")

with open('index.pkl', 'wb') as f:
    dill.dump(index, f)
    
with open('currencies.pkl', 'wb') as f:
    dill.dump(currencies, f)