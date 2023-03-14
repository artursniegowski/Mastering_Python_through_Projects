from chrom_driver_path import CHROME_DRIVER_PATH
from game_bot import GameBot
from game_timer import TimeOut

# craeting a time out for the game - object
# mins - is the argument defining how many minutes will the bot play the game !
game_time = TimeOut(mins=3)

# creating the game_bot object
game_bot = GameBot(CHROME_DRIVER_PATH)

# gettign ready the bot - opening browser and geting the initial size and windowd to monitor
game_bot.wait_for_bot_read()


while True:
    # checking if the game should still be going
    if game_time.check_if_play_time_over():
        print("Time is up for the game bot.")
        game_bot.close_the_game()
        break
    
    # checking for the obstacles
    game_bot.check_for_obstacles()
