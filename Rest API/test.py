#import requests
import product_insert as insert
#BASE = "http://127.0.0.1:5000/"

#data = [{"likes": 78, "name": "Joe", "views":1000000},
      #  {"likes": 10, "name": "How to make REST API", "views":800000},
       # {"likes": 35, "name": "Tim", "views":2000}]

#for i in range(len(data)):
    #response = requests.put(BASE + "video/" + str(i), data [i])
   # print(response.json())

#input ()

#response = requests.delete(BASE + "video/0")
#print(response)

#input()
<<<<<<< HEAD
#response = requests.patch(BASE + "video/2", { "likes":100})
#response = requests.get(BASE , {"search": "Mascara"})
# print(response)

try:
       insert.product_insert(123, 'Lippenstift', 'Lancome', '30.00 €', 'www.sephora.de/lancome/lippenstift', 'www.sehora.de/image/lippenstift')
       print("In datenbank eingespeichert")
except:
       print("Nicht eingespeichert.")
       
=======
response = requests.patch(BASE + "video/2", { "likes":100})
print(response.json())
>>>>>>> parent of cc50c57 (webscraper)
