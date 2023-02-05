# class managing the players spaceship

from create_path import return_path
from my_settings import MySettings
import pygame
from pygame.sprite import Sprite

class SpaceShip(Sprite):
    """class managing the players space ship
    """
    
    def __init__(self, my_settings: MySettings , screen: pygame.Surface, \
        zoom_img : float) -> None:
        """Initialize the ship and set its starting position"""
        super().__init__()
        self.screen = screen
        self.my_settings = my_settings
        self.zoom_img = zoom_img
        # Load the ship
        self.ship = pygame.image.load(return_path(self.my_settings.subfolder_name_image,self.my_settings.name_main_ship))
        self.ship.convert()
        self.ship = pygame.transform.rotozoom(self.ship, 0, self.zoom_img)

        # for Sprite
        self.image = self.ship

        self.ship_rect = self.ship.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect = self.ship_rect

        # Start each new ship at the bottom center of the screen
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom

        # Initial position
        self.center = (self.ship_rect.centerx)

        # Directions to move
        self.moving_right = False
        self.moving_left = False

    def update_pos(self):
        """Update the spaceship's position based on the flag"""
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.center += (self.my_settings.ship_speed)
        if self.moving_left and self.ship_rect.left > 0:
            self.center -= (self.my_settings.ship_speed)
        
        # Updating the position
        self.ship_rect.centerx = self.center 

    def starting_pos(self):
        """initial position for the space ship"""
        self.center = self.screen_rect.centerx

    def draw_ship(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.ship, self.ship_rect)