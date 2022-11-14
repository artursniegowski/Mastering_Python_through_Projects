# env variables !
from dotenv import load_dotenv
load_dotenv()
import os

################################################################################
## sensitive data ###
#####################
# In order to generate the csrf token, you must have a secret key, this is 
# usually the same as your Flask app secret key. If you want to use another 
# secret key, config it.
# env variables ! - dont change here !
FLASK_SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
# user defined email and app password - has to be GMAIL !
# this email will be used to send the contact form 
MY_SENDER_EMAIL = os.environ.get('MY_SENDER_EMAIL')
MY_SENDER_EMAIL_GMAIL_APP_PASSWORD = os.environ.get('MY_SENDER_EMAIL_GMAIL_APP_PASSWORD')
# email adress where we want to send the contact form to
RECIVER_EMAIL_FOR_CONTACT_FORM = os.environ.get('RECIVER_EMAIL_FOR_CONTACT_FORM')
# social media links
LINKEDIN_LINK = os.environ.get('LINKEDIN')
GITHUB_LINK = os.environ.get('GITHUB')
# When developing locally, this will use port 5000, in production 
# Heroku will set the PORT environment variable.
# Bind to PORT if defined, otherwise default to 5000.
PORT_HEROKU = int(os.environ.get('PORT', 5000))
################################################################################