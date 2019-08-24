import os
from flask import Flask, render_template, redirect, request, url_for
from forms.forms import AddRecipeForm
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'bakingBookRecipes'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.secret_key = os.getenv("SECRET")


mongo = PyMongo(app)

@app.route('/')
@app.route('/show_recipes')
def show_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
@app.route('/recipe_card/<recipe_id>')
def recipe_card(recipe_id):
    return render_template("recipecard.html", recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))

@app.route('/recipe_card/<recipe_id>', methods=['POST'])
def save_recipe(recipe_id, user_id):
    user = mongo.db.user.find_one({'_id': ObjectId('5d567ffe1c9d44000015f495')})
    user.update_one({ '$push': { 'saved_recipes': ObjectId(recipe_id) }})
    return render_template("recipecard.html", recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))

@app.route('/submit_recipe', methods = ["GET", "POST"])
def submit_recipe():
    form = AddRecipeForm(request.form)
    recipes = mongo.db.recipes
    if request.method == 'POST':
        ingredients = [x.strip() for x in request.form["ingredients"].split(",") if x != '']
        print(ingredients)
        recipes.insert_one(request.form.to_dict())
    return render_template('submitrecipe.html', form=form)

#@app.route('/insert_recipe', methods=['POST'])
#def insert_recipe():
 #   recipes = mongo.db.recipes
  #  recipes.created_by.update_one('current user') #Need to make this dynamic so sets to currently logged in user
   # recipes.insert_one(request.form.to_dict())
    #return redirect(url_for('/'))

if __name__=='__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)


    