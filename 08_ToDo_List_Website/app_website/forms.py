from flask_wtf import FlaskForm
from wtforms import  (
    BooleanField, 
    DateField, 
    EmailField, 
    PasswordField, 
    SelectField,
    StringField, 
    SubmitField, 
    )
from wtforms.validators import DataRequired, Email, Length, Optional

# for authentication - registration form
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
        "Sign up",
        render_kw = {"class":"btn btn-success btn-lg button-submit-form"},
    )

# for authentication - login form
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
        "Log in",
        render_kw = {"class":"btn btn-success btn-lg button-submit-form"},
    )

# add a new list
class ListForm(FlaskForm):
    """
    Form for creating a new list
    """
    title = StringField(
        label='ToDo List title',
        validators=[DataRequired(message="ToDo List title is required"), Length(min=1,max=150)],
        render_kw={'placeholder':'title', 'class':'form-control text-center'},
    )

    submit = SubmitField(
        "Create",
        render_kw = {"class":"btn btn-success btn-lg"},
    )

# for a new task
class TaskCreateForm(FlaskForm):
    """
    Form for creating a new task
    """
    task_name = StringField(
        # label='name',
        validators=[DataRequired(message="Task name is required"), Length(min=1,max=200)],
        render_kw={'placeholder':'Write your next taks here...', 'class':'form-control'},
    )

    submit = SubmitField(
        "Add task",
        render_kw = {"class":"btn btn-success px-5"},
    )

# form to edit a task
class TaskEditForm(FlaskForm):
    """
    Form for editing a task
    """
    task_name = StringField(
        validators=[DataRequired(message="Task name is required"), Length(min=1,max=200)],
        render_kw={'placeholder':'task name', 'class':'form-control text-center'},
    )

    due_date = DateField(
        label='Due Date',
        validators=[Optional()],
        render_kw={'class':'date-input mt-2'},

    )

    stared = BooleanField(
        label='Stared',
        render_kw={"class":"form-check-input font-size-checkbox-task mt-2"},
    )

    color_tag = SelectField(
        label='Color tag',
        choices=[
            "none", "red", "green",
        ],
        validators=[DataRequired(message="Color tag option is required")],
        render_kw={"class":"form-select color-tag-input mt-2"},
    )

    done = BooleanField(
        label='Done',
        render_kw={"class":"form-check-input font-size-checkbox-task mt-2"},
    )

    submit = SubmitField(
        "Save",
        render_kw = {"class":"btn btn-lg btn-success"},
    )