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

#ueber die beste Ordnung fuer den Tupel nachdenken
#klappen mehr als 8 ergebnisse mit was anderem als row?

# ------------------saving of wanted information in a csv file -------------------------------------------------------

for row in table.findAll("div", attrs = {"class":'product-tile product-tile--is-pop-tile'}):
    product = {}          #product is a tupel and stores several elements for the website
    product['name'] = row.find('div', attrs = {'class' : 'text name'})
    product['brand'] = row.find('div', attrs = {'class' : 'text top-brand'})
    product['category'] = row.find('div', attrs = {'class' : 'text category'})
    #zur Zeit: gibt beide Preise zusammen aus, erst den ohne, dann mit Rabatt
    product['price'] = row.find_all('span', attrs = {'class' : 'product-price__price'})  #aufpassen bei discount vs nicht discount
    #product['price-discount'] = row.find('span', attrs = {'class' : 'product-price__price'}) -> keine Ahnung, wie ich daran komme, hat denselben Namen wie der normale Preis
    product['link'] = row.a['href']       # in Verbindung mit https://www.douglas.de ergibt sich der volle Link
    product['img'] = row.img['src']  
    #print(product)
    products.append(product)              #the product is now part of the product list

filename = 'products.csv'
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
    if req.find("a"):
        ingr_list["name2"] = req.a.text
    else: ingr_list["name2"] = req.span.text
    #hier eine if schleife fuer span oder a oder exceptions schreiben
    #ingr_list["name2"] = req.find("span", attrs = {"header-name"}).text   #funktioniert nicht, da entweder a oder span verwendet wird
    print(ingr_list)
         
