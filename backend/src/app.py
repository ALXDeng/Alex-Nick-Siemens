from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

app = Flask(__name__)
uri = "mongodb+srv://guest:helloimguest@cluster0.huo8uei.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
app.config['MONGO_URI'] = uri
mongo = PyMongo(app)

CORS(app)


user_collection = mongo.cx['sample_mflix'].users

# @app.route("/")
# def index():
#     return '<h1>Hello World<h1>'

@app.route("/users", methods = ["POST"])
def createUser():
    id = user_collection.insert_one({
        'name': request.json['name'],
        'email': request.json['email'],
        'contact': request.json['contact'],
        'address': request.json['address']
    }).inserted_id  # Note how the inserted_id is accessed
    return jsonify({'id': str(id), 'msg': "User Added Successfully"})

@app.route("/hello", methods = ["POST"])

def retHello():
    return "hello world"
if __name__ == '__main__':
    app.run(debug = True)

