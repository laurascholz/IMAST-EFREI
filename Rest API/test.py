import requests

BASE = "http://127.0.0.1:5000/"

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
response = requests.patch(BASE + "video/2", { "likes":100})
print(response.json())