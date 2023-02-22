from flask import Flask
from flask_restful import Api, Resource

app = Flask (__name__)
api = Api(app)

class HelloWorld(Resource):     
    def get(self):                              #get request
        return {"data": "Hello World"}           #json format;if send a get request to URL, get the information Hello World
    
api.add_resource(HelloWorld, "/helloworld")    #the url the user types in

if __name__ == "__main__":
    app.run(debug=True) #only in testing environment