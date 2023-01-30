#this file is used to find the fault in the second webscraper

import requests
#import json
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

#URL = "https://www.douglas.de/de/p/3001047857"   #specific product examples
#URL = "https://www.douglas.de/de/p/3001048261"
#r = requests.get(URL)   
#soup = BeautifulSoup(r.content, 'html.parser')
#print(soup)

#ingr_list = {}  #ingr_list is a tupel with the attributes name and ingredients

#req = soup.find("header", attrs = { "class" : "product-detail-header"})   #gibt nur Productdetails aus, nicht inhaltsstoffe
#print(req)

#data = requests.get(URL).json()
#print(json.dumps(data))

#req2 = soup.find("div", attrs = { "id" : "react-tabs-3"})
#print(req2)
#ingrs = req2.div.text  
#print(ingr_list)

driver = webdriver.Firefox()
newUrl = "https://www.douglas.de/de/p/5010004098?variant=037189"

#first try: selenium  -> nur verwenden, wenn es fuer den xpath der ingredients zwingend notwendig ist
r2 = driver.get(newUrl)
content = driver.page_source
soup2 = BeautifulSoup(content, "html5lib")

#second try beautyfulSoup
#r = requests.get(newUrl)
#soup2 = BeautifulSoup(r.content, 'html5lib')


ingr_list = {}  #ingr_list is a tupel with the attributes name and ingredients
req = soup2.find("div", attrs = { "class" : "second-line"})
#print(req)
if req.find("span"):
    ingr_list["name2"] = req.span.text
else: ingr_list["name2"] = req.a.text
print(ingr_list)
#driver.click

#driver.click()
menu = driver.find_element(by = By.XPATH, value ='//*[@id="react-tabs-4"]')
driver.click(menu)
#print(ingredients)