from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField,BooleanField,SubmitField
from ..models import User 
from wtforms import ValidationError
from wtforms.validators import Required,Email,EqualTo

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators = [Required(),Email()])
    username = StringField('username',validators = [Required(),Email()])
    password = PasswordField('Password',validators = [Required(),EqualTo('password_confirm',message = 'Passwordsmust match!')])
    password_confirm =PasswordField('Confirm Password',validators = [Required()])
    submit = SubmitField('Sign Up')
    
    
    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise VallidationError('An Account With That Email Already Exipython3.6 manage.py db migrate -m "Initial Migration"sts')
    def validate_username(self,data_field):
        if User.query.filter_by(Username = data_field.data).first():
            raise ValidationError('Tht username is already taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators = [Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')