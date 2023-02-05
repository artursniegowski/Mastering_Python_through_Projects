# 11_Image_Color_Palette_Generator

This is a website where the user can upload an image, and it will be processed on the backend side. The most common colors in that image will be extracted from it and listed under the picture with their hex values. This will make it easy to copy the colors if you want to use them in your project. A good example of this functionality can be found on this website: http://www.coolphptools.com/color_extract#demo. Because the website is static, no images are saved on the server; instead, after submitting the form, the file (picture) that the user chose to upload is stored in an in-memory bytes buffer using the buffered I/O implementation. This makes it possible to render images in the HTML without saving them on the server. The form can be submitted with the button RUN. The website was built with the Python web framework - Flask, and the image processing was done with NumPy and Pillow. The styling was done with HTML, CSS, JavaScript, and Bootstrap 5.3. This project is a great example of how to connect a data science task like image processing with a web framework like Flask.
Other features:</br>
- customized error messages were implemented to improve the user experience.</br>
- customised error handling-401-Unauthorized.</br> 
- customised error handling-403-page Forbidden.</br>
- customised error handling-404-page not found.</br>
- customised error handling-405 Method Not Allowed</br> 
- mobile responsive with an adaptive nav bar</br>
- using Jinja2 templating</br>
- image processing using NumPy for identifying the most common colors in the picture</br>
- the use of pillow librarary for image reading</br>
- Buffered I/O implementation using an in-memory bytes buffer</br>
- Directly displaying flask images to HTML without saving them as files on the server</br>
- FileField validation (format and size)</br>

---

Useful Links:

Flask</br>
https://flask.palletsprojects.com/en/2.2.x/</br>

WTForms</br>
https://wtforms.readthedocs.io/en/3.0.x/</br>

Flask-WTF</br>
https://flask-wtf.readthedocs.io/en/1.0.x/</br>

Environmental variables</br>
https://pypi.org/project/python-dotenv/</br>

Bootstrap - icons with CDN</br>
https://icons.getbootstrap.com/</br>

Bootstrap</br>
https://getbootstrap.com/docs/5.3/getting-started/introduction/</br>

Jinja templates</br>
https://jinja.palletsprojects.com/en/3.1.x/</br>

NumPy</br>
https://numpy.org/</br>

Pillow</br>
https://pillow.readthedocs.io/en/stable/</br>

io — Core tools for working with streams</br>
https://docs.python.org/3/library/io.html</br>


---

The necessary steps to make the program work:</br>
1. Install the Python version as stated in runtime.txt (python-3.11.0)</br>
2. Install the required libraries from the requirements.txt using the following command: </br>
*pip install -r requirements.txt*</br>
3. Change the name of .env.example to .env.</br>
4. Define the Flask environmental variables in .env (https://flask.palletsprojects.com/en/2.2.x/config/#SECRET_KEY):</br>
**FLASK_SECRET_KEY** = "your_secret_key_keep_it_secret"</br>
5. Execute main.py to ensure that the website is operational on your local host.</br>
6. Now your website should be running. You can start extracting colors from the uploaded pictures.</br>

---


**Example views from the website:**</br>
</br>

***About page view.***</br>
![Screenshot](docs/img/01_img.png)</br>

---


***Home page view - with the default picture and colors extracted.***</br>
![Screenshot](docs/img/02_img.png)</br>

---


***Home page view - after uploding another image and colors extracted.***</br>
![Screenshot](docs/img/03_img.png)</br>

---


***Home page view - with a validation error after submitting a wrong format image.***</br>
![Screenshot](docs/img/04_img.png)</br>

---


***Home page view - mobile view.***</br>
![Screenshot](docs/img/05_img.png)</br>

---


***Custom Error page view.***</br>
![Screenshot](docs/img/06_img.png)</br>


</br>

---

**The program was developed using python 3.11.0, Flask 2.2, Flask-WTF, Jinja, NumPy, Pillow, io, HTML, CSS, Bootstrap**

In order to run the program, you have to execute main.py.
And your website will be accessible under localhost:5000 (http://127:0:0:1:5000).
