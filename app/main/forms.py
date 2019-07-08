from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,Email,Length

class BlogForm(FlaskForm):
    title = StringField('Title',validators =  [Required()])
    text = TextAreaField('Blog',validators = [Required()])
    submit = SubmitField('Post')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Update Bio',validators = [Required()])
    submit = SubmitField('Submit')
class CommentForm(FlaskForm):
    name = StringField('Your name',validators = [Required()])
    text = TextAreaField('Leave a comment please thank you',validators = [Required()])
    submit = SubmitField('Comment')
class SubscriberForm(FlaskForm):
    name = StringField('Enter your name',validators = [Required()])
    email = StringField('Enter your email',validators =[Required(),Email()])
    submit = SubmitField('Subscribe')