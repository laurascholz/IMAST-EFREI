#this file is the caller API to handle the connections between the website, the webscraper and the database
#flask and the website both need to run on servers!

from flask import Flask
from flask import request
from flask_cors import CORS
import Sephora_Webscraper as sephora 
import json

#create an instance of Flask
app = Flask(__name__)
CORS(app)


#api call search_string -> product details and id
@app.route('/')
def search():
    #if request.method == 'GET':
      search = request.args.get('search')
      print(search)
      return sephora.crawl(search)
          #test, ob bereits in db vorhanden   ->oder sowas wie preise immer aktuell verwenden, weil sich sowas schnell aendert
          #wenn ja, dann db zugriff
          #wenn nein, dann api zugriff, webscraper und score Berechnung
          #andererseits ist das programm eh schneller als ein db zugriff


@app.route('/products', methods = ['GET', 'POST'])  #
def ingredients_post():
  if request.method == 'POST':
    data = request.get_json()       #'dict' object has no attribute 'json'
    print(data)
    id = data['id']
    url = data['url']
    print(id)
    print(url)
    #data = request.data
    #print(data("id"))              'bytes' object is not callable
    #id = data["id"]                TypeError: byte indices must be integers or slices, not str
    #data2= request.json()['id']    Fehler: dict object is not callable
    #params = data.json()
    #id = params["id"]
    #print(params)
    #id = data2["id"]
    #id = data.id 
    #url = data.url
    #id = request.args.get('id')
    #url = request.args.get('url')
    #print(data2)
    #print(url)
    return sephora.scrape(url)  #später url
  else:  return "hello"

#second api call: id -> ingredients and score
#@app.route('/products/')
#def ingredients():
 #   id = request.args.get('id')
  #  print(id)
   # return sephora.scrape(id) 
