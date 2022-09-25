#implement by Mostafa Mahmoud salah
import requests
from bs4 import BeautifulSoup
from tkinter import *
import tkinter as tk

window = Tk()
window.title("Currency Converter")

convert = "TRY"
to_convert = "EUR"
amount = 1
Tops = Frame(window,bg = '#3cb371',pady = 2, width =1850, height = 100, relief = "ridge")
Tops.grid(row=0,column=0)
headlabel = tk.Label(Tops,font=('lato #3cb371', 19,'bold'), bg= '#3cb371', fg='WHITE') 
headlabel.grid(row=1, column=0,sticky=W)

window.configure(background = '#3cb371') 
window.geometry("700x400") 


def list_of_curreny_names():
    currency_list_url = f"https://www.x-rates.com/calculator/?from={convert}&to={to_convert}&amount={1}"
    currency_list = requests.get(currency_list_url).text
    currency_list_page = BeautifulSoup(currency_list,"html.parser")

    currencies = currency_list_page.find_all(class_="currencyList currencycalculator")
    short_name = []
    currency_name = ""

    for currency in currencies:
        currency_name += currency.text
        curreny_symbols= currency.find_all('a')
        for symbol in curreny_symbols:
            symbol_text = symbol.get("href")
            short_name.append(symbol_text.split("=")[1])
    currency_name_list = currency_name.split("\n")

    full_list = []
    for i, x in zip(short_name, currency_name_list):
        full_list.append(f"{i} - {x}")

    return full_list

short_name = list_of_curreny_names()
short_name.sort()

def generate(amount):
        result = am.get(1.0,"end")
        url = f"https://www.x-rates.com/calculator/?from={var1.get()[:3]}&to={var2.get()[:3]}&amount={int(result)}"
        results = requests.get(url).text
        page = BeautifulSoup(results, "html.parser")
        prices = page.find_all(class_="ccOutputRslt")
        for price in prices:
            price_text= price.text
            print(price.text)
        l3.config(text=price_text)
        price_text = price_text.split(" ")[0].replace(",", "")
        price_text = str(round(float(price_text)/int(result),4))
        l4.config(text=price_text)
        print(round(float(price_text)/int(result),4))


convert = Label(text=" Convert from : ",height=5,width=10 , bg="#3cb371",fg ="WHITE")
convert.grid(row=0,column=0)
var1 = StringVar()
OptionMenu(window,var1,*short_name).grid(row=0,column=1)
to_convert = Label(text=" Convert to : ",height=5,width=10 ,bg="#3cb371",fg ="WHITE").grid(row=1,column=0)
var2 = StringVar()
OptionMenu(window,var2,*short_name).grid(row=1,column=1)
am = Text(window,height=1,width=10,bg="#3cb371",fg ="WHITE")
am.grid(row=2,column=1)
Label(text="Amount" ,bg="#3cb371",fg ="WHITE").grid(row=2,column=0)
b3 = Button(text="Generate" ,bg="#3cb371",fg ="WHITE",command=lambda: generate(2)).grid(row=4,column=0)
l3 = Label(text="",width= 20,height=3 ,bg="#3cb371",fg ="WHITE")
l3.grid(row=5,column=0)
Label(text="Unit Price", bg="#3cb371",fg ="WHITE").grid(row=3,column=1)
l4 = Label(text="",width=20,height=3 ,bg="#3cb371",fg ="WHITE")
l4.grid(row=5,column=1)

window.mainloop()
