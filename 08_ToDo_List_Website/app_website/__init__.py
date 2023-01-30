from env_variables import FLASK_SECRET_KEY
from flask import Flask
from flask_wtf import CSRFProtect

# creating flask object and its variables
app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
crsf = CSRFProtect(app)


# models for the data base - and connectin to the database
from app_website import models
# adding the custom filers
from app_website import custom_filters
# rest of the views
from app_website import views
from app_website import views_authentication
from app_website import views_errors 