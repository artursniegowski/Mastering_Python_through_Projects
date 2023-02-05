# class managing the rockets fired form the ship

from my_settings import MySettings
import pygame
from pygame.sprite import Sprite
from space_ship import SpaceShip

class Rocket(Sprite):
    """Class to manage the rockets shot from the ship"""

    # Constructor. Pass in the color of the block
    # and its x,y postion
    def __init__(self, my_settings: MySettings, screen: pygame.Surface, ship: SpaceShip) -> None:
        super().__init__()

        self.screen = screen
        # Create an image of the block
        self.rocket_image = pygame.Surface([my_settings.rocket_width, \
            my_settings.rocket_height])
        self.rocket_image.fill(my_settings.rocket_color_RGB)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x 
        # and rect.y
        self.rocket_image_rect = self.rocket_image.get_rect()
        self.rect =  self.rocket_image_rect
        
        # Set starting postion above the ship
        self.rocket_image_rect.centerx = ship.ship_rect.centerx
        self.rocket_image_rect.top = ship.ship_rect.top

        # Init position
        self.rocket_pos_y = self.rocket_image_rect.y
        # Rocket speed
        self.rocket_speed = my_settings.rocket_speed

    def update(self) -> None:
        """Updating the position of the rocket"""
        # Updating the fractional value
        self.rocket_pos_y -= self.rocket_speed
        # Updating the Rect position of the rocket
        self.rocket_image_rect.y = self.rocket_pos_y

    def draw_rocket(self) -> None:
        """Draw the rocket at its current location"""
        self.screen.blit(self.rocket_image, self.rocket_image_rect)