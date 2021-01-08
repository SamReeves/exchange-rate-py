## What it does

This software predicts exchange rates for currencies traded with the Myanmar currency.  It can predict the numbers for an arbitrary number of days ahead of today's date.

## How it works

scrape.py is a basic web scraper written with urllib.  It checks its own database to look for missing data points and makes requests for json data to the [Central Bank of Myanmar](https://forex.cbm.gov.mm/api/).  At this point the information is stored in a [Pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) object and preserved with [dill](https://pypi.org/project/dill/).

`
        /* latest.json */ 
        { 
            "info":"Central Bank of Myanmar", 
            "description":"Official Website of Central Bank of Myanmar", 
            "timestamp":"1337936081", 
            "rates":{ 
                "USD":"840", 
                "CHF":"1319", 
                "BDT":"298", 
                "SGD":"632", 
                "JPY":"1053", 
                "GBP":"887", 
                "AUD":"759" 
                } 
            } 
`

train.py is what actually does the work.  This is another basic script which leverages [scikit-learn](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model) to split the data into training and test sets, and perform two types of regression.

The output is a Series containing a value for each currency, and a value from the built in scoring algorithm:

`
(AUD    1021.400811 
 BDT      15.509807 
 BND     993.011276 
 BRL     240.891111 
 CAD    1034.650289 
 CHF    1483.695501 
 CNY     203.254209 
 CZK      61.401019 
 DKK     216.245798 
 EGP      82.642884 
 EUR    1607.902320 
 GBP    1784.693489 
 HKD     169.673784 
 IDR       9.378252 
 ILS     413.166338 
 INR      17.888415 
 JPY    1266.167182 
 KES      11.983156 
 KHR      32.349740 
 KRW     120.418397 
 KWD    4330.418691 
 LAK      14.127408 
 LKR       6.987411 
 MYR     325.440774 
 NOK     155.357921 
 NPR      11.182759 
 NZD     953.636890 
 PHP      27.325443 
 PKR       8.179218 
 RSD      13.668619 
 RUB      17.477950 
 SAR     350.878164 
 SEK     159.726628 
 SGD     992.388348 
 THB      43.819647 
 USD    1315.549711 
 VND       5.699854 
 ZAR      85.427552 
 Name: 2021-01-09, dtype: float64, 
 AUD    1021.207824 
 BDT      15.506914 
 BND     992.852299 
 BRL     240.785755 
 CAD    1034.454065 
 CHF    1483.456005 
 CNY     203.217238 
 CZK      61.389330 
 DKK     216.210808 
 EGP      82.619088 
 EUR    1607.613321 
 GBP    1784.326200 
 HKD     169.646598 
 IDR       9.377763 
 ILS     413.104220 
 INR      17.884734 
 JPY    1265.929927 
 KES      11.980097 
 KHR      32.343927 
 KRW     120.397998 
 KWD    4329.665369 
 LAK      14.124445 
 LKR       6.990980 
 MYR     325.374435 
 NOK     155.321094 
 NPR      11.180274 
 NZD     953.438896 
 PHP      27.319474 
 PKR       8.177241 
 RSD      13.669672 
 RUB      17.472617 
 SAR     350.821706 
 SEK     159.689671 
 SGD     992.211613 
 THB      43.813536 
 USD    1315.334640 
 VND       5.699392 
 ZAR      85.408343 
 Name: 2021-01-09, dtype: float64, 
 0.9981319096033762, 
 0.9981984205553264) 
`

## About the developer

All code in this project is provided free for the public by Samuel Reeves.  You can view the repository with the link at the top of the page.  Sam holds a Bachelor's degree from Hampshire College and at the time of this post is studying a Master's degree in Data Science at CUNY.  He studied at the Data Incubator in San Francisco in 2019.

If you would like to get in touch, you can contact him at samtreeves@gmail.com.
