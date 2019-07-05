from flask import Flask
from flask_bootstrap import Bootstrap 
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    
    # creating app configurations
    app = Flask(__name__)
    
    # initializing bootstrap
    bootstrap.init_app(app)
    
    return app