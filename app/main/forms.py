from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,Email,Length

class BlogForm(FlaskForm):
    title = StringField('Ttle',validators =  [Required()])
    text = TextAreaField('Blog',validators = [Required()])
    submit = SubmitField('Post')
class UpdateProfile(FlaskForm):
    bio = TextField('Update Bio',validators = [Required()])
    submit = SubmitField('Submit')
