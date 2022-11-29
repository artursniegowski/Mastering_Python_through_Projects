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