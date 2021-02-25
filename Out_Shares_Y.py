#set up
import bs4
import requests
from bs4 import BeautifulSoup

def Out_Shares_yfunc(TICKER):
    URL = ('https://finance.yahoo.com/quote/') + TICKER + ('/key-statistics?p=') + TICKER
    r = requests.get(URL)
    soup = bs4.BeautifulSoup(r.text,"lxml")
    OS_val = soup.find_all('td',{'class':'Fw(500) Ta(end) Pstart(10px) Miw(60px)'})[9].text
    return(OS_val)

Out_Shares_EST = Out_Shares_yfunc('GME') #any ticker can be inserted here to retrieve the data
print('Outstanding Shares:' + Out_Shares_EST)
