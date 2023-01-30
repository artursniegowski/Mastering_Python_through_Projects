"""
All ascii art for the program / TIC-TAC-TOE game
"""

# draws the board witht he given values (X, O, ' ')
BOARD = lambda a1=' ', a2=' ', a3=' ', b1= ' ', b2=' ', b3= ' ', c1= ' ', c2= ' ', c3=' ': \
f"""
    a     b     c
       |     |     
1   {a1}  |  {b1}  |  {c1}   
  _____|_____|_____
       |     |     
2   {a2}  |  {b2}  |  {c2}
  _____|_____|_____
       |     |     
3   {a3}  |  {b3}  |  {c3}
       |     |     
"""

# logo
LOGO = \
"""
████████╗██╗░█████╗░░░░░░░████████╗░█████╗░░█████╗░░░░░░░████████╗░█████╗░███████╗
╚══██╔══╝██║██╔══██╗░░░░░░╚══██╔══╝██╔══██╗██╔══██╗░░░░░░╚══██╔══╝██╔══██╗██╔════╝
░░░██║░░░██║██║░░╚═╝█████╗░░░██║░░░███████║██║░░╚═╝█████╗░░░██║░░░██║░░██║█████╗░░
░░░██║░░░██║██║░░██╗╚════╝░░░██║░░░██╔══██║██║░░██╗╚════╝░░░██║░░░██║░░██║██╔══╝░░
░░░██║░░░██║╚█████╔╝░░░░░░░░░██║░░░██║░░██║╚█████╔╝░░░░░░░░░██║░░░╚█████╔╝███████╗
░░░╚═╝░░░╚═╝░╚════╝░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░░░░░░░╚═╝░░░░╚════╝░╚══════╝
""" 


# addiotnal messages !
WELCOME_MESSAGE = """\nThe board works like a grid, typing 'a1' will result in placing a character in the top left corner.
Type 'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3', to place your Xs and Os.
The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.\n
Player 1 - 'X'
Player 2 - 'O'\n"""

DO_YOU_WANT_TO_PLAY_AGAINST_COMPUTER_MESSAGE = \
"""
Do you want to play against a computer player?? 
choose '0' for Player 1 and 2 to be human players,
choose '1' for Player 1 to be a computer player,
choose '2' for Player 2 to be a computer player:
"""


CHOOSE_MESSAGE = lambda player='X', CPU='':\
f"""
Player '{player}'{CPU} turn,
Type 'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3', to place your {player}s:
"""

COMPUTER_PLAYER_CHOICE_MESSAGE = lambda computer_move:\
f"""
The Computer choose: {computer_move}.
"""

SEPERATING_LINES = lambda number=10:\
f"{number*'-'}"

WINNER_MESSAGE = lambda player:\
f"""
\n
END OF GAME
Congratulations!! Plyer '{player}' won the game !!\n
"""

DRAW_MESSAGE = \
f"""
\n
END OF GAME!
This is a Draw!! out of moves. There is no winner!\n
"""

PLAY_THE_GAME_MESSAGE = \
"""
Do you want to play the game? [Y/n].
tap 'Y' - for yes or 'n' - to quit :
"""