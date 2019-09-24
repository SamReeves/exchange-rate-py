#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 06:10:59 2019

@author: s
"""

import requests
import datetime


API_KEY = "7729b3a8af2ca6efe3ff51ebe767c2af"
URL = "http://data.fixer.io/api/"

DATE = datetime.date.today()
DATE = DATE.strftime('%Y-%m-%d')

BASE = "MMK"

parameters = {
        "url" : "http://data.fixer.io/api/",
        "access_key" : API_KEY,
        "base" : BASE }
