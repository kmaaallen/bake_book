#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, \
    session
from forms.forms import AddRecipeForm, LoginForm, SignupForm
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'bakingBookRecipes'
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.secret_key = os.getenv('SECRET')

mongo = PyMongo(app)


@app.route('/')
@app.route('/show_recipes')
def show_recipes():
    return render_template('recipes.html',
                           recipes=mongo.db.recipes.find())


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'logged_in' in session:
        return redirect(url_for('show_recipes'))

    form = LoginForm(request.form)
    if request.method == 'POST':
        users = mongo.db.users
        login_username = users.find_one({'user': request.form['username'
                ]})
        if login_username is not None:
            if bcrypt.checkpw(request.form['password'].encode('utf-8'),
                              login_username['password'].encode('utf-8'
                              )):
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('show_recipes'))

        return render_template('login.html', form=form) \
            + 'Invalid username / password combination'

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('show_recipes'))


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = SignupForm(request.form)
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'user': request.form['username'
                ]})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'
                    ].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'user': request.form['username'],
                             'password': hashpass.decode()})
            session['username'] = request.form['username']
            return redirect(url_for('show_recipes'))

        return 'That username already exists, please choose another.'

    return render_template('signup.html', form=form)


@app.route('/recipe_card/<recipe_id>')
def recipe_card(recipe_id):
    return render_template('recipecard.html',
                           recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))


# @app.route('/recipe_card/<recipe_id>', methods=['POST'])
# def save_recipe(recipe_id, user_id):
 #   user = mongo.db.user.find_one({'_id': ObjectId('5d567ffe1c9d44000015f495')})
  #  user.update_one({ '$push': { 'saved_recipes': ObjectId(recipe_id) }})
   # return render_template("recipecard.html", recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))

@app.route('/submit_recipe', methods=['GET', 'POST'])
def submit_recipe():
    if 'logged_in' in session:
        new_recipe = None
        form = AddRecipeForm(request.form)
        recipes = mongo.db.recipes
        form_normal = request.form.to_dict()
        flat_form = request.form.to_dict(flat=False)

       # if 'recipe_img' in request.files:
          #  recipe_img = request.files['recipe_img']
          #  mongo.save_file(recipe_img.filename, recipe_img)
          #  recipe_img_name = recipe_img.filename

        if request.method == 'POST':
            new_recipe = recipes.insert_one({
                'recipe_title': form_normal['recipe_title'],
                'sub_title': form_normal['sub_title'],
                'makes': form_normal['makes'],
                'takes': form_normal['takes'],
                'ingredients': flat_form['ingredients'],
                'method': flat_form['method'],
                'rating': 0,
                'tags': flat_form['tags'],
                'created_by': session['username'],
                })

             # "recipe_img_name": recipe_img_name

            return redirect(url_for('recipe_card',
                            recipe_id=new_recipe.inserted_id))
        return render_template('submitrecipe.html', form=form)
    return redirect(url_for('login'))


@app.route('/my_recipes')
def my_recipes():
    username = session['username']
    return render_template('myrecipes.html',
                           recipes=mongo.db.recipes.find({'created_by': username}))


@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    form = AddRecipeForm()
    form = AddRecipeForm(data=recipe)
    if request.method == 'POST':
        form_normal = request.form.to_dict()
        flat_form = request.form.to_dict(flat=False)
        mongo.db.recipes.recipe.update_one({
            'recipe_title': form_normal['recipe_title'],
            'sub_title': form_normal['sub_title'],
            'makes': form_normal['makes'],
            'takes': form_normal['takes'],
            'ingredients': flat_form['ingredients'],
            'method': flat_form['method'],
            'rating': 0,
            'tags': flat_form['tags'],
            'created_by': session['username'],
            })

         # "recipe_img_name": recipe_img_name

        return redirect(url_for('recipe_card',recipe_id=new_recipe.inserted_id))
    return render_template('editrecipe.html', recipe=recipe, form=form)

# @app.route('/update_recipe/<recipe_id>')
# def update_recipe(recipe_id):
#     recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
#     if request.method == "POST":
#         recipes.update_one(
#          {
#          "recipe_title" : form_normal["recipe_title"],
#          "sub_title" : form_normal["sub_title"],
#          "makes": form_normal["makes"],
#          "takes": form_normal["takes"],
#          "ingredients":flat_form["ingredients"],
#          "method":flat_form["method"],
#          "rating":0,
#          "tags": flat_form["tags"],
#          "created_by": session['username'],
#          #"recipe_img_name": recipe_img_name
#          }
#           )
#     return render_template("recipecard.html", recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT'
            )), debug=True)
