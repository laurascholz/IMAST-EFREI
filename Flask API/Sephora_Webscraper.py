#this webscraper uses the same API that the sephora website uses as well to handle their requests

#  -------------------------- necessary packets and imports for vs code----------------------------
#pip install requests
#pip install bs4
#py -m venv env

import requests
import requests_random_user_agent     #automatically creates a random user
from bs4 import BeautifulSoup
from urllib.parse import urlencode

def crawl(search):

  #request session with individual browser agent using random user agent
  session = requests.Session()      

  #generating a search string that is injected into url
  #urlencode is used to include all special characters and to connect two search words  
  searchstring = urlencode({'query' : search})      

  #url to make post request to       
  url = "https://igcrdsruq7-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.13.1)%3B%20Browser%3B%20instantsearch.js%20(4.49.0)%3B%20JS%20Helper%20(3.11.1)"

  #header needed for API, otherwise error 400
  headers = {'x-algolia-api-key' : '79f5605125908b9b3dd46216f213de60', 'x-algolia-application-id': 'IGCRDSRUQ7'}

  #content as json
  json = {"requests":[{"indexName":"production_eu02_sephora_demandware_net__Sephora_FR__products__fr_FR","params":"clickAnalytics=false&distinct=true&facetingAfterDistinct=false&facets=%5B%22*%22%5D&highlightPostTag=__%2Fais-highlight__&highlightPreTag=__ais-highlight__&hitsPerPage=10&maxValuesPerFacet=200&page=0&" + searchstring + "&tagFilters=&analytics=false"}]}

  #Make request to API and safe in r
  r = requests.post(url, headers=headers, json=json)

  #convert to json object, results will be returned to the website
  result = r.json()



  #Get all hits from result      
  hits = result["results"][0]["hits"]

  return hits

  # a list to store product URLs to access the ingredients
  products = []

  #Get all products details in hits
  for x in hits:
    id = x["id"]
    details = [{}]
    brand = x["brand"]     
    name = x["name"]
    price = str(x["price"]["minPrice"])
    url = x["url"]
    image = x["images"]["productTile"]["url"]
    print("id: "  +  x["id"])      
    print("brand: " + x["brand"])     
    print("name: " + x["name"])
    print("price: " + str(x["price"]["minPrice"]))
    print("url: " +  x["url"])
    print("image: " + x["images"]["productTile"]["url"])
    url= x["url"]
    products.append(url)
    print()

  print(products)
  #------web scraper for ingredients------
def scrape(id):
  ingredients = ["Wasser", "Alcohol", "Fragrance"]

  return ingredients
  for product in products:
    session = requests.Session()
    #print(session.headers['User-Agent'])

    #r = session.get("https://www.sephora.fr/p/perfect-hair-day---shampooing-hydratant-587501.html")   
    r = session.get(product)

    soup = BeautifulSoup(r.content, 'html.parser')

    ingredients = soup.find("div", class_ = "ingredients-content").text

    print(ingredients)