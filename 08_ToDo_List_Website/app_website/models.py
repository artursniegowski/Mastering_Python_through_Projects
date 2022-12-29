from app_website import app
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
# import sqlalchemy as sa

# Connect to Database
# create the extension
db = SQLAlchemy()
# configure the SQLite database, relative to the app instance folder
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# Upgrade SQLite Database to PostgreSQL - if env variable defined
# otherwise the SQLite database will be used
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL_OR_SQLITE_DATABASE_URL
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
    """
    representation of the user in the database
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(500))

    # Creating one to many relationship - child relationship
    # one user - many tasks
    # This will act like a list of todo_lists atached to each User
    # The list_creator refers to the property in ToDoList class
    # if the User gets deleted, all the asosciated todolists will also get deleted
    todo_lists = relationship('ToDoList', back_populates = 'list_creator', cascade="all, delete")

    # representing when printed
    def __repr__(self) -> str:
        return f"<User {self.username}>"

# List model - representing the cafe teble in the schema
class ToDoList(db.Model):
    """
    representation of the todolist in the database
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.String(100), nullable=False)

    # Many to One Relationship - parent relationship
    # the 'todo_lists' refers to the property in User class
    list_creator = relationship('User', back_populates = 'todo_lists')
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    list_creator_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    # Creating one to many relationship - child relationship
    # one todo_list - many tasks
    # This will act like a List of tasks atached to each List
    # The task_todo_list refers to the property in Task class
    # if the ToDoList gets deleted, all the asosciated task will also get deleted
    tasks = relationship('Task', back_populates = 'tasks_todo_list', cascade="all, delete")

    # representing when printed
    def __repr__(self) -> str:
        return f"<ToDoList {self.title}>"


# Task model - representing the cafe teble in the schema
class Task(db.Model):
    """
    representation of a Task in the database
    """
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(250), nullable=False)
    color_tag = db.Column(db.String(100), nullable=False, server_default="none")
    due_date = db.Column(db.String(100), nullable=False, server_default="No due date")
    done = db.Column(db.Boolean, nullable=False, default=False)
    stared = db.Column(db.Boolean, nullable=False, default=False)

    # Many to One Relationship - parent relationship
    # the 'tasks' refers to the property in List class
    tasks_todo_list = relationship('ToDoList', back_populates = 'tasks')
    # Create Foreign Key, "to_do_list.id" the to_do_list refers to the tablename of ToDoList.
    todo_list_id = db.Column(db.Integer, db.ForeignKey("to_do_list.id"))
    
    # representing when printed
    def __repr__(self) -> str:
        return f"<Task {self.task_name}>"


# create the table schema in the database
# this will not update the schema if it is already created!!
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
