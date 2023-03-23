#this file is the caller API to handle the connections between the website, the webscraper and the database
#flask and the website both need to run on servers!

from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import Sephora_Webscraper as sephora
import check 
import json
import insert 

#creates an instance of Flask and enables Cross Origin Resource Sharing (CORS) for the Sephora website
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


#api call search_string -> product details and id
@app.route('/')
@cross_origin()
def search():
  #insert search string in database if it doesn't already exist
  search = request.args.get('search')
  if insert.searchstring_select(search) == 404:
    insert.searchstring_insert(search)
  #else update search_date
  else: insert.searchstring_update(search)
    
  #Get all products details for the website and database
  results = sephora.crawl(search)     #crawl method accesses Sephora's API

  #specific product details are saved
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

    #details are returned to the website
  return results



#api call: case 1 new product:  url -> web scraper results to get the ingredients AND  ingredients are assessed
#          case 2 saved product: api_id + name -> saved score is returned
@app.route('/products', methods = ['GET', 'POST'])  
@cross_origin()
def ingredients_post():
  if request.method == 'POST':
    data = request.get_json()  
    api_id = data['id']
    product_name = data['name']
    url = data['url']

    #if ingredients don't exist for the product, 
    if insert.ingredients_select(api_id, product_name) == 404:
      #get ingredients through web scraping
      ingredients_list = sephora.scrape(url)  
      #insert ingredientslist in relation
      insert.ingredients_insert(api_id, product_name, ingredients_list)

    #call of check.py to assess the ingredients
    harmfull = ""
    results2 = [0,0,0,0]
    try:
      #if count of harmfull and harmless ingredients doesnt exist in database
      if check.select_ingredientsscore(api_id, product_name) == 404: 
              results = check.ingredients_check(api_id, product_name)   #saves the values in database          
      
      #else the already saved values are returned
      else: results = check.select_ingredientsscore(api_id, product_name) 
      
      #if there are harmul ingredients included, get the explanation what kind of harmful they are
      if results[0] > 0:
        results2 = check.select_explanation(api_id, product_name) #selects the explanation
      
      #all values are saved in array
      harmfull = [results[0], results[1], results2[0], results2[1], results2[2], results2[3]] 
    except:
       print("Error while checking") 
    return harmfull
  else:  return "Error"

