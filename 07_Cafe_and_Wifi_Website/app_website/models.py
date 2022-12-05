from app_website import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from sqlalchemy.orm import relationship
import sqlalchemy as sa

# Connect to Database
# create the extension
db = SQLAlchemy()
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# initialize the app with the extension
db.init_app(app)

# Configuring Login  Manager
# creating LoginManager object and binding it to the app
login_manager = LoginManager()
# cofiguring the application for login
login_manager.init_app(app)


# defined models
# User model - representing user in the schema
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(500))

    # Creating one to many relationship - child relationship
    # one user - many cafes
    # This will act like a List of cafes atached to each User
    # The cafe_creator refers to the property in Cafe class
    cafes = relationship('Cafe', back_populates = 'cafe_creator')

    # representing when printed
    def __repr__(self) -> str:
        return f"<User {self.username}>"

# cafe model - representing the cafe teble in the schema
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(50), nullable=False)
    coffee_price = db.Column(db.String(50), nullable=True)

    # Many to One Relationship - parent relationship
    # the 'cafes' refers to the property in User class
    cafe_creator = relationship('User', back_populates = 'cafes')
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    cafe_creator_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    # representing when printed
    def __repr__(self) -> str:
        return f"<Cafe {self.name}>"

# create the table schema in the database
# this will not update the schema if it is created!!
with app.app_context():
    db.create_all()


# This callback is used to reload the user object
@login_manager.user_loader
def load_user(user_id) -> User | None:
    """
    This callback is used to reload the user 
    object from the user ID stored in the session. It should 
    take the str ID of a user, and return the corresponding user object
    """
    # It should return None (not raise an exception) if the ID is not valid. 
    # (In that case, the ID will manually be removed from the session and processing will continue.)!!!
    # https://flask-login.readthedocs.io/en/latest/#flask_login.UserMixin
    # Fetch the first row or None if no row is present.
    return db.session.execute(db.select(User).filter_by(id=int(user_id))).scalar()
    # return User.query.get(int(user_id))