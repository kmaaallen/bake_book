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
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm(request.form)
    return render_template('login.html', form = form)

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form= signupForm(request.form)
    return render_template('signup.html', form = form)

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

@app.route('/submit_recipe', methods=['GET','POST'])
def submit_recipe():
    new_recipe = None
    form = AddRecipeForm(request.form)
    recipes = mongo.db.recipes
    form_normal = request.form.to_dict()
    flat_form = request.form.to_dict(flat=False)
    if(request.method == "POST"):
        new_recipe = recipes.insert_one(
         {
         "recipe_title" : form_normal["recipe_title"],
         "sub_title" : form_normal["sub_title"],
         "makes": form_normal["makes"],
         "takes": form_normal["takes"],
         "ingredients":flat_form["ingredients"],
         "method":flat_form["method"],
         "rating":0,
         "tags": flat_form["tags"],
         "created_by": "current user"
         }
           )
        return redirect(url_for('recipe_card', recipe_id = new_recipe.inserted_id))
    return render_template('submitrecipe.html', form=form);
    
if __name__=='__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)


    