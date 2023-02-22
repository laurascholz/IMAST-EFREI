from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"Video(name={name}, views={views}, likes={likes})"

db.create_all()

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

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message = "Could not find video...") #sends an error massage back #404 could not find

def abord_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message= "Video already exists with that ID...")  #409 = already exists

class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)             #return statement would be skipped
        return videos[video_id]
    
    def put(self, video_id): #create new video
        abord_if_video_exists(video_id)
        args = video_put_args.parse_args()  #args=arguments
        videos[video_id] = args
        return videos[video_id], 201 # 201 code to show that it is created
        
    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204 #204 = deleted succesfully
        
    
api.add_resource(Video, "/video/<int:video_id>")    #the url the user types in <parameter> string or int...

if __name__ == "__main__":
    app.run(debug=True) #only in testing environment