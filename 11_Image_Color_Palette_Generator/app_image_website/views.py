from pathlib import Path
from app_image_website import (
    ALLOWED_FILE_EXTENSIONS,
    app, 
    color_extractor, 
    current_year, 
    )
from app_image_website.forms import ImageForm
from flask import (
    render_template, 
    redirect, 
    url_for,
    )
from werkzeug.utils import secure_filename
import os

# Flask routes
# home website
@app.route("/", methods = ['GET','POST'])
def index() -> str:
    """
    the index - home - view
    """
    # starting list of colors is a empty list
    list_of_colors = []

    # creating the form object
    image_form = ImageForm()

    # if form is validated then it has to be a POST request
    if image_form.validate_on_submit():
        # checking if filename exists
        if image_form.image_file.data.filename and "." in image_form.image_file.data.filename:
            # checking if the extensions matches the allowed extension
            if image_form.image_file.data.filename.split(".")[-1].lower() in ALLOWED_FILE_EXTENSIONS:

                # getting the colors from the picture
                color_extractor.image_to_open = image_form.image_file.data
                list_of_colors = color_extractor.retrun_list_of_colors()

                ## PASING THE IMAGE TO THE HTML
                ### SOLUTION 1 - savig uploaded pictures in the uplode folder 
                # making sure the user input is safe to use
                # secure_file_name = secure_filename(image_form.image_file.data.filename)
                # using default file name
                # secure_file_name = "user_default.png"
                # saving the file into a temp file in the system , defined in the Upload folders
                # image_form.image_file.data.save(os.path.join(app.config["UPLOAD_FOLDER"],secure_file_name))
                # update the src file that gets rendered in the html files
                # image_src = url_for('static', filename=f'uploads/{secure_file_name}') 


                # SOLUTION 2 - passing the image without saving the file on the server
                # recomended bc we dont have to save files on the server
                # Pass Images to HTML Without Saving Them 
                # The file read-write procedure used to transfer images created 
                # in the Python Back-end to the Front-end can sometimes cause problems and run slowly. 
                # In addition, some cloud services do not allow you to write files 
                # to your web applications running on free tier accounts
                #
                # this can be achived we the use of  base64 and io
                # using BytesIO we get the in-memory info to save the image we just read
                # Just like what we do with variables, data can be kept as bytes in an 
                # in-memory buffer when we use the io module’s Byte IO operations.
                # We use the in-memory info we get using BytesIO in the save() function inside the PIL library.
                # Finally, we use base64encode to transfer the image we saved as in-memory to html.
                image_src = color_extractor.image_url_from_memory()
       
                return render_template(
                    'index.html',
                    current_year = current_year, 
                    list_of_colors = list_of_colors,
                    img_src = image_src,
                    form = image_form
                )
     
    # only if form dosent work or after validation dosent return colors
    # then we render the default image from our assets
    image_src = url_for('static', filename='assets/lenna_default.png')

    # print((Path(__file__).parent / f".{image_src}").resolve())
    # creating the list of colors from the picture
    # findig the absolute path of the file in order for us to open the file
    color_extractor.image_to_open = (Path(__file__).parent / f".{image_src}").resolve()
    # extracting the list of colors from the defaul image
    list_of_colors = color_extractor.retrun_list_of_colors()

    return render_template(
        'index.html',
        current_year = current_year, 
        list_of_colors = list_of_colors,
        img_src = image_src,
        form = image_form
    )

# home website
@app.route("/about")
def about() -> str:
    """
    the about - view
    """
    return render_template(
        'about.html',
        current_year = current_year, 
    )