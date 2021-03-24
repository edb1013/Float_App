# Float_App

### Contributors:
Ethan Burrows: Ethandburrows@gmail.com

## Introduction
Float_App is an experimental project with the goal of creating a usefull Windows app for traders. By inserting any ticker into the input boxes one is able to get the public float and shares outstanding as these values allow for a relative understanding of volitality. These values usually differ from source to source so due to this fact Float_App pulls both from MarketWatch and Yahoo finance in order to give the user the ability to compare the returned data.

## Method
### Function Creation:
The first step was to use BeautifulSoup and build webscraping functions that returned our desired values. For Market watch our basic scraping function for public float can be found [here](F&D_marketwatch.py) and our code for the oustanding shares can be found [here](Out_Shares_MW.py). For Yahoo Finance our public float code can be found [here](F&D_yahoo.py) and our outstanding share code can be found [here](Out_Shares_Y.py).

### App Creation:
The use of Tkinter was chosen because Tkinter allows for a wide variety of apps as well as hands on formating. These useful formatting tools allowed for a final product visual to look like this:
![](Figures/image_app(1).PNG)
This look was precisely what we were going for and below is a photo of it with the specified ticker "AAPL" (Apple) and its returned values. 
INSERT IMAGE OF APP WITH TICKER AND VALUES
By comparing the returned values with those produced by the app we are able to conclude that the app works properly. The code for the app can be found [here](Float_app.py).

## Conclusion: 
This was the first time something like this has been attempted. Though I am happy with the result there are obvious improvements to formatting and function that can be done. 
