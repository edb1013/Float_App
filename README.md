# Float_App

### Contributors:
Ethan Burrows: Ethandburrows@gmail.com

## Introduction
Float_App is an experimental project with the goal of creating a usefull Windows app for traders. By inserting any ticker into the input boxes one is able to get the public float and shares outstanding as these values allow for a relative understanding of volitality. These values usually differ from source to source so due to this fact Float_App pulls both from MarketWatch and Yahoo finance in order to give the user the ability to compare the returned data.

## Method
### Function Creation:
The first step was to use BeautifulSoup and build webscraping functions that returned our desired values. For Market watch our basic scraping function for public float can be found [here](F&D_marketwatch.py) and our code for the oustanding shares can be found [here](Out_Shares_MW.py). For Yahoo Finance our public float code can be found [here](F&D_yahoo.py) and our outstanding share code can be found [here](Out_Shares_Yahoo.py)
