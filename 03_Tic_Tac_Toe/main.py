from ascii_art import (LOGO, SEPERATING_LINES, WELCOME_MESSAGE, 
                    DRAW_MESSAGE, PLAY_THE_GAME_MESSAGE, WINNER_MESSAGE,
                    DO_YOU_WANT_TO_PLAY_AGAINST_COMPUTER_MESSAGE)
from board import TicTacToeBoard

# players
players = {
    'player 1': {
        'name':'player 1',
        'cpu': False,
        },
    'player 2': {
        'name':'player 2',
        'cpu': False,
        },
    }


# creating board object for the Tic Tac Toe game
board_game = TicTacToeBoard()

# start game info
print(LOGO)
print(SEPERATING_LINES(70))
board_game.show_board()
print(WELCOME_MESSAGE)
print(SEPERATING_LINES(70))

# ccreating generator for switching turns for the players
def player_turn_generator() -> str:
    """
    changing the turn of the players
    """
    while True:
        yield players['player 1']
        yield players['player 2']


# creating generator for switching the players - taking turns
# this way X - player will alwasy start the first game
# and then they will alwasy take turns - so next game can start either
# player 1 or 2 it depends who will end the first game
current_player = player_turn_generator()


while True:

    play_the_game = input(PLAY_THE_GAME_MESSAGE).upper().strip()
    if play_the_game != 'Y':
        break
    else:
        players = {
            'player 1': {
                'name':'player 1',
                'cpu': False,
                },
            'player 2': {
                'name':'player 2',
                'cpu': False,
                },
            }

    computer_player = input(DO_YOU_WANT_TO_PLAY_AGAINST_COMPUTER_MESSAGE).upper().strip()
    if computer_player == '1':
        print("You choose player 1 to be CPU.")
        players['player 1']['cpu'] = True
    elif computer_player == '2':
        print("You choose player 2 to be CPU.")
        players['player 2']['cpu'] = True
    else:
        print("You choose player 1 and 2 to be human.")


    # game loop 
    while not(end_of_game := board_game.check_for_end_of_game()):
        # creating generator for switching the players - taking turns
        # this way X - player will alwasy start the first game
        # and then they will alwasy take turns - so next game can start either
        # player 1 or 2 it depends who will end the first game
        player = next(current_player)
        board_game.get_user_input_and_setting_value(player['name'],player['cpu'])
        board_game.show_board()
    else:
        board_game.start_new_game()
        if end_of_game == ' ':
            print(DRAW_MESSAGE)
        else:
            print(WINNER_MESSAGE(end_of_game))