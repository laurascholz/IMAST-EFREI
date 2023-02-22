from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
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

# db.create_all()

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

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=int, help="Views of the video is required")
video_update_args.add_argument("likes", type=int, help="Likes on the video is required")


# videos = {} #before database

#def abort_if_video_id_doesnt_exist(video_id):
  #  if video_id not in videos:
  #      abort(404, message = "Could not find video...") #sends an error massage back #404 could not find

#def abord_if_video_exists(video_id):
   # if video_id in videos:
   #     abort(409, message= "Video already exists with that ID...")  #409 = already exists

resource_fields = {
    'id':fields.Integer,
    'name':fields.String,
    'views':fields.Integer,
    'likes':fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)              #DB Instance convert into json format 
    def get(self, video_id):
        # abort_if_video_id_doesnt_exist(video_id)             #return statement would be skipped
        result = VideoModel.query.filter_by(id=video_id).first() #search for id=video_id and select the first 
        #return videos[video_id]
        if not result:
            abort(404, message="Could not find video with this id")
        return result
    
    @marshal_with(resource_fields)
    def put(self, video_id): #create new video  #use post to create data, put is for update
        # abord_if_video_exists(video_id)
        args = video_put_args.parse_args()  #args=arguments
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video id taken...")
        #videos[video_id] = args
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)  #temporay add to session
        db.session.commit()  #make permanent in the database
        #return videos[video_id], 201 # 201 code to show that it is created
        return video, 201
    
    #def delete(self, video_id):
       # abort_if_video_id_doesnt_exist(video_id)
       # del videos[video_id]
       # return '', 204 #204 = deleted succesfully
    @marshal_with(resource_fields)
    def patch(self, video_id):  #update  
        args = video_update_args.parse_args()  #args=arguments
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video doesn't exist, cannot update")
        if args['name']:
            result.name = args ['name']
        if args ['views']:
            result.viwes = args ['views']
        if args ['likes']:
            result.likes = args ['likes']
       
        db.session.commit()  #make permanent in the databas
        return result
        
api.add_resource(Video, "/video/<int:video_id>")    #the url the user types in <parameter> string or int...

if __name__ == "__main__":
    app.run(debug=True) #only in testing environment