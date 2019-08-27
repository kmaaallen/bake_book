import os
import bcrypt
#from flask_login import current_user, login_user, logout_user, login_required, LoginManager, login_manager
from flask import Flask, render_template, redirect, request, url_for, session
from forms.forms import AddRecipeForm, LoginForm, SignupForm
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'bakingBookRecipes'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.secret_key = os.getenv("SECRET")

#login_manager = LoginManager()
#login_manager.init_app(app)

#@login_manager.user_loader
#def load_user(_id):
 #   return User.get(_id)

mongo = PyMongo(app)

@app.route('/')
@app.route('/show_recipes')
def show_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/login', methods=['GET','POST'])
def login():
    if 'logged_in' in session:
        return redirect(url_for('show_recipes'))
        
    form = LoginForm(request.form)
    if request.method == "POST":
        users = mongo.db.users
        login_username = users.find_one({'user' : request.form['username']})
        if login_username is not None:
            if bcrypt.checkpw(request.form['password'].encode('utf-8'), login_username['password'].encode('utf-8')): 
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('show_recipes'))
    
        return render_template('login.html', form = form) + 'Invalid username / password combination'
        
    return render_template('login.html', form = form) 

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form= SignupForm(request.form)
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'user' : request.form['username']})
        
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'user': request.form['username'], 'password' : hashpass.decode()})
            session['username'] = request.form['username']
            return redirect (url_for('show_recipes'))
        
        return 'That username already exists, please choose another.'
            
    return render_template('signup.html', form = form)
    
@app.route('/recipe_card/<recipe_id>')
def recipe_card(recipe_id):
    return render_template("recipecard.html", recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))

@app.route('/recipe_card/<recipe_id>', methods=['POST'])
@login_required
def save_recipe(recipe_id, user_id):
    user = mongo.db.user.find_one({'_id': ObjectId('5d567ffe1c9d44000015f495')})
    user.update_one({ '$push': { 'saved_recipes': ObjectId(recipe_id) }})
    return render_template("recipecard.html", recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))

@app.route('/submit_recipe', methods=['GET','POST'])
@login_required
def submit_recipe():
    new_recipe = None
    form = AddRecipeForm(request.form)
    recipes = mongo.db.recipes
    form_normal = request.form.to_dict()
    flat_form = request.form.to_dict(flat=False)
    if request.method == "POST":
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


    