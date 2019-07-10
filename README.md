# mmk
kyat prediction with sklearn

-------------------------------------------------

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

	scrape.py *DEPRICATED*
This script scrapes the web for data
concerning currency trading prices 
of the Myanmar Kyat.  Output is a 
.json file for each day.  It also
makes a separate file with the
list of currencies.

It is set to get the last ten years
of data, skipping requests if a record 
already exists.  It can be modified to
search for a different number of days,
however, it does not return a file if
there is no data on that day.  As
the dataset goes back in time, it 
becomes more sparse.



