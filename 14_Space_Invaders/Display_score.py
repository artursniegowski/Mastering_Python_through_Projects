# class managing the score of the game
from my_settings import MySettings
import pygame
from space_ship import SpaceShip
from statistics_game import Statistics

class Scores:
    """A class to show all the scores"""

    def __init__(self, my_settings : MySettings, screen : pygame.Surface, \
        game_stats : Statistics) -> None:
        """initialize all the scoring atributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.my_settings = my_settings
        self.game_stats = game_stats
        self.tex_color_RGB = my_settings.score_text_color_RGB
        self.font = pygame.font.SysFont(None,self.my_settings.score_text_size)

        # initlai score
        self.update_score()
        # highes score
        self.update_high_score()
        # update level
        self.update_level()
        # update lives
        self.update_lives()
        # drawing the ships number equel to number of lives left
        self.draw_ships_lives()

    def update_score(self) -> None:
        """Updating the score"""    
        # changing the score to a imgage
        self.score_text_image = self.font.render("Points: " + \
            str(self.game_stats.total_score),True,self.tex_color_RGB)

        #  position of the score
        self.score_rect = self.score_text_image.get_rect()
        self.score_rect.topright = self.screen_rect.topright
        self.score_rect.x -= 20
        self.score_rect.y += 5

    def update_high_score(self) -> None:
        """Updating the high score"""    
        # changing the high score to a imgage
        self.high_score_text_image = self.font.render("High Score: " + \
            str(self.game_stats.high_score),True,self.tex_color_RGB)

        #  position of the score
        self.high_score_rect = self.high_score_text_image.get_rect()
        self.high_score_rect.topleft = self.screen_rect.topleft
        self.high_score_rect.x += 10
        self.high_score_rect.y += 5

    def update_level(self) -> None:
        """Updating the level"""    
        # changing the level number to a imgage
        self.level_text_image = self.font.render("Level: " + \
            str(self.game_stats.level),True,self.tex_color_RGB)

        #  position of the level image
        self.level_rect = self.level_text_image.get_rect()
        self.level_rect.bottomleft = self.screen_rect.bottomleft
        self.level_rect.x += 10
        self.level_rect.y -= 5  

    def update_lives(self) -> None:
        """Updating lives"""    
        # changing the lives number to a imgage
        self.lives_text_image = self.font.render("Lives: " + \
            str(self.game_stats.ships_lives),True,self.tex_color_RGB)

        #  position of the lives image
        self.lives_rect = self.lives_text_image.get_rect()
        self.lives_rect.bottomright = self.screen_rect.bottomright
        self.lives_rect.x -= 20
        self.lives_rect.y -= 5 

    def draw_ships_lives(self) -> None:
        """drawing number of ships equal to number of lives"""
        self.ships_lives_drawings = pygame.sprite.Group()
        for number_of_ship in range(self.game_stats.ships_lives):
            ships_lives_drawing = SpaceShip(self.my_settings,self.screen,0.1)
            ships_lives_drawing.rect.top = self.screen_rect.top
            ships_lives_drawing.rect.x += (-ships_lives_drawing.rect.width) + \
                number_of_ship  * ships_lives_drawing.rect.width
            self.ships_lives_drawings.add(ships_lives_drawing)

    def draw_score(self) -> None:
        """drawing the score"""
        self.screen.blit(self.score_text_image,self.score_rect)
        self.screen.blit(self.high_score_text_image,self.high_score_rect)
        self.screen.blit(self.level_text_image,self.level_rect)
        self.screen.blit(self.lives_text_image,self.lives_rect)
        self.ships_lives_drawings.draw(self.screen)
        