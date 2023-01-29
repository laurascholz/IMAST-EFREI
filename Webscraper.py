#pip install html5lib
#pip install requests
#pip install bs4

import requests
from bs4 import BeautifulSoup
import csv

#Examples for searches:
#https://www.douglas.de/de/search?q=niacinamide     Produktart
#https://www.douglas.de/de/search?q=lipgloss        Produktart
#https://www.douglas.de/de/search?q=boss            Marke
#https://www.douglas.de/de/search?q=the%20ordinary%20more%20modecules%20niacinamide   spezifisches Produkt

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

for row in table.findAll('div', attrs = {'class':'product-tile product-tile--is-pop-tile'}):
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
