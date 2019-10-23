# mmk
kyat prediction with sklearn

------------------------------------------------
    scrape3.py
An updated scraper that makes API calls to 
fixer.io and exports csv data to our DB.
Still in development.

------------------------------------------------

    scrape2.py
This This script scrapes the web for data
concerning currency trading prices 
of the Myanmar Kyat.  Output is rates.pkl,
a Pandas DataFrame with all the information
queried previously.

scrape2 reads the rates.pkl and for every
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

-------------------------------------------------

    clean.py *DEPRICATED* (see scrape2.py)
This script loads in all the files created by
scrape.py and cleans the data before outputting
a .pkl file with the rates.  This became the 
jumping-off point for rewriting the initial
scraper with these functionalities.

-------------------------------------------------

	scrape.py *DEPRICATED* (see scrape2.py)
This script scrapes the web for data concerning 
currency trading prices of the Myanmar Kyat.
Output is a .json file for each day.  NOTE: this
can easily be converted to JSON format, but it 
really isn't JSON.  It also makes a separate file
currencies.pkl with the list of currencies.

It is set to get the last ten years
of data, skipping requests if a record 
already exists.  It can be modified to
search for a different number of days,
however, it does not return a file if
there is no data on that day.  As
the dataset goes back in time, it 
becomes more sparse.



