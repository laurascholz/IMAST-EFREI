#this file is the caller API to handle the connections between the website, the webscraper and the database
#flask and the website both need to run on servers!

from flask import Flask
from flask import request
from flask_cors import CORS
import Sephora_Webscraper as sephora 

#create an instance of Flask
app = Flask(__name__)
CORS(app)


#api call search_string -> product details and id
@app.route('/')
def index():
    search = request.args.get('search')
    print(search)
    return sephora.crawl(search)
        #test, ob bereits in db vorhanden   ->oder sowas wie preise immer aktuell verwenden, weil sich sowas schnell aendert
        #wenn ja, dann db zugriff
        #wenn nein, dann api zugriff, webscraper und score Berechnung
        #andererseits ist das programm eh schneller als ein db zugriff

#second api call: id -> ingredients and score
@app.route('/')
def ingredients():
    id = request.args.get('id')
    print(id)
    return sephora.scrape(id) 
