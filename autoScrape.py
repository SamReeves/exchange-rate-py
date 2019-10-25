#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 10:56:40 2019
@author: Thomas Lionel Evans
"""

import time
import pandas
import os
import urllib
import datetime


# Define the web address and the date of first entry
today = datetime.today().strftime('%d-%m-%Y')
url_base = 'http://forex.cbm.gov.mm/api/history/'
db_start = pandas.to_datetime(today, format='%d-%m-%Y')

end_date = pandas.to_datetime(today)
total_days = (end_date - db_start).days

# Load the root directory into a variable for later use.
main_path = os.getcwd()

# Scrape every page of the domain, waiting 3 seconds between
# pages.


for day in range(0, total_days + 1):
    date = db_start + datetime.timedelta(days=day)
    date_str = date.strftime('%d-%m-%Y')
    title = date.strftime('%Y.%m.%d')

    time.sleep(3)
    response = urllib.request.urlopen(url_base + date_str)
    os.chdir(main_path)
    web_content = response.read()
    html_str = web_content.decode()

# Check to see if data_store folder has been created - if not, create it.
    data_path = 'data_store'
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    os.chdir(data_path)
    
# Simple loop to add some level of user-friendliness to the program.
    with open(title + '.json', "w") as entry:
        file_path = entry
        print(html_str, file=entry)
        if os.path.exists(title + '.json'):
            print('Scraped file saved to', title, ".json")
        else:
            print('Could not find scraped files.')
            print('Exiting program')
            break