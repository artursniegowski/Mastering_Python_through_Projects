# class managing the Alien space ship
from create_path import return_path
from my_settings import MySettings
import pygame
from pygame.sprite import Sprite

class Alien_Ship(Sprite):
    """Class for the alien spaceship"""

    def __init__(self,  my_settings: MySettings , screen: pygame.Surface ) -> None:
        super().__init__()

        self.screen = screen
        self.my_settings = my_settings

        # Load the alien ship
        self.alien_ship = pygame.image.load(return_path(self.my_settings.subfolder_name_image,self.my_settings.name_alien_ship))
        self.alien_ship.convert()
        # reseize the alien space ship loaded from the file
        self.alien_ship = pygame.transform.rotozoom(self.alien_ship, 0, 0.1)

        self.alien_ship_rect = self.alien_ship.get_rect()
        self.rect =  self.alien_ship_rect
        self.screen_rect = self.screen.get_rect()
        
        # Init position
        self.x_increment = 0.0

    def update(self) -> None:
        """Updates the position of alien ship"""
        #pass
        self.x_increment += self.my_settings.alien_ships_speed
        if self.x_increment >= 1.0:
            if self.my_settings.direction_alien_RIGHT:
                self.alien_ship_rect.x += 1
            elif not self.my_settings.direction_alien_RIGHT:
                self.alien_ship_rect.x -= 1

            self.x_increment = 0.0


    def check_vertical_right_border(self) -> bool:
        """If one of the allien ships is on the edge of right border"""
        if self.alien_ship_rect.right >= self.screen_rect.right:
            return True

    def check_vertical_left_border(self) -> bool:
        """If one of the allien ships is on the edge of left border"""
        if self.alien_ship_rect.left <= 0.0:
            return True

    def draw_alien_ship(self):
        """Draw the alien ship at its current location"""
        self.screen.blit(self.alien_ship, self.alien_ship_rect)