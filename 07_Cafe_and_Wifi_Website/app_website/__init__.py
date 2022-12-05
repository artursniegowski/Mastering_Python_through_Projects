from flask import Flask
from flask_wtf import CSRFProtect
from env_variables import FLASK_SECRET_KEY
from flask_gravatar import Gravatar

# creating flask object and its variables
app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
crsf = CSRFProtect(app)

# Initialize with flask application and default parameters:
# Initialize flask_gravatar for avatars
# Gravatar uses your email address to provide your image to other sites
# If you own a WordPress or GitHub account, you probably also have a Gravatar 
# account, and your data was scraped in the leak
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    use_ssl=False,
                    base_url=None)

# models for the data base - and connectin to the database
from app_website import models
# rest of the views
from app_website import views 
from app_website import views_authentication 
from app_website import views_cafe
from app_website import views_errors