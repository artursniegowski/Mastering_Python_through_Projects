# the main part of the game - putting everything together 
from controls import Control
from Display_score import Scores
import functions as game_func
from my_settings import MySettings
import pygame
from read_write import read_write_game
from space_ship import SpaceShip
from statistics_game import Statistics

# function for starting the game
def game_on():
    # Main thread - init Pygame , screen etc.
    pygame.init()
    my_settings = MySettings()
    screen = pygame.display.set_mode((my_settings.screen_width,my_settings.screen_height))
    pygame.display.set_caption(my_settings.caption)
    
    # Creating the play button
    play_button = Control(my_settings,screen,my_settings.start_button_caption)
    # Instance to store game statistics
    game_stats = Statistics(my_settings)
    # creaing the score on the main view
    display_score = Scores(my_settings,screen,game_stats)
    # Make a spaceship
    space_ship = SpaceShip(my_settings,screen,0.2)
    # Creating a group of rockets
    rockets = pygame.sprite.Group()
    # Creating alien ships
    alien_ships = pygame.sprite.Group()
    # Position all the alien ships
    game_func.position_alien_ships(my_settings,screen,alien_ships)
    # managing and storing data - game stats to a file
    read_write = read_write_game(my_settings)
    
    # run window
    while True: 

        # Watch for keyboard and mouse events
        game_func.check_events(read_write,display_score,my_settings,screen,\
            game_stats,play_button,space_ship,rockets,alien_ships)
      
        # Checking if the players has still lives left
        if game_stats.game_on:
            space_ship.update_pos()
            game_func.update_rockets(my_settings,screen,alien_ships,rockets,\
                game_stats,display_score)
            game_func.update_alien_ships(read_write,my_settings,game_stats,\
                display_score,screen,space_ship,alien_ships,rockets)

        # updatign screen 
        game_func.update_view(my_settings,game_stats,screen,display_score,\
            space_ship,rockets,alien_ships,play_button)

        
# Start the game
game_on()