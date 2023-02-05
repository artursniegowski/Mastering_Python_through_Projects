# class for managing the screen settings
from turtle import Screen, Turtle

class GamesScreenSettings:
    """
    Basic screen settings
    """
    SCREEN_WIDTH = int(800)
    SCREEN_HEIGHT = int(600)
    SCREEN_BACKGROUNDCOLOR = 'black'
    SCREEN_TITLE = 'BREAKOUT'
    SCREEN_TRACER_VALUE = int(0) # 0 for turning tracer off ,
                            # inorder to control animation manually
    SCREEN_TIME_SLEEP = 0.000001
    # walls on the screen
    SCREEN_WALLS_WIDTH = int(20)
    SCREEN_WALLS_COLOR = 'grey'
    # parameters to center elements
    # CURSOR_SIZE = 20
    # BORDER_SIZE = 2
    # CHROME_SIZE = 9


class GamesScreen():
    """
    creating screen object and its properties
    """
    def __init__(self) -> None:
        # creating screen view
        self.screen = Screen()
        self.screen.setup(width=GamesScreenSettings.SCREEN_WIDTH,\
            height=GamesScreenSettings.SCREEN_HEIGHT)
        self.screen.bgcolor(GamesScreenSettings.SCREEN_BACKGROUNDCOLOR)
        self.screen.title(GamesScreenSettings.SCREEN_TITLE)
        # # turn off tracer # so we control manually when to update the 
        # # screen with update function
        self.screen.tracer(GamesScreenSettings.SCREEN_TRACER_VALUE)
        # disable resizing
        self.screen.cv._rootwindow.resizable(False, False)

        # registering walls shape
        self.register_walls_polly_shapes("walls", width=GamesScreenSettings.SCREEN_WALLS_WIDTH)
        # adding walls shape
        # top wall
        self.create_wall("walls",(0,int(GamesScreenSettings.SCREEN_HEIGHT)/2), direction=90)
        # right wall
        self.create_wall("walls",(int(GamesScreenSettings.SCREEN_WIDTH)/2,0), direction=180)
        # left wall
        self.create_wall("walls",(-int(GamesScreenSettings.SCREEN_WIDTH)/2,0), direction=180)

    def register_walls_polly_shapes(self, shape_name: str, width: int) -> None:
        """
        adding a new polly shape witht the given shape_name to the Screen object,
        later it can be used to draw the walls
        """
        # creating the object points
        P1 = (int(GamesScreenSettings.SCREEN_WIDTH)/2,width)
        P2 = (int(GamesScreenSettings.SCREEN_WIDTH)/2,-width)
        P3 = (-int(GamesScreenSettings.SCREEN_WIDTH)/2,-width)
        P4 = (-int(GamesScreenSettings.SCREEN_WIDTH)/2,width)

        # adding the shape 
        self.screen.register_shape(shape_name,((P1),(P2),(P3),(P4)))
        
    def create_wall(self, shape_name: str, init_pos_x_y: tuple[int,int], direction: int = 0) -> None:
        """
        creating the walls
        """
        wall = Turtle(shape_name)
        wall.penup()
        wall.speed('fastest')
        wall.setheading(direction)
        wall.color(GamesScreenSettings.SCREEN_WALLS_COLOR)
        wall.goto(init_pos_x_y)