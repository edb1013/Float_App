#set up
import bs4
import requests
from bs4 import BeautifulSoup


#Below is a function built to determine the float of any stock on Yahoo Finance

def Float_func_yahoo(TICKER):
    URL = ('https://finance.yahoo.com/quote/') + TICKER + ('/key-statistics?p=') + TICKER
    r = requests.get(URL)
    soup = bs4.BeautifulSoup(r.text,"lxml")
    #print(soup):result = success
    F_val = soup.find_all('td',{'class':'Fw(500) Ta(end) Pstart(10px) Miw(60px)'})[10].text 
    #Our value for the float is found as the Eighth element in the list 
    return (F_val)

Float_EST = Float_func_yahoo('GME') #any ticker can be inserted here to retrieve the data
print('Public Float:' + Float_EST )


