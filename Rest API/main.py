from flask import Flask
from flask_restful import Api, Resource

app = Flask (__name__)
api = Api(app)

names = 

class HelloWorld(Resource):                        #define Resource
    def get(self, name):                              #define method: get request
        return {"name": name}  #json format;if send a get request to URL, get the information Hello World
    
    def post(self):
        return {"data": "Posted"}
    
api.add_resource(HelloWorld, "/helloworld/<string:name>")    #the url the user types in <parameter> string or int...

if __name__ == "__main__":
    app.run(debug=True) #only in testing environment