from flask import render_template
from . import main 

# function and method decorator for the error page

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Funtion to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404