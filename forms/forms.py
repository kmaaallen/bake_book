from flask_wtf import Form
from wtforms import TextField, TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired

class AddRecipeForm(Form):
    recipe_title = StringField("Recipe Title", validators=[DataRequired()])
    sub_title = TextField("Recipe Sub-title", validators=[DataRequired()])
    makes = TextField("Makes")
    takes = TextField("Takes")
    ingredients = TextField("Ingredients:")
    method = TextField("Method:")
    tags = TextField("Tags:")
    submit = SubmitField("Send")
 