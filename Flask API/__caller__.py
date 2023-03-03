#this file is the caller API to handle the connections between the website, the webscraper and the database
#flask and the website both need to run on servers!

from flask import Flask
from flask import request
from flask_cors import CORS
import Sephora_Webscraper as sephora 
import json

#create an instance of Flask and enables Cross Origin Resource Sharing (CORS) for the sephora website
app = Flask(__name__)
CORS(app)

#api call search_string -> product details and id
@app.route('/')
def search():
  search = request.args.get('search')
  print(search)
  return sephora.crawl(search)

#api call id -> database entry   OR     url -> web scraper results
#to get the ingredients
@app.route('/products', methods = ['GET', 'POST'])  
def ingredients_post():
  if request.method == 'POST':
    data = request.get_json()      
    print(data)
    id = data['id']
    #test, ob bereits in db vorhanden  
    #wenn ja, dann db zugriff
    #wenn nein, dann api zugriff, webscraper und score Berechnung
    url = data['url']
    
    print(id)
    print(url)
    return sephora.scrape(url)  #später url
  else:  return "hello"

