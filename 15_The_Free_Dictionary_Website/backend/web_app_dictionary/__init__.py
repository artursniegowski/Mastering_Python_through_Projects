from env_variables import FLASK_SECRET_KEY
from flask import Flask
from flask_wtf import CSRFProtect
from datetime import datetime
from web_app_dictionary.owlbot_API import OwlData

## initializing the object for comunication with the public API
owl_api = OwlData()

# creating flask object and its variables
app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
# setting crsf protection globally
crsf = CSRFProtect(app)

# current year - global variable
current_year: str = datetime.now().strftime("%Y")

# rest of the views
from web_app_dictionary import views