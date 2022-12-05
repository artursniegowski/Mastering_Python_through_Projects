# Components
# TODO checklist
# 1. Screen - create ----.... DONE .....
# 2. paddle - create and move ----.... DONE .....
# 3. Create a ball and make it move  ----.... DONE .....
# 4. detects collisions with wall and bounce ----.... DONE .....
# 5. detect colision with the padle ----.... DONE .....
# 6. detect when the paddle misses the ball ----.... DONE .....
# 7. Scoreboards and lives !----.... DONE .....
# 8. create blocks that will be destoyed !----.... DONE .....
# 9. detect colision with the blocks and destroy them !----.... DONE .....

from blocks import Blocks
from ball import Ball
from paddle import Paddle
from screen import GamesScreen, GamesScreenSettings
from score_board import ScoreBoard 
from time import sleep

# creating the screen object
game_screen = GamesScreen()
# creating the paddle - player
paddle_player = Paddle((0,30-GamesScreenSettings.SCREEN_HEIGHT/2))
# creating blocks object 
blocks = Blocks()
total_posible_score = blocks.total_score()
# creating the ball 
ball = Ball((0,55-GamesScreenSettings.SCREEN_HEIGHT/2), paddle_player, blocks.list_of_blocks)
# creating scoreboards
# for lives
scoreboard_lives = ScoreBoard(
    (100-GamesScreenSettings.SCREEN_WIDTH/2,GamesScreenSettings.SCREEN_HEIGHT/2-60),
    "Lives",
    init_value=3)
# for score
scoreboard_score = ScoreBoard(
    (GamesScreenSettings.SCREEN_WIDTH/2-130,GamesScreenSettings.SCREEN_HEIGHT/2-60),
    "Score")

# activating event listeners
game_screen.screen.listen()

# adding functions to move the paddle
# to the left side
game_screen.screen.onkeypress(key='a',fun=paddle_player.paddle_move_left)
# to the right side
game_screen.screen.onkeypress(key='d',fun=paddle_player.paddle_move_right)


# main game loop
game_is_on = True

while game_is_on:
    # setting the default sleep time for tha animation
    sleep(GamesScreenSettings.SCREEN_TIME_SLEEP)
    # updating the screen , since tracer is off
    game_screen.screen.update()
    # updaiting the position of the ball
    ball.update_position(scoreboard_score)

    # checking end of game 
    if blocks.check_all_blocks_gone():
        # if game is finished create everything from sart
        ball.goto_start_positin()
        blocks.reset_all_blocks_to_origin()

    # checking if the ball is out of game
    # restart position or ending the game
    if not ball.check_if_ball_in_game():
        if scoreboard_lives.value_score_board > 1:
            scoreboard_lives.value_score_board -= 1
            ball.goto_start_positin()
        else:
            # GAME OVER - end of the game
            scoreboard_lives.text = "GAME OVER!! Lives"
            scoreboard_lives.goto(scoreboard_lives.pos_x_y[0]+90,scoreboard_lives.pos_x_y[1])
            scoreboard_lives.value_score_board = 0
            game_is_on = False
            game_screen.screen.update()


# wait for the scree to disapear after a click
game_screen.screen.exitonclick()