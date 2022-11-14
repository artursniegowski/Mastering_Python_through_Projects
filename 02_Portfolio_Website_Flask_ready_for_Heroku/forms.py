from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, EmailField, TelField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    """
    Form for the contact form
    """
    name = StringField(
        label='Full name', 
        validators=[DataRequired(message="Full name is required"), Length(min=2, max=50)],
        render_kw={'class':'form-control', 'placeholder':'Enter your name...'},
        )
    email = EmailField(
        label='Email address', 
        validators=[DataRequired(message="Email address is required"), Email(), Length(min=2, max=50)],
        render_kw={'class':'form-control', 'placeholder':'name@example.com'},
        )
    phone = TelField(
        label='Phone number', 
        validators=[Length(min=0, max=20)],
        render_kw={'class':'form-control', 'placeholder':'(123) 456-7890'},
        )
    message = TextAreaField(
        label='Message', 
        validators=[DataRequired(message="A message is required"), Length(min=5, max=200)],
        render_kw={'class':'form-control', 'placeholder':'Enter your message here...', 'style':'height: 10rem;'},
        )
    submit = SubmitField("Send")