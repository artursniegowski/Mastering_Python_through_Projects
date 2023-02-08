# addiontnal functions for managing the game

from alien_ship import Alien_Ship
from controls import Control
from Display_score import Scores
from my_settings import MySettings
import pygame
from pygame.sprite import Group
from read_write import read_write_game
from rocket import Rocket
from space_ship import SpaceShip
from statistics_game import Statistics


def add_rocket(space_ship : SpaceShip , rockets : Group , \
    screen : pygame.Surface, my_settings : MySettings) -> None :
    """Creating rockets"""
    if len(rockets) < my_settings.rocket_capacity:
        rocket = Rocket(my_settings,screen,space_ship)
        rockets.add(rocket)

def max_alien_ships_x(my_settings : MySettings, alien_ship: Alien_Ship) -> int:
    """Calculating max number of ships (horizontally)"""
    Max_aliens_ships_x = int((my_settings.screen_width / \
        alien_ship.alien_ship_rect.width) /my_settings.space_factor_x)

    return Max_aliens_ships_x

def max_alien_ships_y(my_settings : MySettings, alien_ship: Alien_Ship) -> int:
    """Calculating max number of ships (vertically) """
    filling_density = 0.4
    Max_aliens_ships_y = int((my_settings.screen_height / \
        alien_ship.alien_ship_rect.height) /my_settings.space_factor_y * \
            filling_density)

    return Max_aliens_ships_y

def position_alien_ships_shiftig(max_aliens_ships_x : int, \
    max_aliens_ships_y : int, my_settings : MySettings, screen :pygame.Surface,\
        alien_ships: Group) -> None:
    """logic for the position of each alien ship, to determine the location
        of x and y coordinates on the screen"""
            # Positioning the alien ships
    for alien_ship_number_y in range(max_aliens_ships_y):  
        for alien_ship_number_x in range(max_aliens_ships_x):
            alien_ship = Alien_Ship(my_settings,screen)
            pos_x = alien_ship.alien_ship_rect.width/2 + \
                my_settings.space_factor_x * alien_ship.alien_ship_rect.width *\
                     alien_ship_number_x 
            alien_ship.alien_ship_rect.x = pos_x
            pos_y = alien_ship.alien_ship_rect.height/2 + \
                my_settings.space_factor_y * alien_ship.alien_ship_rect.height*\
                     alien_ship_number_y 
            alien_ship.alien_ship_rect.y = pos_y +50
            alien_ships.add(alien_ship)

def position_alien_ships(my_settings : MySettings, screen :pygame.Surface, \
    alien_ships: Group) -> None:
    """Create and position all of the alien ships"""
    # Getting the dimensions from an alien ship
    alien_ship = Alien_Ship(my_settings,screen)
    Max_aliens_ships_x = max_alien_ships_x(my_settings,alien_ship)
    Max_aliens_ships_y = max_alien_ships_y(my_settings,alien_ship)

    # Positioning the alien ships
    position_alien_ships_shiftig(Max_aliens_ships_x,Max_aliens_ships_y,\
        my_settings,screen,alien_ships)

def update_high_score_file(file_high_score : int, game_stats : Statistics) \
    -> None:
    """Methode used for updating the high score from file"""
    if file_high_score > game_stats.high_score:
        game_stats.high_score = file_high_score


def check_in_range_start_button(read_write_game_stats : read_write_game, \
    display_scores: Scores, game_stats : Statistics,\
    my_settings : MySettings, screen : pygame.Surface, start_button : Control,\
    space_ship : SpaceShip ,alien_ships : Group ,rockets : Group, \
        mouse_x : int, mouse_y : int) -> None :
    """checking if the usser pressed the button start"""
    if start_button.rect.collidepoint(mouse_x,mouse_y) and \
        not game_stats.game_on:
        # reseting at the start of the game
        game_stats.init_statistics()
        # Reset the game settings
        my_settings.init_settings_start_game()
        game_stats.game_on = True

        # Empty everything
        alien_ships.empty()
        rockets.empty()

        # reading the high score from the file
        update_high_score_file(read_write_game_stats.return_high_score(),game_stats)

        # Display staring values for high scores
        display_scores.update_high_score()
        # Display staring values scores
        display_scores.update_score()
        # update level
        display_scores.update_level()
        # update lives
        display_scores.update_lives()
        # draw ships lives
        display_scores.draw_ships_lives()

        # Create the game 
        position_alien_ships(my_settings,screen,alien_ships)
        space_ship.starting_pos()

def check_if_mouse_above_button(start_button : Control, mouse_x : int,\
     mouse_y : int) -> None:
    """Managing the start button if the mouse hover above it"""
    if start_button.rect.collidepoint(mouse_x,mouse_y):
        start_button.hover = True
    else:
        start_button.hover = False

def remove_all_rockets(rockets : Group , removing_all : bool = False) -> None:
    """Removing all existing rockets"""
    for rocket in rockets:
        if rocket.rocket_image_rect.bottom <= 0 or removing_all:
            rockets.remove(rocket)

def update_high_score(game_stats : Statistics, display_score : Scores) -> None:
    """Methode used for updating the high score"""

    if game_stats.total_score > game_stats.high_score:
        game_stats.high_score = game_stats.total_score
        # updateing the score on the main view
        display_score.update_high_score()

def save_to_file_high_score(read_write_game_stats : read_write_game, \
    game_stats : Statistics) -> None:
    """Saving to file the high score if it is higher than the current high score
        in the file"""
    high_score_file = read_write_game_stats.return_high_score()
    if game_stats.high_score > high_score_file:
        read_write_game_stats.write_high_score(game_stats.high_score)

def ending_life_ship(read_write_game_stats : read_write_game, \
    my_settings : MySettings, game_stats : Statistics, \
    display_score : Scores, screen : pygame.Surface, space_ship : SpaceShip, \
    alien_ships : Group, rockets : Group) -> None :
    """Logic when collison wiht an alien ship occurs"""
    # Decreassing lifes of eh player
    game_stats.ships_lives -= 1

    # updating lives on the screen
    display_score.update_lives()
    # updating the number of ships drawn
    display_score.draw_ships_lives()

    if game_stats.ships_lives > 0:
        # restart the game 
        alien_ships.empty()
        rockets.empty()

        # create alien ships from starting possiton
        position_alien_ships(my_settings,screen,alien_ships)
        # initila position for the space ship
        space_ship.starting_pos()
    else:
        # updating high score if the current score is higher that the actual 
        # high score
        update_high_score(game_stats,display_score)
        # write high score to the json file for future use
        save_to_file_high_score(read_write_game_stats,game_stats)

        game_stats.game_on = False

def if_allien_ship_reached_bottom(read_write_game_stats : read_write_game, \
    my_settings : MySettings, game_stats : Statistics, \
    display_score : Scores, screen : pygame.Surface, space_ship : SpaceShip, \
    alien_ships : Group, rockets : Group) -> None :
        """Checking if any alien ships reached the bottom of the screen"""
        screen_rect = screen.get_rect()
        for alien in alien_ships:
            if alien.rect.bottom >= screen_rect.bottom:
                # same as player loosing
                ending_life_ship(read_write_game_stats,my_settings,game_stats, \
                    display_score,screen,space_ship,alien_ships,rockets)
                #ending the game
                break

def check_alien_ship_on_the_edege(my_settings : MySettings, alien_ships : Group) -> None:
    """Checking if a alien ship is on the edge and changing the
        direction they move"""
    for alien_ship in alien_ships:
        if alien_ship.check_vertical_right_border():
            my_settings.direction_alien_RIGHT = False
            drop_alien_ships(my_settings,alien_ships)
            break
        if alien_ship.check_vertical_left_border():
            my_settings.direction_alien_RIGHT = True
            drop_alien_ships(my_settings,alien_ships)
            break

def drop_alien_ships(my_settings : MySettings, alien_ships : Group) -> None:
    """Droping the alien ships"""
    for alien_ship in alien_ships:
        alien_ship.alien_ship_rect.y += my_settings.alien_ships_speed_droping
