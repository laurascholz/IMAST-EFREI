#  -------------------------- necessary packets and imports for vs code----------------------------
#pip install html5lib
#pip install requests
#pip install bs4
#pip install selenium
#py -m venv env

import requests
from bs4 import BeautifulSoup
import csv
#import pandas as pd
from selenium import webdriver


#Examples for searches:
#https://www.douglas.de/de/search?q=niacinamide     Produktart
#https://www.douglas.de/de/search?q=lipgloss        Produktart
#https://www.douglas.de/de/search?q=boss            Marke
#https://www.douglas.de/de/search?q=the%20ordinary%20more%20modecules%20niacinamide   spezifisches Produkt


# ------------------------starting the webscraper search -------------------------------------


#search = "the%20ordinary%20more%20modecules%20niacinamide"               #hier spaeter Eingabe entgegen nehmen
search = "Makeup"
URL = "https://www.douglas.de/de/search?q=" + search        #Searchstring is formed for Douglas Website

r = requests.get(URL)               #html request to the url

#html5lib ist der parser, der am meisten fehlende komponenten bei falschem html ergaenzt, aber html.parser funktioniert auch
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

products=[]  # a list to store products

#all product results of the search are saved in table
table = soup.find("div", attrs= {"class": "product-grid cms-component cms-component__margin cms-component__margin--default"})  

# ------------------saving of wanted information in a csv file -------------------------------------------------------

for row in table.findAll("div", attrs = {"class":'product-tile product-tile--is-pop-tile'}):   #all product info is saved in this class
    product = {}                 #product is a tupel and stores several elements of the scraped website
    product['name'] = row.find('div', attrs = {'class' : 'text name'}).text
    product['brand'] = row.find('div', attrs = {'class' : 'text top-brand'}).text
    product['category'] = row.find('div', attrs = {'class' : 'text category'}).text
    #check, whether there is a discount price, if yes, it will be saved as the products price
    price_var = {}
    price_var = row.find_all('span', attrs = {'class' : 'product-price__price'})
    if len(price_var) == 2:
        product['price'] = price_var[1].text
    else: product['price'] = price_var[0].text
    product['link'] = row.a['href']       # together with https://www.douglas.de the link leads to the product
    product['img'] = row.img['src']  
    products.append(product)              #the product is now part of the product list

filename = 'products.csv'           #products stores the scraped information except for the ingredients
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['name','brand','category','price','link','img'])
    w.writeheader()
    for product in products:
        w.writerow(product)


# ---------------------getting the ingredients with the prior saved link ------------------------------------------------


driver = webdriver.Firefox()  #executable_path= "C:\Users\laura\OneDrive\Dokumente\GitHub\IMAST-EFREI\ " ) #geckodriver.exe

for product in products:                #die gespeicherten Links werden von der forschleife zu richigen links ergaenzt
    URL = "https://www.douglas.de"
    newUrl = URL + product['link']
    #with newUrl search for ingredients

    #first try: selenium
    r2 = driver.get(newUrl)
    content = driver.page_source
    soup2 = BeautifulSoup(content, "html5lib")
    
    #second try beautyfulSoup
    #r = requests.get(newUrl)
    #soup2 = BeautifulSoup(r.content, 'html5lib')


    ingr_list = {}  #ingr_list is a tupel with the attributes name and ingredients
    req = soup2.find("div", attrs = { "class" : "second-line"})
    print(req)
    if req.find("span"):
        ingr_list["name2"] = req.span.text
    else: ingr_list["name2"] = req.a.text
    print(ingr_list)


