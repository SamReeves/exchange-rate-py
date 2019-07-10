# mmk
kyat prediction with sklearn


	scrape.py
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

    .pkl files
These are python pickle objects.  I
am using Python 3, so these are generated
with the library dill.  db.pkl is a 
pandas DataFrame object.  index.pkl is
a list of dates that correspond to the
rows in db.pkl.  The columns are given
in currencies.pkl.
