from flask_wtf import Form
from wtforms import TextField, TextAreaField, StringField, SubmitField, PasswordField
from wtforms.fields.html5 import  URLField
from wtforms.validators import DataRequired, URL


class AddRecipeForm(Form):
    recipe_title = StringField("Recipe Title", validators=[DataRequired()])
    sub_title = TextField("Recipe Sub-title", validators=[DataRequired()])
    recipe_url = URLField("Recipe Image URL", validators=[URL(False, message="Please enter a valid url or leave blank to use default image")])
    makes = TextField("Makes", validators=[DataRequired()])
    takes = TextField("Takes", validators=[DataRequired()])
    ingredients = TextField("Ingredients:", validators=[DataRequired()])
    method = TextAreaField("Method:", validators=[DataRequired()])
    submit = SubmitField("Send")

class LoginForm(Form):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

class SignupForm(Form):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
