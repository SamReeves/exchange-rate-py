# mmk
kyat prediction with sklearn

    scrape.py

This script scrapes the web for data
concerning currency trading prices 
of the Myanmar Kyat.  Output is rates.pkl,
a Pandas DataFrame with all the information
queried previously.

scrape.py reads the rates.pkl and for every
queried date that hasn't already been 
recorded, it appends a Series with the 
rates for that day.  It then sorts the
DataFrame by the date, and outputs a 
Pickle.

-------------------------------------------------

    train.py
This script runs linear and ridge regression on
the data to produce a prediction for tomorrow.

-------------------------------------------------

    .pkl files
These are python pickle objects.  I
am using Python 3, so these are generated
with the library dill.  db.pkl is a 
pandas DataFrame object.  index.pkl is
a list of dates that correspond to the
rows in db.pkl.  The columns are given
in currencies.pkl.

-------------------------------------------------

    maps.ipynb
This Jupyter Notebook is just for making some
images to put on the website.


