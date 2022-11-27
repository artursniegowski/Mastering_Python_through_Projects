"""This is a class to manage the Tic TAc Toe board game"""
from ascii_art import BOARD, CHOOSE_MESSAGE, COMPUTER_PLAYER_CHOICE_MESSAGE
from random import choice as random_choice

class TicTacToeBoardSettings:
    """
    Settings for the class TicTacToeBoard
    """
    PLAYERS = {
        "player 1":'X',
        "player 2":'O',
    }

    OPTIONS = {
        'a1':0, 
        'b1':1, 
        'c1':2, 
        'a2':3, 
        'b2':4, 
        'c2':5, 
        'a3':6, 
        'b3':7, 
        'c3':8,
        }

    REVERS_OPRIONS = {v:k for k,v in OPTIONS.items()}

class TicTacToeBoard:
    """
    class managing the game - TIC TAC TOE
    """

    def __init__(self) -> None:
        self._reset_board_state()

    def _reset_board_state(self) -> None:
        """
        reseting the board state
        """
        # row / col
        self.board_state = [[' ']*3 for i in range(3)]
        # list of int, all posible positions to which a move can be made
        self.moves_left = [_ for _ in range(9)]
        self.number_of_moves = 0

    def _set_value_for_position_in_board(self, value:str, position:int) -> bool:
        """
        sets the value in the definied position in the board
        where: 

        a1|b1|c1
        --------
        a2|b2|c2
        --------
        a3|b3|c3

        a1 = pos 0, b1 = pos 1, c1 = pos 2
        a2 = pos 3, b2 = pos 4, c2 = pos 5
        a3 = pos 6, b3 = pos 7, c3 = pos 8

        position has to be an integer in the range 0-8 

        value can be either 'X', 'O' or ' '

        returns True if function is successful 
        returns False if the function can't set the value bc of an error
        """
        if isinstance(position, int):
            position = int(position)
        else:
            print("Error: posotion parameter is not an integer!")
            return False

        if isinstance(value, str):
            value = value.upper().strip()
        else:
            print("Error: value parameter is not a string!")
            return False

        if value in ['X', 'O', ' ']:
            if 0 <= position <= 8:
                self.board_state[position//3][position%3] = value
                self.number_of_moves += 1
                return True
            else:
                print("Error: Board out of range!")
                return False
        else:
            print("Error: value is not 'X', 'O' or ' '!")
            return False


    def _check_if_position_empty(self, position:int) -> tuple[bool, str]:
        """
        checks the given position in the board,

        where: 

        a1|b1|c1
        --------
        a2|b2|c2
        --------
        a3|b3|c3

        a1 = pos 0, b1 = pos 1, c1 = pos 2
        a2 = pos 3, b2 = pos 4, c2 = pos 5
        a3 = pos 6, b3 = pos 7, c3 = pos 8

        position has to be an integer in the range 0-8 

        if it is empty it will return a tuple (True, ' ')
        if the position has alredy value it will return (False,'X') or (False,'O')
        """
        
        position = int(position)
        character_at_the_position = self.board_state[position//3][position%3]
        if character_at_the_position == ' ':
            return (True, ' ')
        else:
            return (False, character_at_the_position)

    def show_board(self) -> str:
        """
        printing the board 
        """
        print(BOARD(
            a1=self.board_state[0][0],
            b1=self.board_state[0][1],
            c1=self.board_state[0][2],
            a2=self.board_state[1][0],
            b2=self.board_state[1][1],
            c2=self.board_state[1][2],
            a3=self.board_state[2][0],
            b3=self.board_state[2][1],
            c3=self.board_state[2][2],
        ))

    def get_user_input_and_setting_value(self, player:str, ai_player: bool = False) -> None:
        """
        getting the user input and setting the value on the board

        player - only valid options:
        'player 1' or 'player 2'

        ai_player - if true the computer will make the move,
        if false a humna has to make a move
        """
        if player in TicTacToeBoardSettings.PLAYERS:
            if not ai_player:
                while (players_choice := input(CHOOSE_MESSAGE(player=TicTacToeBoardSettings.PLAYERS[player])).lower().strip()) \
                    not in TicTacToeBoardSettings.OPTIONS:

                    print(f"\nYour choice '{players_choice}' is not valid! options: {list(TicTacToeBoardSettings.OPTIONS.keys())}")

                else:
                    # checking if the given position is empty
                    is_position_empty = self._check_if_position_empty(position=TicTacToeBoardSettings.OPTIONS[players_choice])
                    if is_position_empty[0] :

                        # setting the value
                        self._set_value_for_position_in_board(
                            value=TicTacToeBoardSettings.PLAYERS[player],
                            position=TicTacToeBoardSettings.OPTIONS[players_choice]
                            )

                        self.moves_left.remove(TicTacToeBoardSettings.OPTIONS[players_choice])

                    else:
                        print(f"{players_choice} has already a value: {is_position_empty[1]}. Try a different position!!")
                        self.get_user_input_and_setting_value(player)
            # computer makes a move - random move
            else:
                print(CHOOSE_MESSAGE(player=TicTacToeBoardSettings.PLAYERS[player],CPU=' - ComputerPlayer'))
                
                random_move = random_choice(self.moves_left)
                # computer makes a move
                # setting the value

                print(COMPUTER_PLAYER_CHOICE_MESSAGE(computer_move=TicTacToeBoardSettings.REVERS_OPRIONS[random_move]))

                self._set_value_for_position_in_board(
                    value=TicTacToeBoardSettings.PLAYERS[player],
                    position=random_move
                    )

                self.moves_left.remove(random_move)
        else:
            print("Error: wrong player input!!")
            return 0

    def check_for_end_of_game(self) -> str:
        """
        checking for end of game,
        if there is a winner it will return either 'X' or 'O' coresponding to the winner
        if it is a draw it will return ' '
        and if it returns False, than the game is not over yet!
        """
        

        # checking all the posible winnig options 
        for num in range(3):
            if  self.board_state[0][num] == self.board_state[1][num] == self.board_state[2][num] != ' ':

                return self.board_state[0][num]
        
        for num in range(3):
            if  self.board_state[num][0] == self.board_state[num][1] == self.board_state[num][2] != ' ':
                return self.board_state[num][0]

        if self.board_state[0][0] == self.board_state[1][1] == self.board_state[2][2] != ' ':
            return self.board_state[1][1]

        if self.board_state[2][0] == self.board_state[1][1] == self.board_state[0][2] != ' ':
            return self.board_state[1][1]

        # this is a draw, no winner but the game ended
        if self.number_of_moves >= 9:
            return ' '


        return False

            
    def start_new_game(self) -> None:
        """
        reseting all the values for a new game
        """
        self._reset_board_state()