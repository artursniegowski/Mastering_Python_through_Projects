# 07_Cafe_and_Wifi_Website

This is a fully-fledged website that is mobile-responsive. It lists cafes where users can explore some interesting facts about them; it will show how work- or study-friendly they are based on such factors as WiFi access, toilet access, electrical sockets, the option of taking calls, seating, and coffee price. This website stores the data in a SQLite database in two tables. One table will include all of the cafes, while the other will include all of the users. There is a one-to-many relationship between a user (the creator of the cafe on the website) and a cafe. There are two different users: one is authenticated (logged in), and the other is anonymous (not logged in). Only authenticated users will be able to delete and add cafes to the website's database. The Cafe Wifi website was developed using the Python framework Flask, JavaScript, and HTML, and the styling was done with CSS and Bootstrap 5.2.</br>

The main features are:</br>
- RESTful website: Authenticated users will be able to add new cafes and delete existing cafes from the database (via Flask HTTP requests and forms WTF and AJAX JavaScript) on the Cafe Wifi website. Only authenticated users will have those rights. Unauthenticated users will only be able to browse the website. </br>
- User authentication for the website and assigning different permissions based on their status. There will be 2 groups that are distinguished: logged-in users and anonymous users (not logged in). </br>
- passwords that have been hashed and salted are saved in the database.</br>
- all cafe and user data will be stored in a SQLite database and managed using Flask-SQLAlchemy.</br>
- use of Gravatar images to provide an avatar image for website users.</br>
- making use of relational databases (one-to-many relationships). </br>
- message flashing using Flask Flash to give feedback to the user. They will be visible only for one session. </br>
- a multi-page website with an interactive side bar. </br>
- fully mobile responsive with an adaptive side bar.</br>
- customised error handling-403-page Forbidden.</br>
- customised error handling-404-page not found.</br>
- customised error handling-405 Method Not Allowed.</br> 


The data is stored in two different tables using an SQLite database (if launched locally) managed with the help of Flask-SQLAlchemy. Between these two tables, there exists a database relationship "A one to many," which makes it easy to locate all the cafes that were created by a certain user. The Cafe Wifi website can perform POST, GET, and DELETE HTTP requests in order to create, retrieve, or delete cafes or users from the database.

 
The main page consists of a list of cafes with the option to open a Google link to them or to delete the cafe (only visible and accessible if the user is logged in). Users who are not logged in and try to add a cafe will get redirected to the login website, where they can either log in with their credentials or create a new account. After creating an account, the user will be automatically logged in. A notification will always appear at the top of the screen, enhancing the user experience (flash message visible for one session only). Flask flash messaging was implemented to give feedback to the user if the email address is incorrect, like if it already exists in the database, or if the email address does not exist and the user tries to login, or if the password was wrong, or when a cafe will be added, or if the cafe name already exists in the database.


Each user who wants to be authenticated needs to register. After registering, the users' data will be stored securely in the database. Afterwards, the user can simply log in to the Cafe Wifi website.
When the user gets registered, the email address, user name, and hashed password with salt are stored in the database in the users table. This website shows how authentication is done with the use of Flask and Flask-login while maintaining the highest level of security by hashing the user passwords, adding salt to them, and then storing the hash in the database instead of the password itself. Every user who is logged in can always log out.


If the user is not logged in or does not have permission to access a specific website or send DELETE requests, the server will respond with a customized error message:</br> 
- HTTP 403: Forbidden</br> 
- HTTP 404: page not found</br> 
- HTTP 405: Method Not Allowed</br> 


---

Database Schema:</br>

![Screenshot](docs/img/databse_schema.png)</br>

---

Useful Links:

Flask</br>
https://flask.palletsprojects.com/en/2.2.x/</br>

Flask - Message Flashing</br>
https://flask.palletsprojects.com/en/2.2.x/patterns/flashing/</br>

Flask-Gravatar</br>
https://pythonhosted.org/Flask-Gravatar/</br>

Flask-Login / Authentication</br>
https://flask-login.readthedocs.io/en/latest/</br>

WTForms</br>
https://wtforms.readthedocs.io/en/2.3.x/</br>

Flask-WTF</br>
https://flask-wtf.readthedocs.io/en/1.0.x/</br>

Viewing database - SQLite browser </br>
https://sqlitebrowser.org/dl/ </br>

Flask-SQLAlchemy</br>
https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/</br>

SQLAlchemy</br>
https://docs.sqlalchemy.org/en/14/orm/query.html </br>

Environmental variables</br>
https://pypi.org/project/python-dotenv/</br>

Bootstrap - icons with CDN</br>
https://icons.getbootstrap.com/</br>

Bootstrap</br>
https://getbootstrap.com/docs/5.2/getting-started/introduction/</br>

Jinja templates</br>
https://jinja.palletsprojects.com/en/3.1.x/</br>

Hashing + Salting a password</br>
https://werkzeug.palletsprojects.com/en/2.2.x/utils/</br>
https://werkzeug.palletsprojects.com/en/2.2.x/utils/#werkzeug.security.generate_password_hash</br>


---

The necessary steps to make the program work:</br>
1. Install the Python version as stated in runtime.txt (python-3.11.0)</br>
2. Install the required libraries from the requirements.txt using the following command: </br>
*pip install -r requirements.txt*</br>
3. Change the name of .env.example to .env.</br>
4. Define the Flask environmental variables in .env (https://flask.palletsprojects.com/en/2.2.x/config/#SECRET_KEY):</br>
**FLASK_SECRET_KEY** = "your_secret_key_keep_it_secret"</br>
5. You have the option of using the existing database (at this point, you will use SQLite) with defined users and cafes or creating a new one.</br>
Alternatively, you can simply delete the database instance/data.db and then run run_main.py.
A new, empty database will be created, and you will have to register the users and add cafes.</br>
I recommend using the SQLite browser to explore the data currently saved in the database (there are two tables, users and cafes).</br>
6. Execute run_main.py to ensure that the website is operational on your local host.</br>
7. Now your website should be running. You can register users or add cafes and explore the functionality.</br>

---

**Example views from the website:**</br>
</br>

***Home page view - logged in user. ***</br>
![Screenshot](docs/img/image1.png)</br>

---

***Adding a Cafe view.***</br>
![Screenshot](docs/img/image2.png)</br>

---

***Validation error while adding a cafe: "name exists already in the database."***</br>
![Screenshot](docs/img/image3.png)</br>

---

***View while logged out - redirecting to home view.***</br>
![Screenshot](docs/img/image4.png)</br>

---

***If you are not logged in and try to add a cafe, you will be redirected to Log In view.*** </br>
![Screenshot](docs/img/image5.png)</br>

---

***Creating an account and registering a user view.***</br>
![Screenshot](docs/img/image6.png)</br>

---

***Custom error page 404 view.***</br>
![Screenshot](docs/img/image7.png)</br>

---

***View after registering for an account (redirects to the home page) The flash message at the top is active only for one session.***</br>
![Screenshot](docs/img/image8.png)</br>

---

***Log in view.***</br>
![Screenshot](docs/img/image9.png)</br>

---

***Home page - mobile view. ***</br>
![Screenshot](docs/img/image10-mobile.png)</br>

---

***Account creation - mobile view. ***</br>
![Screenshot](docs/img/image11-mobile.png)</br>

---

***Sign in – mobile view.***
![Screenshot](docs/img/image12-mobile.png)</br>


</br>

---

**The program was developed using python 3.11.0, Flask 2.2, Flask-Login, Flask - Message Flashing, Flask-SQLAlchemy 3.0, Flask-WTF, SQLite, Hashing passwords with Wergzeug, Flask-Gravatar**

In order to run the program, you have to execute run_main.py.
And your website will be accessible under localhost:5000 (http://127:0:0:1:5000).
