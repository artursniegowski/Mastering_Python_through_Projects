from app_website import app
from flask import (
    flash, 
    render_template, 
    Response,
    url_for, redirect, 
    )
from flask_login import (
    current_user,
    login_user, 
    login_required, 
    logout_user, 
    )
from app_website.forms import LogInForm, RegisterForm
from app_website.models import db, User
from app_website.views import current_year
from werkzeug.security import check_password_hash, generate_password_hash

# register website
@app.route("/register", methods = ['GET','POST'])
def register() -> Response | str:
    """
    registering a new user view
    """
    register_form = RegisterForm()

    # if form is validated then it has to be a POST request
    if register_form.validate_on_submit():
        
        # checking if user/ email already exists
        # making sure the email and username dosent exists in the database
        user_exists = db.session.execute(
            db.select(User).filter_by(username=register_form.username.data.strip())
        ).scalar() # returns None if not found
        email_exists = db.session.execute(
            db.select(User).filter_by(email=register_form.email.data.strip())
        ).scalar() # returns None if not found

        # creating the new user in the database
        if not user_exists and not email_exists:
            
            # create new user
            new_user = User(
                username = register_form.username.data.strip(),
                email = register_form.email.data.strip(),
                # saving the password as a hash with salt on the server
                password = generate_password_hash(
                    password=register_form.password.data,
                    method='pbkdf2:sha256',
                    salt_length=8,
                )
            )

            # saving the new user in the database
            db.session.add(new_user)
            db.session.commit()

            # flash message for one session
            flash(f"An account for {new_user.username} was created!")

            # Login and validate the new user
            login_user(new_user)

            # redirecting to mylists view page
            return redirect(url_for('mylists'))

        else:
            if user_exists and email_exists:
                # flask flash messages
                flash("The email and username already exists. Please sign in!")
                # redirect to login page
                return redirect(url_for('login'))
            
            elif user_exists:
                # flask flash messages
                flash("The username already exists. Try a different username!")
            else:
                # flask flash messages
                flash("The email already exists. Try a different email!")
   

    return render_template(
        'register.html',
        form = register_form,
        current_year = current_year,
    )

# login website
@app.route("/login", methods = ['GET','POST'])
def login() -> Response | str:
    """
    login page view
    """

    login_form = LogInForm()

    # if form is validated then it has to be a POST request
    if login_form.validate_on_submit():
        
        user_trying_to_login = db.session.execute(
            db.select(User).filter_by(username=login_form.username.data.strip())
        ).scalar() # returns None if not found
        
        # if user exists
        if user_trying_to_login:
            
            # checking if password matches the server password
            if check_password_hash(user_trying_to_login.password, login_form.password.data):
                
                # login and validate the user
                login_user(user_trying_to_login)
                # flash message
                flash(f"{user_trying_to_login.username} was logged in.")
                return redirect(url_for('mylists'))
            else:
                flash("Password incorrect!")
                return redirect(url_for('login'))
        else:
            flash("This username dosent exists!")
            return redirect(url_for('login'))

    return render_template(
        'login.html',
        form = login_form,
        current_year = current_year,
    )


# logout website
@app.route("/logout")
@login_required
def logout() -> Response:
    """
    logout page - view 
    """
    # flash message for one session
    flash(f"{current_user.username} was logged out.")
    # logout the current user
    logout_user()
    return redirect(url_for('index'))