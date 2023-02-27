#this file is the caller API to handle the connections between the website, the webscraper and the database
#ein ganzes project zu erstellen ist too much, ein einzelnes File muesste ausreichen, ansonsten ein flaskkr erstellen
from flask import Flask
from flask import request
from flask_cors import CORS
import Sephora_Webscraper as sephora 

#create an instance of Flask
app = Flask(__name__)
CORS(app)
#bsp fuer die website
#request an api von den buttons von der home seite

@app.route('/')
def index():
    #if request.method == 'GET':
        #if (args.get("search_string") != None ):
        search = request.args.get('search')
        print(search)
        return sephora.crawl(search)
        
        #elif(args.get("id") != None):   
         #   id = args.get("id") #, default=0, type=int
          #  return "3"
        #else: return "4" #Fehlermeldung
        #neuer request an webscraper?
        #testen ob leeres searchwort?
        #anfrage an sephora api
        #rueckgabe der id von sephora und der namen
        #test, ob bereits in db vorhanden   ->oder sowas wie preise immer aktuell verwenden, weil sich sowas schnell aendert
        #wenn ja, dann db zugriff
        #wenn nein, dann api zugriff, webscraper und score Berechnung
        return id

#zweite api
#fuer alle anderen infos ausser die id, also alles was gedruckt wird

