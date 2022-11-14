from datetime import datetime
from env_variables import (FLASK_SECRET_KEY, GITHUB_LINK, LINKEDIN_LINK,
                           MY_SENDER_EMAIL, MY_SENDER_EMAIL_GMAIL_APP_PASSWORD,
                           RECIVER_EMAIL_FOR_CONTACT_FORM, PORT_HEROKU)
from flask import Flask, jsonify, render_template, request, url_for
from flask_wtf.csrf import CSRFProtect
from forms import ContactForm
from notification_manager import NotificationManager

# creating flask object and its variables
app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
csrf = CSRFProtect(app)



# global variables 
# current year
current_year = datetime.now().strftime("%Y")

# creating an email sender manager object for sending emails
email_sender_manager = NotificationManager(email_app_password=MY_SENDER_EMAIL_GMAIL_APP_PASSWORD
                                            ,email_from=MY_SENDER_EMAIL)


# all Flask routes below
# main route - home - /
@app.route('/', methods = ["GET", "POST"])
def home():
    contact_form = ContactForm()
    
    # validate_on_submit will check if it is a POST request and if it is valid.
    # we keep it for the errors on the form to be displayed !
    if contact_form.validate_on_submit():
        # not used anymore - done with fetch() and javascript !!
        # so the page wont reload after submiting the form!
        pass

    return render_template(
        "index.html",
        current_year = current_year,
        contact_form = contact_form,
        social_media_link = {
            'linkedin': LINKEDIN_LINK,
            'github': GITHUB_LINK,
        },
        get_contact_url = url_for('contact'),
    )


# route for the contact form to send an email
@app.route('/contact', methods = ["POST"])
def contact():

    contact_form = ContactForm()
    
    # validate_on_submit will check if it is a POST request and if it is valid.
    if contact_form.validate_on_submit():
        # getting all the data from the form that was posted
        name = contact_form.name.data
        email = contact_form.email.data
        phone = contact_form.phone.data
        message = contact_form.message.data

        # sending email
        # creating message for the email
        message_content = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        # sending an email
        email_sender_manager.send_gmail_mail(email_title="Portfolio website - new message", 
                                            message_to_send=message_content, 
                                            email_to=RECIVER_EMAIL_FOR_CONTACT_FORM)


        return jsonify(success='true',
                        message="The message was sent successfully!") , 200
    
    return jsonify(success='false',
                    error="Validation Failed - Your message was NOT sent!") , 403




#### running the website ####
# running the app and setting the required env variable as a script
if __name__ == "__main__":
    # only run if it's not imported
    # so only if the file main.py is run directly and not imported
    # by another file

    # adding the env variable for Flask to work
    # > $env:FLASK_APP = "main"
    import os

    # print(os.environ.get("FLASK_APP"))
    os.environ["FLASK_APP"] = "main"

    # > flask run
    # start server
    # in a debug mode not suitable for production !!
    # Setting host='0.0.0.0' will make Flask available from the network)
    # Bind to PORT if defined, otherwise default to 5000.
    app.run(host='0.0.0.0', port=PORT_HEROKU, debug=False)
