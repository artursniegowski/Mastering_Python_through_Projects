from app_image_website.color_extractor import ColorExtractor
from env_variables import FLASK_SECRET_KEY
from flask import Flask
from flask_wtf import CSRFProtect
# from app_website.forms import ListForm
from datetime import datetime
from pathlib import Path

# the path for uploading files
UPLOAD_FOLDER = 'static/uploads'
# for filtering in the backend file extensions
ALLOWED_FILE_EXTENSIONS = {'png', 'jpg'}


# creating flask object and its variables
app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
# setting crsf protection globally
crsf = CSRFProtect(app)
# configuring the enviromental variable for the path of uploaded files
app.config['UPLOAD_FOLDER'] = (Path(__file__).parent / f"{UPLOAD_FOLDER}").resolve()
# limit the maximum allowed payload to 16 megabytes. If a larger file is 
# transmitted, Flask will raise a RequestEntityTooLarge exception
# Limiting the file uploads amount of memory,  by setting the MAX_CONTENT_LENGTH config key:
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

# current year - global variable
current_year: str = datetime.now().strftime("%Y")

# creating the class responsible for extracting colors
color_extractor = ColorExtractor()

# rest of the views
from app_image_website import views
from app_image_website import views_errors 