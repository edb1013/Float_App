import bs4
import requests
from bs4 import BeautifulSoup

def Out_Shares_mwfunc(TICKER):
    URL = ('https://www.marketwatch.com/investing/stock/gme')
    r = requests.get(URL)
    soup = bs4.BeautifulSoup(r.text,"lxml")
    #print(soup):result=success
    OS_val = soup.find_all('li',{'class':'kv__item'})[4].find('span').text
    return(OS_val)

Out_Shares_EST = Out_Shares_mwfunc('GME') #any ticker can be inserted here to retrieve the data
print('Outstanding Shares:' + Out_Shares_EST)