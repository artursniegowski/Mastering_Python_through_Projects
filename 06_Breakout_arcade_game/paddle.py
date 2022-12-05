# class for managing the Paddle
from turtle import Turtle
from screen import GamesScreenSettings

class PaddleSettings:
    """
    Paddle settings
    """
    # paddle size - zero is in the middle of the paddle
    PADDLE_WIDTH = int(100) 
    PADDLE_HEIGHT = int(20) # 20 is the default size for the square
    PADDLE_COLOR = 'white'
    # basic size is 20x20 pixels
    PADDLE_SHAPE = 'square'
    PADDLE_DEFAULT_SIZE = int(20)
    PADDLE_MOVE_DISTANCE = int(10)


class Paddle(Turtle):
    """
    class for managing the paddle
    """
    def __init__(self, start_pos_x_y: tuple[int,int]) -> None:
        """
        creating the paddle object
        """
        super().__init__()
        stretch_width = PaddleSettings.PADDLE_WIDTH / PaddleSettings.PADDLE_DEFAULT_SIZE
        # default shape 20x20 pixels
        self.shape(PaddleSettings.PADDLE_SHAPE)
        self.color(PaddleSettings.PADDLE_COLOR)
        self.shapesize(stretch_wid=1, stretch_len=stretch_width)
        self.penup()
        self.init_pos = start_pos_x_y
        self.goto(self.init_pos)

    def paddle_move_left(self) -> None:
        """
        moving the paddle to the left side
        taking into account the left wall
        """
        if (self.xcor() - PaddleSettings.PADDLE_MOVE_DISTANCE - PaddleSettings.PADDLE_WIDTH/2) >= \
            GamesScreenSettings.SCREEN_WALLS_WIDTH - GamesScreenSettings.SCREEN_WIDTH/2:
            self.setx(
                self.xcor() - PaddleSettings.PADDLE_MOVE_DISTANCE
            )
   
    def paddle_move_right(self) -> None:
        """
        moving the paddle to the right side
        taking into account the right wall
        """
        if (self.xcor() + PaddleSettings.PADDLE_MOVE_DISTANCE + PaddleSettings.PADDLE_WIDTH/2) <= \
            -GamesScreenSettings.SCREEN_WALLS_WIDTH + GamesScreenSettings.SCREEN_WIDTH/2:
            self.setx(
                self.xcor() + PaddleSettings.PADDLE_MOVE_DISTANCE
            )

    def goto_start_positin(self) -> None:
        """
        move the paddle to the start position
        """
        self.setpos(self.init_pos)