from flask_wtf import FlaskForm
from wtforms import BooleanField ,SubmitField, StringField, EmailField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, Length, URL


class RegisterForm(FlaskForm):
    """
    Form for registering a user
    """
    username = StringField(
        label='Username',
        validators=[DataRequired(message="Username is required"), Length(min=2,max=100)],
        render_kw={'placeholder':'username', 'class':'form-control'},
    )
    email = EmailField(
        label='Email',
        validators=[DataRequired(message="Email address is required"), Email() ,Length(min=3,max=100)],
        render_kw={'placeholder':'email', 'class':'form-control'},
    )
    password = PasswordField(
        label='Password',
        validators=[DataRequired(message="Password is required"), Length(min=6,max=100)],
        render_kw={'placeholder':'password', 'class':'form-control'},
    )
    submit = SubmitField(
        "SIGN ME UP!",
        render_kw = {"class":"btn btn-primary"},
    )


class LogInForm(FlaskForm):
    """
    Form for login a user
    """
    username = StringField(
        label='Username',
        validators=[DataRequired(message="Username is required"), Length(min=2,max=100)],
        render_kw={'placeholder':'username', 'class':'form-control'},
    )
    password = PasswordField(
        label='Password',
        validators=[DataRequired(message="Password is required"), Length(min=6,max=100)],
        render_kw={'placeholder':'password','class':'form-control'},
    )
    submit = SubmitField(
        "LogIn!",
        render_kw = {"class":"btn btn-primary"},
    )


class AddCafeForm(FlaskForm):
    """
    Form for adding a cafe
    """
    name = StringField(
        label='Café name',
        validators=[DataRequired(message="Café name is required"), Length(min=2,max=200)],
        render_kw={'placeholder':'Café name', "class":"form-control"},
    )
    map_url = StringField(
        label='Café Location on Google Maps (URL)',
        validators=[DataRequired(message="Café Map URL is required"), URL(), Length(min=2,max=300)],
        render_kw={'placeholder':'Café Map URL', "class":"form-control"},
    )
    img_url = StringField(
        label='Café Image Location URL',
        validators=[DataRequired(message="Café Image URL is required"), URL(), Length(min=2,max=300)],
        render_kw={'placeholder':'Café Image URL', "class":"form-control"},
    )
    location = StringField(
        label='Café Location',
        validators=[DataRequired(message="Café Location is required"), Length(min=2,max=100)],
        render_kw={'placeholder':'Café location - city', "class":"form-control"},
    )
    seats = SelectField(
        label='Café Seating',
        choices=[
            "0-10", "10-20", "20-30", "30-45", "45-60", "60-80", "80+"
        ],
        validators=[DataRequired(message="Café seating option is required")],
        render_kw={"class":"form-select"},
    )
    coffee_price = SelectField(
        label='Coffee Price',
        choices=[
            "2.00 and under", "2.00-5.00", "5.00-7.50", "7.50-10.00", "10.00+",
        ],
        validators=[DataRequired(message="Coffee Price range is required")],
        render_kw={"class":"form-select"},
    )
    price_currency = SelectField(
        label='Currency',
        choices=[
            "£", "€", "$",
        ],
        validators=[DataRequired(message="Currency is required")],
        render_kw={"class":"form-select"},
    )
    has_sockets = BooleanField(
        label='Access to sockets',
        default='True',
        render_kw={"class":"form-check-input"},
    )
    has_toilet = BooleanField(
        label='Access to Toilets',
        default='True',
        render_kw={"class":"form-check-input"},
    )
    has_wifi = BooleanField(
        label='Access to WIFI',
        default='True',
        render_kw={"class":"form-check-input"},
    )
    can_take_calls = BooleanField(
        label='Access to a Phone',
        render_kw={"class":"form-check-input"},
    )
    submit = SubmitField(
        "Add Café!",
        render_kw = {"class":"btn btn-primary w-100"},
    )