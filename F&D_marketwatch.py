#set up
import bs4
import requests
from bs4 import BeautifulSoup


#Below is a function built to determine the float of any stock on Market Watch
def Float_func(TICKER):
    URL = ('https://www.marketwatch.com/investing/stock/') + TICKER + ('?mod=mw_quote_tab')
    r = requests.get(URL)
    soup = bs4.BeautifulSoup(r.text,"lxml")
    #print(soup):result=success
    F_val = soup.find_all('li',{'class':'kv__item'})[5].find('span').text
    #Our value for the float is found as the Fith element in the list 
    return(F_val)

Float_EST = Float_func('TSLA') #any ticker can be inserted here to retrieve the data
print('Public Float:' + Float_EST)