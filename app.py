from flask import Flask, render_template, redirect, request, url_for
from bson.objectid import ObjectId
import pymongo
import os

app = Flask(__name__)

MONGODB_URI = os.getenv('MONGO_URI', 'mongodb://localhost')
DBS_NAME = "bakingBookRecipes"
COLLECTION_NAME = 'bakingBookRecipes'

@app.route('/')
@app.route('/show_recipes')
def show_recipes():
    return render_template("recipes.html", bakingBookRecipes=mongodb.bakingBookRecipes.find())


if __name__=='__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)


    