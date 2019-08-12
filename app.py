from flask import Flask
from flask_pymongo import PyMongo
from bson.objectId import ObjectId
import os

app = Flask(__name__)

if __name__=='__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)s