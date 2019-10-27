import os
import bcrypt
from flask import Flask, flash, render_template, redirect, request, url_for, \
    session
from forms.forms import AddRecipeForm, LoginForm, SignupForm
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from urllib.request import urlopen


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'bakingBookRecipes'
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.secret_key = os.getenv('SECRET')

mongo = PyMongo(app)

""" Helper Functions """
def password_check(password, db_password):
    return bcrypt.checkpw(password.encode('utf-8'), db_password.encode('utf-8'))

""" Routes """

@app.route('/')
@app.route('/show_recipes')
def show_recipes():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())


@app.errorhandler(404)
def page_not_found(e):
    """
    error handler function taken from
    https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
    """
    return render_template('404error.html'), 404


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
        login_username = users.find_one({'user': request.form['username']})
        """ If username exists, check password matches """
        if login_username is not None:
            if(password_check(request.form['password'], login_username['password'])):
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('show_recipes'))
        """ If username and password combination is not correct """
        return render_template('login.html', form=form) \
            + '<p class="invalid-message">Invalid username / password combination</p>'
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
        existing_user = users.find_one({'user': request.form['username']})
        """ If username does not already exist, hash pw and store """
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'user': request.form['username'],
                             'password': hashpass.decode(), 'saved_recipes': []})
            session['username'] = request.form['username']
            """ Return user to login form to log in """
            return redirect(url_for('login'))
        else:
            flash('That username already exists, please choose another.')
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
            mongo.db.recipes.update_one({'_id': recipe }, {"$inc":{'save_count': 1}})
            flash("Recipe has been saved")
        else:
            flash("You have already saved this recipe")
    return render_template('recipecard.html',
                           recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))


@app.route('/my_saved_recipes', methods=['GET', 'POST'])
def my_saved_recipes():
    """ Check user is logged in """
    if 'logged_in' in session:
        user = mongo.db.users.find_one({'user': session['username']})
        saved = user['saved_recipes']
        return render_template('savedrecipes.html', recipes=mongo.db.recipes.find({'_id': {"$in": saved}}))
    return render_template('404error.html')


@app.route('/unsave_recipe/<recipe_id>', methods=['GET', 'POST'])
def unsave_recipe(recipe_id):
    """ Check user is logged in """
    if 'logged_in' in session:
        user = mongo.db.users.find_one({'user': session['username']})
        """ Remove recipe from saved_recipes array in db """
        mongo.db.users.update_one({'user': session['username']}, {"$pull": {"saved_recipes": ObjectId(recipe_id)}})
        mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)}, {"$inc":{'save_count': -1}})
        return redirect(url_for('my_saved_recipes'))
    return render_template('404error.html')


@app.route('/submit_recipe', methods=['GET', 'POST'])
def submit_recipe():
    """ Check user is logged in """
    if 'logged_in' in session:
        new_recipe = None
        form = AddRecipeForm(request.form)
        recipes = mongo.db.recipes
        form_normal = request.form.to_dict()
        flat_form = request.form.to_dict(flat=False)
        if request.method == 'POST':
            default_img_url = '/static/images/default.png'
            input_img_url = request.form['recipe_url']

            try:
                f = urllib.urlopen(urllib.Request(input_img_url))
                deadLinkFound = False
            except:
                deadLinkFound = True

            if deadLinkFound:
                recipe_url = default_img_url

            #if input_img_url != '' and input_img_url.lower().endswith(('.png', '.jpg', '.jpeg')):
             #   recipe_url = input_img_url
            else:
                recipe_url = input_img_url
            new_recipe = recipes.insert_one({
                'recipe_title': form_normal['recipe_title'],
                'sub_title': form_normal['sub_title'],
                'makes': form_normal['makes'],
                'takes': form_normal['takes'],
                'ingredients': flat_form['ingredients'],
                'method': flat_form['method'],
                'created_by': session['username'],
                'recipe_url': recipe_url,
                'save_count': 0
                })
            return redirect(url_for('recipe_card',
                            recipe_id=new_recipe.inserted_id))
        return render_template('submitrecipe.html', form=form)
    return render_template('404error.html')


@app.route('/my_recipes')
def my_recipes():
    if 'logged_in' in session:
        """ Get username of logged in user """
        username = session['username']
        return render_template('myrecipes.html', recipes=mongo.db.recipes.find({'created_by': username}))
    return render_template('404error.html')


@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """ Check user is logged in """
    if 'logged_in' in session:
        recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
        """ check recipe was created by logged in user """
        if recipe['created_by'] == session['username']:
            form = AddRecipeForm()
            """ Populate AddRecipeForm with data from db """
            form = AddRecipeForm(data=recipe)
            form.ingredients.data = recipe['ingredients']
            form.method.data = recipe['method']
            if request.method == 'POST':
                default_img_url = '/static/images/default.png'
                input_img_url = request.form['recipe_url']
                if input_img_url != '' and input_img_url.lower().endswith(('.png', '.jpg', '.jpeg')):
                    recipe_url = input_img_url
                else:
                    recipe_url = default_img_url
                form_normal = request.form.to_dict()
                flat_form = request.form.to_dict(flat=False)
                mongo.db.recipes.update({'_id': ObjectId(recipe_id)}, {
                    'recipe_title': form_normal['recipe_title'],
                    'sub_title': form_normal['sub_title'],
                    'makes': form_normal['makes'],
                    'takes': form_normal['takes'],
                    'ingredients': flat_form['ingredients'],
                    'method': flat_form['method'],
                    'created_by': session['username'],
                    'recipe_url': recipe_url
                    })
                return render_template('recipecard.html', recipes=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))
            return render_template('editrecipe.html', recipe=recipe, form=form)
        return render_template('404error.html')
    return render_template('404error.html')


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    """ Check user is logged in """
    if 'logged_in' in session:
        recipes = mongo.db.recipes
        recipes.remove({'_id': ObjectId(recipe_id)})
        return redirect(url_for('my_recipes'))
    return render_template('404error.html')


@app.route('/search_results', methods=["GET", "POST"])
def search_results():
    if request.method == 'POST':
        keywords = request.form.get("keywords")
        """ Text index on mongodb set for recipe title and subtitle"""
        recipes = mongo.db.recipes.find({"$text": {"$search": keywords}})
        if recipes.count() == 0:
            flash("I'm sorry that search returned no results")
        return render_template('recipes.html', recipes=recipes)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=False)
