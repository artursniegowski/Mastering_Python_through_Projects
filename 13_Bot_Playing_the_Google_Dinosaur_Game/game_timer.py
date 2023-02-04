# class for defining the end of the game
import time 

class TimeOut:
    """class managing the current play time 
    """
    def __init__(self, mins: int = 5) -> None:
        """mins - is the amount in mins for the game to be active
        """
        self.play_time = mins
        self.current_time = time.time()

    def check_if_play_time_over(self) -> bool:
        """checking if play time is over
        returns True if play time is over and returns false if play time is not over yet
        """
        return time.time() > (self.current_time+60*self.play_time)

    @property
    def play_time(self):
        """getter for the play time
        """
        return self.__play_time

    @play_time.setter
    def play_time(self,value):
        """setting the play_time value
        """
        assert isinstance(value, int), "Error: Value has to be an integer"
        assert value>0, "Error: Value has to greater than 1"

        self.__play_time = value