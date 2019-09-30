import os
import bcrypt
from flask import Flask, flash, render_template, redirect, request, url_for, \
    session
from forms.forms import AddRecipeForm, LoginForm, SignupForm
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename

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

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ If user already logged in redirect to homepage """
    if 'logged_in' in session:
        return redirect(url_for('show_recipes'))
    """ If user not logged in, check db for username """
    form = LoginForm(request.form)
    if request.method == 'POST':
        users = mongo.db.users
        login_username = users.find_one({'user': request.form['username'
                ]})
        """ If username exists, check password matches """
        if login_username is not None:
            if bcrypt.checkpw(request.form['password'].encode('utf-8'),
                              login_username['password'].encode('utf-8'
                              )):
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('show_recipes'))
        """ If username and password combination is not correct """
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
        """ Check if username already exists in the db """
        existing_user = users.find_one({'user': request.form['username'
                ]})
        """ If username does not already exist, hash pw and store """
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'
                    ].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'user': request.form['username'],
                             'password': hashpass.decode(), 'saved_recipes':''})
            session['username'] = request.form['username']
            """ Return user to login form to log in """
            return redirect(url_for('login'))

        else: flash('That username already exists, please choose another.')

    return render_template('signup.html', form=form)


@app.route('/recipe_card/<recipe_id>')
def recipe_card(recipe_id):
    return render_template('recipecard.html',
                           recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))


@app.route('/save_recipe/<recipe_id>', methods=['GET', 'POST'])
def save_recipe(recipe_id):
    """Check user is logged in """
    if 'logged_in' in session:
        recipe = ObjectId(recipe_id)
        user = mongo.db.users.find_one({'user': session['username']})
        saved = user['saved_recipes']
        """Check recipe is not already saved"""
        if recipe not in saved:
            mongo.db.users.update_one({'user': session['username']}, {"$push": {"saved_recipes": recipe}})
        else:
            flash("Recipe has already been saved")
    return render_template('recipecard.html',
                           recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))

@app.route('/my_saved_recipes', methods=['GET', 'POST'])
def my_saved_recipes():
    """ Check user is logged in """
    if 'logged_in' in session:
        user = mongo.db.users.find_one({'user': session['username']})
        saved = user['saved_recipes']
        if (saved == None):
            flash("Sorry you don't have any saved recipes.")
        return render_template('savedrecipes.html',recipes=mongo.db.recipes.find({'_id': {"$in": saved}}))
    return redirect(url_for('login'))
        
        

@app.route('/unsave_recipe/<recipe_id>', methods=['GET', 'POST'])
def unsave_recipe(recipe_id):
    """ Check user is logged in """
    if 'logged_in' in session:
        user = mongo.db.users.find_one({'user': session['username']})
        """ Remove recipe from saved_recipes array in db """
        mongo.db.users.update_one({'user': session['username']}, {"$pull": {"saved_recipes": ObjectId(recipe_id)}})
        saved = user['saved_recipes']
        return render_template('savedrecipes.html',
                           recipes=mongo.db.recipes.find({'_id': {"$in": saved}}))
    return render_template('login.html', form=LoginForm(request.form))   


@app.route('/submit_recipe', methods=['GET', 'POST'])
def submit_recipe():
    """ Check user is logged in """
    if 'logged_in' in session:
        new_recipe = None
        form = AddRecipeForm(request.form)
        recipes = mongo.db.recipes
        form_normal = request.form.to_dict()
        flat_form = request.form.to_dict(flat=False)
        default_img_url = 'https://imgur.com/a/qeaCvhA'
        
        if request.form['recipe_url'] == '':
            recipe_url = default_img_url
        else:
            recipe_url = form_normal['recipe_url']

            if request.method == 'POST':
                new_recipe = recipes.insert_one({
                    'recipe_title': form_normal['recipe_title'],
                    'sub_title': form_normal['sub_title'],
                    'makes': form_normal['makes'],
                    'takes': form_normal['takes'],
                    'ingredients': flat_form['ingredients'],
                    'method': flat_form['method'],
                    'created_by': session['username'],
                    'recipe_url': recipe_url
                    })
                return redirect(url_for('recipe_card',
                                recipe_id=new_recipe.inserted_id))
        return render_template('submitrecipe.html', form=form)
    return redirect(url_for('login'))

@app.route('/my_recipes')
def my_recipes():
    if 'logged_in' in session:
        """ Get username of logged in user """
        username = session['username']
        return render_template('myrecipes.html',
                           recipes=mongo.db.recipes.find({'created_by': username}))
    return redirect(url_for('login'))


@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """ Check user is logged in """
    if 'logged_in' in session:
        recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
        form = AddRecipeForm()
        """ Populate AddRecipeForm with data from db """
        form = AddRecipeForm(data=recipe)
        form.ingredients.data = recipe['ingredients']
        form.method.data = recipe['method']
    
        if request.method == 'POST':
            form_normal = request.form.to_dict()
            flat_form = request.form.to_dict(flat=False)
            mongo.db.recipes.update({'_id' : ObjectId(recipe_id)}, {
                'recipe_title': form_normal['recipe_title'],
                'sub_title': form_normal['sub_title'],
                'makes': form_normal['makes'],
                'takes': form_normal['takes'],
                'ingredients': flat_form['ingredients'],
                'method': flat_form['method'],
                'created_by' : session['username'],
                'recipe_url': form_normal['recipe_url']
                })
            return render_template('recipecard.html', recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))
        return render_template('editrecipe.html', recipe=recipe, form=form)
    return render_template('login.html', form=LoginForm(request.form))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    """ Check user is logged in """
    if 'logged_in' in session:
        recipes = mongo.db.recipes
        recipes.remove({'_id': ObjectId(recipe_id)})
        return redirect(url_for('my_recipes'))
    return render_template('login.html', form=LoginForm(request.form))
    
@app.route('/search_results', methods=["GET", "POST"])
def search_results():
    if request.method == 'POST':
        keywords = request.form.get("keywords")
        """ Text index on mongodb set for recipe title and subtitle"""
        recipes=mongo.db.recipes.find({"$text": { "$search": keywords}})
    return render_template('recipes.html', recipes=recipes )


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT'
            )), debug=True)
