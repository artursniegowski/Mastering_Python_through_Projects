# class for managing the ball
from turtle import Turtle
from screen import GamesScreenSettings
from math import sin, cos, atan2, pi
from paddle import Paddle, PaddleSettings
from time import sleep
from blocks import Block, BlocksSettings
from score_board import ScoreBoard
import random

class BallSettings:
    """
    class for managing the class ball settings
    """
    #BALL_WIDTH = 20
    #BALL_HEIGHT = 20
    BALL_RADIUS = 10.0
    BALL_COLOR = 'white'
    # basic size 20x20 pixels
    BALL_SHAPE = 'circle'
    BALL_VELOCITY = 2.0
    #  pi = 180 degrees
    BALL_START_ANGLE = pi/2+pi/10

class Ball(Turtle):
    """
    class for managing the ball
    """
    def __init__(self, start_pos_x_y: tuple[int,int], paddle: Paddle, list_of_blocks: list[Block]) -> None:
        """
        creating the ball object
        """
        super().__init__()
        self.shape(BallSettings.BALL_SHAPE)
        self.color(BallSettings.BALL_COLOR)
        self.penup()
        self.init_pos = start_pos_x_y
        self.goto(self.init_pos)
        self.time_step_simulation = GamesScreenSettings.SCREEN_TIME_SLEEP
        self.velocity = BallSettings.BALL_VELOCITY
        self.angle = BallSettings.BALL_START_ANGLE
        self.top_line_y = GamesScreenSettings.SCREEN_HEIGHT/2 - GamesScreenSettings.SCREEN_WALLS_WIDTH 
        self.left_line_x = GamesScreenSettings.SCREEN_WALLS_WIDTH-GamesScreenSettings.SCREEN_WIDTH/2
        self.rigth_line_x = -GamesScreenSettings.SCREEN_WALLS_WIDTH+GamesScreenSettings.SCREEN_WIDTH/2
        # tuple[x_pos,y_pos]
        self.bounce_pos = (0,55-GamesScreenSettings.SCREEN_HEIGHT/2)
        # paddle position
        self.paddle = paddle
        # list of blocks
        self.list_of_blocks = list_of_blocks

    def update_position(self, score_board: ScoreBoard) -> None:
        """
        update the position of the ball
        """
        # check in the ball is the game 
        if self.ycor() > 5-GamesScreenSettings.SCREEN_HEIGHT/2 :
            self.setx(
                self.xcor() + self.velocity * cos(self.angle)
            )
            self.sety(
                self.ycor() + self.velocity * sin(self.angle)
            )

            next_pos_y_plus = (self.ycor() + BallSettings.BALL_RADIUS + (self.velocity) * sin(self.angle))
            next_pos_y_minus = (self.ycor() - BallSettings.BALL_RADIUS + (self.velocity) * sin(self.angle))
            next_pos_x_plus = (self.xcor() + BallSettings.BALL_RADIUS + (self.velocity) * cos(self.angle) )
            next_pos_x_minus = (self.xcor() - BallSettings.BALL_RADIUS + (self.velocity) * cos(self.angle) )
            
            self._check_for_wall(next_pos_x_minus, next_pos_x_plus, next_pos_y_plus)
            self._check_for_paddle(next_pos_x_minus, next_pos_x_plus, next_pos_y_minus, self.paddle)
            if self.list_of_blocks:
                self._check_for_block_collision(self.list_of_blocks, next_pos_y_plus,\
                     next_pos_y_minus, next_pos_x_plus, next_pos_x_minus, score_board)



    def _check_for_block_collision(self, list_of_blocks: list[Block], \
        next_ball_pos_y_max: float, next_ball_pos_y_min: float, \
            next_ball_pos_x_max:float, next_ball_pos_x_min: float, \
                score_board: ScoreBoard) -> None:
        """
        checks if the ball hit a block
        if a block was hit or detroyed it will update the score
        """
        tolerance = 5
        for block in list_of_blocks:
            if block.lives > 0:               
                # BlocksSettings.BLOCK_WIDTH = int(60)
                # BlocksSettings.BLOCK_DEFAULT_SIZE = int(20)
                block_center_x, block_center_y = block.pos()
                # left side
                block_min_x = int(block_center_x - BlocksSettings.BLOCK_DEFAULT_SIZE/2)
                # right side
                block_max_x = int(block_center_x + BlocksSettings.BLOCK_DEFAULT_SIZE/2)
                # bottom side
                block_min_y = int(block_center_y - BlocksSettings.BLOCK_WIDTH/2)
                # top side
                block_max_y = int(block_center_y + BlocksSettings.BLOCK_WIDTH/2)

                # checking - ball hitting the bottom side of the block
                if  block_min_y - tolerance < int(next_ball_pos_y_min) < block_min_y + 10 and \
                    self.distance(block) < 43 :
                        self.angle = -self.angle
                        self.bounce_pos = self.pos()    
                        block.hit_the_block()
                        # updates the score board
                        score_board.value_score_board += block.score
                # checking - ball hitting the top side of the block
                elif  block_max_y - 10 < int(next_ball_pos_y_max) < block_max_y + tolerance and \
                    self.distance(block) < 43 :
                        self.angle = -self.angle
                        self.bounce_pos = self.pos()    
                        block.hit_the_block()
                        # updates the score board
                        score_board.value_score_board += block.score
                # checking - ball hitting the left side of the block
                # elif  block_max_x < int(next_ball_pos_x_min) < block_max_x + tolerance and \
                #     self.distance(block) < 42 :
                #         self.angle = pi - atan2(self.ycor()-self.bounce_pos[1],self.xcor()- self.bounce_pos[0])
                #         self.bounce_pos = self.pos()    
                #         block.hit_the_block()
                # # checking - ball hitting the right side of the block
                # elif  block_min_x < int(next_ball_pos_x_max) < block_min_x + tolerance and \
                #     self.distance(block) < 42 :
                #         self.angle = pi - atan2(self.ycor()-self.bounce_pos[1],self.xcor()- self.bounce_pos[0])
                #         self.bounce_pos = self.pos()    
                #         block.hit_the_block()


    def _check_for_wall(self, next_pos_x_min: float, next_pos_x_max: float, next_pos_y_max: float) -> None:
        """
        checks if the ball is in contact with the wall
        """
        # top side
        if next_pos_y_max > self.top_line_y:
            self.angle = -self.angle + random.random()/8  
            self.bounce_pos = self.pos()   
        # rigth side
        elif next_pos_x_max > self.rigth_line_x:
            self.angle = pi - atan2(self.ycor()-self.bounce_pos[1],self.xcor()- self.bounce_pos[0])
            self.bounce_pos = self.pos()
        # left side
        elif next_pos_x_min < self.left_line_x:
            self.angle = pi - atan2(self.ycor()-self.bounce_pos[1],self.xcor()- self.bounce_pos[0])
            self.bounce_pos = self.pos()

    def _check_for_paddle(self, next_pos_x_min: float, next_pos_x_max: float, next_pos_y_min: float, paddle: Paddle) -> None:
        """
        checks if the ball is in contact with the paddle
        """ 
        paddle_position = paddle.pos()

        if float(paddle_position[1]) + PaddleSettings.PADDLE_HEIGHT/4 < next_pos_y_min < float(paddle_position[1]) + PaddleSettings.PADDLE_HEIGHT/2:
            # left side of the paddle
            if float(paddle_position[0]) - PaddleSettings.PADDLE_WIDTH/2 < next_pos_x_min + 15 < float(paddle_position[0]) - PaddleSettings.PADDLE_WIDTH/5:
                self.angle = -self.angle - self.angle/12 + random.random()/8
                self.bounce_pos = self.pos()
            # middle of the paddle 
            elif float(paddle_position[0]) - PaddleSettings.PADDLE_WIDTH/5 <= next_pos_x_min + 15 <= float(paddle_position[0]) + PaddleSettings.PADDLE_WIDTH/5:
                self.angle = -self.angle + random.random()/8
                self.bounce_pos = self.pos()
            # rigth side of the paddle
            elif float(paddle_position[0]) + PaddleSettings.PADDLE_WIDTH/5 < next_pos_x_min + 15 < float(paddle_position[0]) + PaddleSettings.PADDLE_WIDTH/2:
                self.angle = -self.angle + self.angle/12 + random.random()/8
                self.bounce_pos = self.pos()

    def check_if_ball_in_game(self) -> bool:
        """
        checking if the ball is in the play range,
        game over check ,
        returns true if it is , and returns false if the ball is not anymore in game
        """
        if self.ycor() > 5-GamesScreenSettings.SCREEN_HEIGHT/2:
            return True
        else:
            # let the user know it is over - time to process the information
            sleep(0.3)
            return False    

    def goto_start_positin(self) -> None:
        """
        move the ball to the start position
        """
        # reset the start angle
        self.angle = BallSettings.BALL_START_ANGLE
        self.setpos(self.init_pos)
        self.bounce_pos = self.pos()