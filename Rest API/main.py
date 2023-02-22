from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask (__name__)
api = Api(app)

names = {"tim": {"age": 19, "gender": "male"}, 
         "bill": {"age": 70, "gender": "male"}, 
         }

class HelloWorld(Resource):                        #define Resource
    def get(self, name):                              #define method: get request
        return names[name]  #json format;if send a get request to URL, get the information Hello World
    
    def post(self):
        return {"data": "Posted"}
    
api.add_resource(HelloWorld, "/helloworld/<string:name>")    #the url the user types in <parameter> string or int...

video_put_args = reqparse.RequestParser()  #new RequestParser-Object, makes sure that the information has the right format and is complete
video_put_args.add_argument("name", type=str, help="Name of the video is required", required =True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required =True)
video_put_args.add_argument("likes", type=int, help="Likes on the video is required", required =True)

videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    
    def put(self, video_id): #create new video
        args = video_put_args.parse_args()  #args=arguments
        return {video_id: args}
        
        
    
api.add_resource(Video, "/video/<int:video_id>")    #the url the user types in <parameter> string or int...

if __name__ == "__main__":
    app.run(debug=True) #only in testing environment