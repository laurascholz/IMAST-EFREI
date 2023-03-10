#this webscraper uses the same API that the sephora website uses as well to handle their requests

#  -------------------------- necessary packets and imports for vs code----------------------------
#pip install requests
#pip install bs4
#py -m venv env

import requests
import requests_random_user_agent     #automatically creates a random user for every session
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



  #------web scraper for ingredients------
def scrape(url):   
  ingredients = ""
  session = requests.Session()
  #print(session.headers['User-Agent'])

  #the product page is saved and parsed into html code
  r = session.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')

  #the ingredients are accessed from their div container called "ingredients-content"
  ingredients = soup.find("div", class_ = "ingredients-content").text

  #removes all non ingredient words from ingredients list
  substring = "Cette liste d'ingr??dients peut faire l'objet de modifications, veuillez consulter l'emballage du produit achet??."
  substring2 = "Les listes d???ingr??dients entrant dans la composition des produits de notre marque sont r??guli??rement mises ?? jour. Avant d???utiliser un produit de notre marque, vous ??tes invit??s ?? lire la liste d???ingr??dients figurant sur son emballage afin de vous assurer que les ingr??dients sont adapt??s ?? votre utilisation personnelle "
  substring3 = "Ingrediente"
  substring4 = "INGREDIENTS"
  substring5 = "(1)certified organic ingredient"
  substring6 = "AVANT D???UTILISER UN PRODUIT DE NOTRE MARQUE, VOUS ??TES INVIT??S ?? LIRE LA LISTE D???INGR??DIENTS FIGURANT SUR SON EMBALLAGE AFIN DE VOUS ASSURER QUE LES INGR??DIENTS SONT ADAPT??S ?? VOTRE UTILISATION PERSONNELLE"
  sub_list = [substring, substring2, substring3, substring4, substring5, substring6]
  for sub in sub_list:
    if sub in ingredients:
      ingredients = ingredients.replace(sub, "")    
  ingredients = ingredients.replace("???",",")
  
  
  #ingredients are saved all caps
  ingredients = ingredients.upper()
  return ingredients