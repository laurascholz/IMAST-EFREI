#this file is used to find the fault in the second webscraper

import requests
#import json
from bs4 import BeautifulSoup
import csv

URL = "https://www.douglas.de/de/p/3001047857"   #specific product examples
URL = "https://www.douglas.de/de/p/3001048261"
r = requests.get(URL)   
soup = BeautifulSoup(r.content, 'html.parser')
print(soup)

ingr_list = {}  #ingr_list is a tupel with the attributes name and ingredients

#req = soup.find("header", attrs = { "class" : "product-detail-header"})   #gibt nur Productdetails aus, nicht inhaltsstoffe
#print(req)

req = soup.find("div", attrs = { "class" : "second-line"})
ingr_list["name2"] = req.a.text          
#es koennte Probleme geben fuer alle Namen, die aus einem span und einem a Element bestehen, der Name ist dann nicht vollstaendig

#data = requests.get(URL).json()
#print(json.dumps(data))

#req2 = soup.find("div", attrs = { "id" : "react-tabs-3"})
#print(req2)
#ingrs = req2.div.text  
#print(ingr_list)