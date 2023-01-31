#this file is used to find the fault in the second webscraper

import requests
#import json
from bs4 import BeautifulSoup
import csv
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
newUrl = "https://www.douglas.de/de/p/5009310047?variant=1077417"

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

#ideen:
# -alle reacts durchklicken und ueberpruefen, ob es Inhaltsstoffe findet = erfuellt wenn der text = inhaltsstoffe ist


#alle mit der klasse anklickwn, wenn der text inhalt ist, dann den xpath nehmen
#menu = ""

#while menu != "Inhaltsstoffe":     klappt nicht, da immer das erste ausgewaehlt wird, obwohl das bereits geklickt ist
 #   menu= driver.find_element(By.CLASS_NAME, "react-tabs__tab")
  #  driver.find_element(By.CLASS_NAME, "react-tabs__tab").click()

#print(menu)

number = 0
counter= 0
while counter < 100:
    try:
        if driver.find_element(by = By.XPATH, value ='//*[@id="react-tabs-' +str(number)+'"]') and driver.find_element(by = By.XPATH, value ='//*[@id="react-tabs-' +str(number)+'"]').text == "INHALTSSTOFFE":
            driver.find_element(by = By.XPATH, value ='//*[@id="react-tabs-' +str(number)+'"]').click()
            ingr_list["ingredients"] = driver.find_element(by = By.XPATH, value ='/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div/div[1]/div/div[3]/div').text
            
    except Exception as err:
        pass
    number +=1
    counter += 1   

       
print(ingr_list)

#driver.find_element(by = By.XPATH, value ='//*[@id="react-tabs-2"]').click()

#menues = soup2.find_all('li', attrs = {'class' :'react-tabs__tab'})
#print(menues)
#for menu in menues:
 #   if menu.text == "Inhaltsstoffe":
  #      print(menu)
   #     var_id = menu.id
    #    print(var_id)
     #   menu.click()                #kann man auf den Xpath von Menu zugreifen?

#driver.find_element(by = By.XPATH, value ='//*[@id="react-tabs-' + var_id + '"]').click()   #nicht die zahl ist die id sondern das ganze was eingesetzt wird
#driver.find_element(by = By.XPATH, value ='//*[@id="react-tabs-4"]').click()
#listen = []
#listen = soup2.findAll('li', attrs = {'class' :'react-tabs__tab'})
#print(listen)
#liste = soup2.find('li', attrs = {"text" == "Inhaltsstoffe"})
#liste.click()
#if soup2.findAll('li', attrs = {'react-tabs__tab'}) and soup2.findAll('li', attrs = {'react-tabs__tab'}).text == "Inhaltsstoffe":
#for liste in listen:
 #   if(liste.text == "Inhaltsstoffe"):
  #      click()
#        #print(liste)
#ingr_list["ingredients"] = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[1]/div/div[1]/div[3]/div/div[2]/div/div/div/div[1]/div/div[3]/div/div/p').text
#print(ingr_list)