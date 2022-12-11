# class for managing the blocks
from turtle import Turtle
from screen import GamesScreenSettings

class BlocksSettings:
    """
    settings for the Blocks
    """
    BLOCK_COLOR_RED = 'red'
    BLOCK_COLOR_BLUE = 'blue'
    BLOCK_COLOR_GREEN = 'green'
    BLOCK_COLOR_YELLOW = 'yellow'
    BLOCKS_COLORS = [BLOCK_COLOR_RED, BLOCK_COLOR_BLUE, BLOCK_COLOR_GREEN, BLOCK_COLOR_YELLOW]
    BLOCK_WIDTH = int(60)
    BLOCK_DEFAULT_SIZE = int(20)
    BLOCK_STRETCH_WIDTH = BLOCK_WIDTH/BLOCK_DEFAULT_SIZE
    BLOCKS_WIDTH_PLAYGROUND = GamesScreenSettings.SCREEN_WIDTH - GamesScreenSettings.SCREEN_WALLS_WIDTH * 2

class Block(Turtle):
    """
    class for creating single block
    """
    def __init__(self, color: str, pos_x_y: tuple[int,int], lives=1, score = 10) -> None:
        """
        creating block object
        """
        super().__init__()
        self.color_init = color
        self.pos_x_y_init = pos_x_y
        self.lives_init = lives
        if color == BlocksSettings.BLOCK_COLOR_RED:
            self.score = 50
            self.lives_init += 1
        elif color == BlocksSettings.BLOCK_COLOR_BLUE:
            self.score = 40
            self.lives_init += 1
        elif color == BlocksSettings.BLOCK_COLOR_GREEN:
            self.score = 30
        elif color == BlocksSettings.BLOCK_COLOR_YELLOW:
            self.score = 20
        else:
            self.score = score

        self.reset_values_to_origin()

    def hit_the_block(self) -> None:
        """
        block takes a hit and decreasing lives
        reseting values whihc will delte the turtle object from the view
        """
        self.lives -= 1
        if self.lives <= 0:
            self.reset()
    
    def reset_values_to_origin(self) -> None:
        """
        reset the block values to initial
        """
        self.lives = self.lives_init
        self.shape('square')
        self.color(self.color_init)
        self.shapesize(stretch_wid=1, stretch_len=BlocksSettings.BLOCK_STRETCH_WIDTH)
        self.penup()
        self.goto(self.pos_x_y_init)


class Blocks():
    """
    class managing the all the Blocks layout
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.create_blocks()
        
    def create_blocks(self) -> None:
        """
        creating all the blocks
        """
        self.list_of_blocks: list[Block] = []
        gap_size_x = 3
        possible_number_x = BlocksSettings.BLOCKS_WIDTH_PLAYGROUND // (BlocksSettings.BLOCK_WIDTH + gap_size_x) 
        offset_x = int((BlocksSettings.BLOCKS_WIDTH_PLAYGROUND - possible_number_x * (BlocksSettings.BLOCK_WIDTH + gap_size_x))/2 )
        color_num = 0

        for pos_y in range(200,80,-25):
            for pos_x in range(
                offset_x - int(BlocksSettings.BLOCKS_WIDTH_PLAYGROUND/2-BlocksSettings.BLOCK_WIDTH/2),
                int(BlocksSettings.BLOCKS_WIDTH_PLAYGROUND/2-BlocksSettings.BLOCK_WIDTH/2),
                int(BlocksSettings.BLOCK_WIDTH+gap_size_x)): 

                if color_num >= len(BlocksSettings.BLOCKS_COLORS):
                    color_num = 2
                
                # adding and drawing the blocks
                self.list_of_blocks.append(
                    Block(
                        BlocksSettings.BLOCKS_COLORS[color_num],
                        (pos_x,pos_y))
                )

            # changing the color
            color_num += 1

    def reset_all_blocks_to_origin(self) -> None:
        """
        reseting all block to the origin
        """
        for block in self.list_of_blocks:
            block.reset_values_to_origin()

    def total_score(self) -> int:
        """
        returns the total possible score to obtain
        """
        score = 0
        for block in self.list_of_blocks:
            if block.lives > 0:
                score += block.score

        return score

    def check_all_blocks_gone(self) -> bool: 
        """
        checks if any blocks are still alive / not destroyed
        returns false if they are any left
        returns true if there all blocks are destroyed
        """
        for block in self.list_of_blocks:
            if block.lives > 0:
                return False
        return True