from flask import render_template,request,redirect,url_for,abort
from . import main

@main.route('/')
def index():
    '''
    View root page function that returnsthe index page and its data
    '''
    title = 'Home - Welcome to My Blog'
    return render_template('index.html',title = title)
