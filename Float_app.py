import requests
import tkinter as tk
import bs4
import requests
from bs4 import BeautifulSoup

HEIGHT = 350
WIDTH = 600

#import stock functions

def format_response_y(response_y):
    return response_y

def Float_func_yahoo(entry_yahoo):
    URL = ('https://finance.yahoo.com/quote/') + entry_yahoo + ('/key-statistics?p=') + entry_yahoo
    r = requests.get(URL)
    soup = bs4.BeautifulSoup(r.text,"lxml")
    #print(soup):result = success
    F_val = soup.find_all('td',{'class':'Fw(500) Ta(end) Pstart(10px) Miw(60px)'})[10].text 
    #Our value for the float is found as the Eighth element in the list 
    response_y = F_val
    Float_label_yahoo['text'] = format_response_y(response_y)

def format_response_yOUT(response_yOUT):
    return response_yOUT

def Out_Shares_yfunc(entry_yahoo):
    URL = ('https://finance.yahoo.com/quote/') + entry_yahoo + ('/key-statistics?p=') + entry_yahoo
    r = requests.get(URL)
    soup = bs4.BeautifulSoup(r.text,"lxml")
    OS_val = soup.find_all('td',{'class':'Fw(500) Ta(end) Pstart(10px) Miw(60px)'})[9].text
    response_yOUT = OS_val
    Out_Shares_ylabel['text'] = format_response_yOUT(response_yOUT)

def format_response_mw(response_mw):
    return response_mw

def Float_func_mw(entry_mw):
    URL = ('https://www.marketwatch.com/investing/stock/') + entry_mw + ('?mod=mw_quote_tab')
    r = requests.get(URL)
    soup = bs4.BeautifulSoup(r.text,"lxml")
    #print(soup):result=success
    F_val = soup.find_all('li',{'class':'kv__item'})[5].find('span').text
    #Our value for the float is found as the Fith element in the list 
    response_mw = F_val
    Float_label_mw['text'] = format_response_mw(response_mw)
    

def format_response_mwOUT(response_mwOUT):
    return response_mwOUT

def Out_Shares_mwfunc(entry_mw):
    URL = ('https://www.marketwatch.com/investing/stock/') + entry_mw + ('?mod=mw_quote_tab')
    r = requests.get(URL)
    soup = bs4.BeautifulSoup(r.text,"lxml")
    #print(soup):result=success
    OS_val = soup.find_all('li',{'class':'kv__item'})[4].find('span').text
    response_mwOUT = OS_val
    Out_Shares_mwlabel['text'] = format_response_mwOUT(response_mwOUT)


root = tk.Tk()

#create canvas
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#set background
background_image = tk.PhotoImage(file='Candlestick.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame_y  = tk.Frame(root, bg='black', bd=5)
frame_y.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
frame_mw = tk.Frame(root, bg='black', bd=5)
frame_mw.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.1, anchor='n')

#lower frame
lf_y = tk.Frame(root,bg='black', bd=5)
lf_y.place(relx=0.5, rely=0.23, relwidth=0.75, relheight=0.2, anchor='n')
lf_mw = tk.Frame(root,bg='black', bd=5)
lf_mw.place(relx=0.5, rely=0.63, relwidth=0.75, relheight=0.2, anchor='n')

#add a button
button_yahoo = tk.Button(frame_y, text='Yahoo Float', bg='#ffffff', fg='black', relief ='raised',command=lambda:[Float_func_yahoo(entry_yahoo.get()), Out_Shares_yfunc(entry_yahoo.get())])
button_mw = tk.Button(frame_mw, text = 'Market Watch Float', bg ='#ffffff', fg = 'black', relief = 'raised', command=lambda:[Float_func_mw(entry_mw.get()), Out_Shares_mwfunc(entry_mw.get())])
button_yahoo.place(relx=0.7, relwidth=0.3, relheight=1)
button_mw.place(relx=0.7, relwidth=0.3, relheight=1)

#add a label and place them
Float_label_yahoo = tk.Label(lf_y, text = 'Public Float from Yahoo Finance', bg = '#ffffff')
Out_Shares_ylabel = tk.Label(lf_y, text = 'Outstanding Shares from Yahoo Finance', bg = '#ffffff')
yratio_label = tk.Label(lf_y, text = 'Volatility can be be infered: Public/Outstanding', bg = '#ffffff')

Float_label_yahoo.place(relx=0.5, rely=0.02, relwidth=0.75, relheight=0.25, anchor='n')
Out_Shares_ylabel.place(relx=0.5, rely=0.39, relwidth=0.75, relheight=0.25, anchor='n')
yratio_label.place(relx=0.5, rely=0.75, relwidth=0.75, relheight=0.25, anchor='n')

Float_label_mw = tk.Label(lf_mw, text = 'Public Float from Market Watch', bg = '#ffffff')
Out_Shares_mwlabel = tk.Label(lf_mw, text = 'Outstanding Shares from Market Watch')
mwratio_label = tk.Label(lf_mw, text = 'Volatility can be be infered: Public/Outstanding', bg = '#ffffff')

Float_label_mw.place(relx=0.5, rely=0.02, relwidth=0.75, relheight=0.25, anchor='n')
Out_Shares_mwlabel.place(relx=0.5, rely=0.39, relwidth=0.75, relheight=0.25, anchor='n')
mwratio_label.place(relx=0.5, rely=0.75, relwidth=0.75, relheight=0.25, anchor='n')

#add an entry for each label
entry_yahoo = tk.Entry(frame_y, bg = '#ffffff', font=40)
entry_mw = tk.Entry(frame_mw, bg = '#ffffff', font=40)
entry_yahoo.place(relwidth=0.65, relheight=1)
entry_mw.place(relwidth=0.65, relheight=1)


root.mainloop()
