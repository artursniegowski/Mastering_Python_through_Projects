# loading env variables
from dotenv import load_dotenv
load_dotenv()
import os

################################################################################
## sensitive data ###
#####################
# env variables ! - dont change here !
################################################################################
# In order to generate the csrf token, you must have a secret key, this is 
# usually the same as your Flask app secret key. If you want to use another 
# secret key, config it.
FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
################################################################################
# When developing locally, this will use port 5000, in production it will
# bind to enviromental variable PORT (if defined), otherwise default to 5000.
FLASK_PORT = int(os.environ.get('PORT',5000))
################################################################################
# The URI should start with postgresql:// instead of postgres://. 
# SQLAlchemy used to accept both, but has removed support for the postgres name.
# for the DATABASE_URL - if defined the program can use PostgresSQL database
# if not defined the progam will use SQLite databse !
POSTGRESQL_OR_SQLITE_DATABASE_URL = os.environ.get("DATABASE_URL", 'sqlite:///data.db')
if 'postgres://' in POSTGRESQL_OR_SQLITE_DATABASE_URL:
    POSTGRESQL_OR_SQLITE_DATABASE_URL = POSTGRESQL_OR_SQLITE_DATABASE_URL.replace('postgres://', 'postgresql://')
