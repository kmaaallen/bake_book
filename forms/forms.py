from flask_wtf import Form
from wtforms import TextField, TextAreaField, StringField, SubmitField, PasswordField, FileField
from wtforms.validators import DataRequired

class AddRecipeForm(Form):
    recipe_title = StringField("Recipe Title", validators=[DataRequired()])
    sub_title = TextField("Recipe Sub-title", validators=[DataRequired()])
    recipe_url = TextField("Recipe Image URL")
    makes = TextField("Makes")
    takes = TextField("Takes")
    ingredients = TextField("Ingredients:")
    method = TextField("Method:")
    tags = TextField("Tags:")
    submit = SubmitField("Send")
    
class LoginForm(Form):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    
class SignupForm(Form):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
 