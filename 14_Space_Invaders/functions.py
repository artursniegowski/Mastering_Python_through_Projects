# main functions of the game

from additional_functions import *
from controls import Control
from Display_score import Scores
from my_settings import MySettings
import pygame
from pygame.sprite import Group
from read_write import read_write_game
from space_ship import SpaceShip
from statistics_game import Statistics
import sys

def check_events_keydown(event: pygame.event, my_settings : MySettings,\
     screen : pygame.Surface, space_ship: SpaceShip,\
          rockets :  Group ) -> None:
    """Events - key down"""
    if event.key == pygame.K_ESCAPE:
        # End the game
        pygame.quit()
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        # Start movig to the right
        space_ship.moving_right = True 
    elif event.key == pygame.K_LEFT:
        # Start movig to the left
        space_ship.moving_left = True 
    elif event.key == pygame.K_SPACE:
        # New rocket - hit spacebar
        add_rocket(space_ship,rockets,screen,my_settings)

def check_events_keyup(event: pygame.event, space_ship: SpaceShip) -> None:
    """Events - key up"""
    if event.key == pygame.K_RIGHT:
        # Stop movig to the right
        space_ship.moving_right = False 
    elif event.key == pygame.K_LEFT:
        # Stop movig to the left
        space_ship.moving_left = False 

def check_events(read_write_game_stats : read_write_game, \
    display_scores : Scores,my_settings : MySettings, screen : pygame.Surface, \
    game_stats : Statistics, start_button : Control, space_ship : SpaceShip, \
    rockets : Group, alien_ships : Group) -> None:
    """Watch for keyboard and mouse events"""
    for event in pygame.event.get():
        # Exiting the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Moving the ship
        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event, my_settings, screen, space_ship, \
                rockets)
        
        # Start button for the game
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            check_in_range_start_button(read_write_game_stats,display_scores,\
                game_stats,my_settings,screen, start_button,space_ship,\
                    alien_ships,rockets,mouse_x,mouse_y)

        elif event.type == pygame.MOUSEMOTION:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            check_if_mouse_above_button(start_button,mouse_x,mouse_y)

        elif event.type == pygame.KEYUP:
            check_events_keyup(event, space_ship)

def update_rockets(my_settings : MySettings, screen :pygame.Surface, \
    alien_ships : Group ,rockets : Group, game_stats : Statistics, \
        display_score : Scores) -> None:
    """Encapsulating the functions managing rockets"""
    
    # Updating rockets position
    rockets.update()
    # checking for contact betwen rockets and alien_ships
    contact_alien_ship_rocket = pygame.sprite.groupcollide(rockets,alien_ships,\
        True,True)

    if contact_alien_ship_rocket:
        for alien_ships in contact_alien_ship_rocket.values():
            for alien in alien_ships:
                # addin points for destroying an alien ship
                game_stats.total_score += my_settings.alien_ship_points
                # updating main score
                display_score.update_score()
                # updating high score
                update_high_score(game_stats,display_score)

    # Erasing rockets that are out of reach
    # remove rockets that went pass the screen
    remove_all_rockets(rockets)
    
    # When all alien ships were shoot down we start over -next level
    if(len(alien_ships)==0):
        
        rockets.empty()
        
        # addin points for finihsing the level
        game_stats.total_score += my_settings.next_level_points
        display_score.update_score()
        
        # increasing the difficulty
        my_settings.next_level()

        position_alien_ships(my_settings,screen,alien_ships)

        # updating level
        game_stats.level += 1
        display_score.update_level()
    
def update_alien_ships(read_write_game_stats : read_write_game, \
    my_settings : MySettings, game_stats : Statistics, \
    display_score : Scores, screen : pygame.Surface, space_ship : SpaceShip,\
    alien_ships : Group, rockets : Group) -> None :
    """Move all the allien ships"""
    alien_ships.update()

    # Chcking if the alien ships reached the our ship
    if pygame.sprite.spritecollideany(space_ship,alien_ships):
        ending_life_ship(read_write_game_stats,my_settings,game_stats, \
            display_score,screen,space_ship,alien_ships,rockets)

    if_allien_ship_reached_bottom(read_write_game_stats, \
        my_settings,game_stats,display_score,screen,space_ship, \
            alien_ships,rockets)

def update_view(my_settings : MySettings, game_stats : Statistics, \
    screen : pygame.Surface, display_score : Scores, space_ship : SpaceShip, \
        rockets : Group, alien_ships : Group, button : Control) -> None:
        """Update view on tha main screen"""
        # Changing surface color
        screen.fill(my_settings.background_color)
        space_ship.draw_ship()       
        # Draw all the rockets
        for rocket in rockets:
            rocket.draw_rocket()
        # Drawing Alien ships
        for alien_ship in alien_ships:
            alien_ship.draw_alien_ship()
        # changing the sites the alien ships are moving
        check_alien_ship_on_the_edege(my_settings,alien_ships)
        # drawing the score on the mian view
        display_score.draw_score()
        # Draw the start button if the game is not active
        if not game_stats.game_on:
            button.draw_button()
        # Update the screen
        pygame.display.flip()
