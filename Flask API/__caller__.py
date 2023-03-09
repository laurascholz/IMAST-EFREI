#this file is the caller API to handle the connections between the website, the webscraper and the database
#flask and the website both need to run on servers!

from flask import Flask
from flask import request
from flask_cors import CORS
import Sephora_Webscraper as sephora
import check 
import json
import insert 

#create an instance of Flask and enables Cross Origin Resource Sharing (CORS) for the sephora website
app = Flask(__name__)
CORS(app)

#api call search_string -> product details and id
@app.route('/')
def search():
  
  #insert search string in database if it doesn't already exist
  search = request.args.get('search')
  if insert.searchstring_select(search) == 404:
    insert.searchstring_insert(search)
  #else update search_date
  else: insert.searchstring_update(search)
  
  
  #Get all products details for the database
  results = sephora.crawl(search) 
  for x in results:
    api_id = x["id"]
    product_brand = x["brand"]     
    product_name = x["name"]
    product_price = str(x["price"]["minPrice"])
    product_url = x["url"]
    product_image = x["images"]["productTile"]["url"]
    #only add products to database that don't already exist
    if insert.product_select(api_id, product_name) == 404:
      insert.product_insert(search, api_id, product_name, product_brand, product_price, product_url, product_image)
    #else update product url, image and price in database
    else: insert.product_update(search, api_id, product_name, product_price, product_url, product_image)
  return results

#api call id -> database entry   OR     url -> web scraper results   to get the ingredients
@app.route('/products', methods = ['GET', 'POST'])  
def ingredients_post():
  if request.method == 'POST':
    data = request.get_json()      
    #print(data)
    api_id = data['id']
    product_name = data['name']
    #test, ob bereits in db vorhanden 
    print(product_name)
    #wenn ja, dann db zugriff
    #wenn nein, dann api zugriff, webscraper und score Berechnung
    url = data['url']

    #print(id)
    #print(url)
    ingredients_list = sephora.scrape(url)  

    #if ingredients doesnt exist for the product, insert ingredientslist in relation
    if insert.ingredients_select(api_id, product_name) == 404:
      insert.ingredients_insert(api_id, product_name, ingredients_list)
    #else update ingredientlis of product
    else: insert.ingredients_update(api_id, product_name, ingredients_list)

    harmless = "5"
    harmfull = "13"
    try:
       if check.select_ingredientsscore(api_id, product_name) == 404:  #if count of harmfull and harmless ingredients dosnt exist in database
              results = check.ingredients_check(api_id, product_name)   
              print(results)
              harmfull = [results[0], results[1]]
              print(harmfull)
    except:
       print("Fehler beim Check.") 
    return harmfull
  else:  return "Error"

