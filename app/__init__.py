from flask import Flask
from flask_bootstrap import Bootstrap 
from config import config_options
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
photos =UploadSet('photos',IMAGES)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    
    # creating app configurations
    app = Flask(__name__)
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    
    # initializing bootstrap
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple = SimpleMDE()
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # confiure UploadSet
    configure_uploads(app,photos)
    
    return app