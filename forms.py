from flask_wtf import Form
from wtforms import TextField, TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired

class AddRecipeForm(Form):
    recipe_title = StringField("Recipe Title", validators=[DataRequired()])
    sub_title = TextField("Recipe Sub-title", validators=[DataRequired()])
    makes = TextField("Makes")
    takes = TextField("How long does this recipe take to make?")
    ingredients = TextAreaField("Ingredients:")
    method = TextAreaField("Method:")
    tags = TextAreafIELD("Tags:")
    submit = SubmitField("Send")
 