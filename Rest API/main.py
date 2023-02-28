<<<<<<< HEAD
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import Sephora_webscraper as sephora


app = Flask (__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class ProductModel(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    ingredientslist_id = db.Column(db.Integer, nullable=False)
    api_id = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    product_brand = db.Column(db.String(100), nullable=False)
    product_price = db.Column(db.String(100), nullable=False)
    product_link = db.Column(db.String(100), nullable=False)
    product_image = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"Product(api_id={api_id}, product_name={product_name}, product_brand={product_brand}, product_price={product_price},product_link={product_link},product_image={product_image})"
    
 # db.create_all()

product_post_args = reqparse.RequestParser()  #new RequestParser-Object, makes sure that the information has the right format and is complete
product_post_args.add_argument("api_id", type=int, help="API_ID of the Product is required", required =True)
product_post_args.add_argument("product_name", type=str, help="Name of the Product is required", required =True)
product_post_args.add_argument("product_brand", type=str, help="Brand of the Product is required", required =True)
product_post_args.add_argument("product_price", type=str, help="Price of the Product is required", required =True)
product_post_args.add_argument("product_link", type=str, help="Link of the Product is required", required =True)
product_post_args.add_argument("product_image", type=str, help="Image of the Product is required", required =True)

resource_fields = {
    'api_id':fields.Integer,
    'product_name':fields.String,
    'product_brand':fields.String,
    'product_price':fields.String,
    'product_link':fields.String,
    'product_image':fields.String
}


class Search(Resource):
    def get(self, search_string):
        result = sephora.crawl(search_string)
        print(result)
        if not result:
            abort(404, message="Could not find any product with this search string")
        return result
        

api.add_resource(Search, "/<string:search_string>")    #the url the user types in <parameter> string or int...
 
#api.add_resource(Product, "product/<int:api_id>")    #the url the user types in <parameter> string or int...


if __name__ == "__main__":
    app.run(debug=True) #only in testing environment   
=======
>>>>>>> parent of cc50c57 (webscraper)
