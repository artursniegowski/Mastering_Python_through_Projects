# Mastering_Python_through_Projects
This is a repository of professional projects that can be used as ideas to further your Python skills and master this
versatile scripting language. The repository will cover a wide range of projects like scripting Python projects (text-based), Web Development (Flask), Data Science (Pandas, Numpy, SciPy), GUI - graphical user interface (Tkinter), APIs (Requests), Games (Turtle), Web Scrapping (BeautifulSoup, Selenium), Automating Tasks with Python, and many more.


## 01_Morse_Code_Converter
This is a Python scrypting project - a text-based Morse converter.
Morse code is a way of encoding text characters as standardized sequences of two different signal durations, called dots and dashes, and named after Samuel Morse, one of the inventors of the telegraph.
You can read more [here](https://en.wikipedia.org/wiki/Morse_code).</br>
This programme was developed based on the OOP (object-oriented programming) methodology.
The user will be faced with three options:</br>
- 'encode': after choosing this option, the user will have to provide a text that will be encoded to morse code (the end result),</br>
- 'decode': after choosing this option, the user will have to provide a morse code text that will be decoded (the decoded message will be outputed),</br>
- 'q' - quitting the program.</br>
 

## 02_Portfolio_Website_Flask_ready_for_Heroku
This is a one-page Portfolio Website, a unique way to showcase my work and let others know about myself. It is ready to be published and launched on Heroku (https://www.heroku.com/). This way, it can be easily shared via a link with anyone who is interested in my work. The Portfolio Website was developed using the Python framework Flask, CSS, HTML, and Java Script with AJAX (fetch). The styling was done with the help of additional Bootstrap templates (https://startbootstrap.com/theme/freelancer), Bootstrap, and CSS. Additionally, the website is fully mobile responsive with an adaptive navigation bar, and it has a functional, dynamic contact form, which means that after submitting it, it won't reload the entire page. This functionality is achieved by sending a Java Script AJAX request ([fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)) to the Flask server in order to send the data from the form and later validate it on the server side. If successful, the server will send an email that will consist of the data from the contact form. The server will return json data to the website whether or not the process was successful, which will be rendered with JS as a short message below the contact form. In modern browsers, there is no need to use "AJAX" methods like XMLHttpRequest() or jQuery; the modern, built-in JavaScript solution to make these requests from a page is with the use of fetch. All projects listed on the website have a detailed view in a modal that will appear after selecting one of the projects.

## 03_Tic_Tac_Toe
This is a text-based version of the popular [Tic-Tac-Toe](https://en.wikipedia.org/wiki/Tic-Tac-Toe) game. It is playable from the command line, and it has to be played by two players.
The user gets to choose whether to play against another human player or a computer player (and the user can choose if player 1 or player 2 should be the computer player). The algorithm for the computer player is implemented by checking which fields are empty and choosing a random one. This way, the computer player always leaves some room for the human player to outsmart him.
In the game, two players take turns and place an "X" or "O" in a three-by-three grid. The player who succeeds first in placing three of the same marks in a horizontal, vertical, or diagonal row is the winner. There are in total nine moves the players can make, and if, by placing the last mark on the grid, no one wins, it will be a draw (out of moves). The first game is always started by Player 1 (X), but they always take turns, so when the second game begins, it could be either Player 1 (X) or Player 2 (O), depending on who ended the previous game. The program was developed using the Object Oriented methodology.</br>
Can you beat the computer player??</br>
Have fun playing! 

## 04_Image_Watermarking_Desktop_App
This is a desktop application that makes it possible to add watermarks to uploaded pictures.
Watermark is a pattern that appears as various shades of lightness or darkness to help identify the picture.
This app was developed using Python and Tkinter for creating a graphical user interface.
It will make it possible to add a logo to any image you want. It's basically like an image editing software like Photoshop for adding the watermark, or like an online service like https://watermarkly.com/. </br>

## 05_Typing_Speed_Test_Desktop_App
This desktop application was developed using Python 3.11 and Tkinter for creating a graphical user interface.
The main purpose of this application is to assess the typing speed of the user.
The average typing speed is 40 words per minute. But with practice, you can speed up to 100 words per minute.
It is similar to the online typing-speed-test app: https://typing-speed-test.aoeu.eu/.
How does it work? The user is given some sample text as words, and the user has to start typing them down one by one.
The timer starts counting down from 60 seconds when the user starts typing the first word.
When the timer hits 0, it stops, the user input will be disabled, and the user can check how many words per second (WPS) and how many characters per second (CPS) was it possible for the user to type in a minute.
Each time the user hits the space bar or the enter key, the app will compare the input word with the sample word that was supposed to be typed.
If the user typed the word correctly, it will be highlighted in green, and if the user typed the word incorrectly, it will be highlighted in red.
The current word to be typed will have a green tag around it.
The user can restart the program by pressing the Restart button at any time.

## 06_Breakout_arcade_game
This is a recreation of the famous game Breakout, which was a hit game originally coded up by Steve Wozniak before he and Jobs started Apple.
You can read more about the original game here: https://en.wikipedia.org/wiki/Breakout_(video_game)
It was developed using Python 3.11 and Turtle graphics. The main aim of the game is to use the ball and paddle to break down the wall.
The user will start with three lives, and every time the ball misses the paddle, the user will lose one. If the player runs out of lives, the game is over. The aim is to make sure the ball bounces off the paddle and breaks as many blocks as possible. If all the blocks are broken,
The whole layout will be reloaded, but your score will keep going. Try to achieve the highest score! 

## 07_Cafe_and_Wifi_Website
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

## 08_ToDo_List_Website
This is a fully functional to-do list website. where the user needs to create an account and login in order to use it.
After that, each account will be allowed to create to-do lists where various tasks can be added and, upon completion, marked as done and crossed out. This website makes it possible to keep track of your to-do tasks. To-do lists offer a way to increase productivity by stopping you from forgetting things, helping you prioritize tasks, managing tasks effectively, using your time wisely, and improving time management as well as workflow. This website was built with Python, Flask, SQLite database (a one-to-many relationship), HTML, CSS, JavaScript, and Bootstrap 5.2.</br>
The main features are:</br>
- RESTful website: Authenticated users will be able to add / update / delete - ToDo lists and tasks from the database (via Flask HTTP requests and forms WTF and AJAX JavaScript) on the ToDo List website. Only authenticated users will have those rights.</br>
- a AJAX PATCH request (with JavaScript).</br>
- User authentication for the website and assigning different permissions based on their status. There will be 2 groups that are distinguished: logged-in users and anonymous users (not logged in). </br>
- passwords that have been hashed and salted are saved in the database.</br>
- all data will be stored in a SQLite database and managed using Flask-SQLAlchemy.</br>
- making use of relational databases (one-to-many relationships) and cascade deletion. </br>
- message flashing using Flask Flash to give feedback to the user. They will be visible only for one session. </br>
- a multi-page website with an interactive nav bar. </br>
- fully mobile responsive with an adaptive nav bar.</br>
- customised error handling-401-Unauthorized.</br>
- customised error handling-403-page Forbidden.</br>
- customised error handling-404-page not found.</br>
- customised error handling-405 Method Not Allowed.</br>

## 09_Disappearing_Text_Writing_App
This desktop application was developed using Python 3.11 and Tkinter to create a graphical user interface. For most writers, a big problem is the writing block. Where you can't think of what to write and you can't write anything. One of the most interesting solutions to this is a web app called The Most Dangerous Writing App, an online text editor where, if you stop writing, all your progress will be lost. A timer will count down, and when the website detects the user has not written anything in the last 5 seconds, it will delete all the text they've written so far. This desktop app has similar functionality to the popular https://www.squibler.io/dangerous-writing-prompt-app. The time remaining will be indicated with a progress bar at the top. Every time the user presses a button, the time will be reset. When there are only 1.5 seconds left, the background will change to red to indicate that it is almost out of time. After the time is up, the text gets erased, and the restart button will be enabled. Pressing it will restart the app to its starting condition. The restart button can only be pressed when the time is up! In the start condition, the input text box will have a placeholder, "Start typing..." If the user clicks in the box, the placeholder will disappear, and if the user presses any keyboard key, the timer will start. Have fun writing your next big novel!