from flask import Flask
import pymongo
from bson.objectid import ObjectId
import os

app = Flask(__name__)

MONGODB_URI = os.getenv('MONGO_URI', 'mongodb://localhost')
DBS_NAME = "bakingBookRecipes"
COLLECTION_NAME = 'bakingBookRecipes'




if __name__=='__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)


    