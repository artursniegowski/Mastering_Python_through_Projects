# class for managing the scoreboard
from turtle import Turtle

class ScoreBoardSettings:
    """
    settings for scoreboard
    """
    SCOREBOARD_ALIGMENT = 'center'
    SCOREBOARD_FONT = ('Courier',20,'normal')
    SCOREBOARD_COLOR = 'white'


class ScoreBoard(Turtle):
    """
    class to manage the score on the screen
    """
    def __init__(self, pos_x_y: tuple[int,int], text: str, init_value: int = 0) -> None:
        super().__init__()
        self.text = text
        self.message = lambda text, value: f"{text}: {value}"
        self.pos_x_y = pos_x_y
        self.penup()
        self.color(ScoreBoardSettings.SCOREBOARD_COLOR)
        self.goto(self.pos_x_y)
        self.hideturtle()

        # properties - init value
        self.value_score_board = init_value
        
    @property
    def value_score_board(self):
        return self.__value_score_board

    @value_score_board.setter
    def value_score_board(self, value):
        if value < 0:
            raise ValueError("ERROR: value_score_board cant be smaller than 0!!")
        self.__value_score_board = value
        # always after setting the value 
        # it will be redrawn
        self.clear()
        self.draw_score_board()

    def draw_score_board(self) -> None:
        """
        draw the score on the screen
        """
        self.write(
            self.message(self.text,self.value_score_board), 
            align = ScoreBoardSettings.SCOREBOARD_ALIGMENT,
            font=ScoreBoardSettings.SCOREBOARD_FONT)