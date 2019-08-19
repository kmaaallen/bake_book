import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'bakingBookRecipes'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')


mongo = PyMongo(app)

@app.route('/')
@app.route('/show_recipes')
def show_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
@app.route('/recipe_card')
def recipe_card():
    return render_template("recipecard.html", recipes=mongo.db.recipes.find())


if __name__=='__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)


    