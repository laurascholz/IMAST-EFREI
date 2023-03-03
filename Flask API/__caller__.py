#this file is the caller API to handle the connections between the website, the webscraper and the database
#flask and the website both need to run on servers!

from flask import Flask
from flask import request
from flask_cors import CORS
import Sephora_Webscraper as sephora 
import json
import insert 

#create an instance of Flask and enables Cross Origin Resource Sharing (CORS) for the sephora website
app = Flask(__name__)
CORS(app)

#api call search_string -> product details and id
@app.route('/')
def search():
  #search string is saved in database
  search = request.args.get('search')
  insert.searchstring_insert(search)
  
  #Get all products details for the database
  results =sephora.crawl(search) 
  for x in results:
    api_id = x["id"]
    product_brand = x["brand"]     
    product_name = x["name"]
    product_price = str(x["price"]["minPrice"])
    product_url = x["url"]
    product_image = x["images"]["productTile"]["url"]
    insert.product_insert(search, api_id, product_name, product_brand, product_price, product_url, product_image)
  return results

#api call id -> database entry   OR     url -> web scraper results   to get the ingredients
@app.route('/products', methods = ['GET', 'POST'])  
def ingredients_post():
  if request.method == 'POST':
    data = request.get_json()      
    #print(data)
    id = data['id']
    #test, ob bereits in db vorhanden 
     
    #wenn ja, dann db zugriff
    #wenn nein, dann api zugriff, webscraper und score Berechnung
    url = data['url']

    #print(id)
    #print(url)
    return sephora.scrape(url)  
  else:  return "Error"

