from flask_wtf import FlaskForm
from wtforms import  (
    SubmitField, 
    FileField, 
    )
from flask_wtf.file import FileAllowed

# add a new list
class ImageForm(FlaskForm):
    """
    Form for posting a new image
    """
    image_file = FileField(
        "Image File to upload:",
        validators=[FileAllowed(['jpg', 'png'], 'Error: Accepted formats only: .jpg or .png !')],
        render_kw= {"class":"form-control"}
    )

    submit = SubmitField(
        "Run",
        render_kw = {"class":"btn btn-success"}
    )
