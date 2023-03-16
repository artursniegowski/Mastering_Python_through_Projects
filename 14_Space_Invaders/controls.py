# class for managing the buttons
from my_settings import MySettings
import pygame

class Control:
    """class to manage buttons"""

    def __init__(self, my_settings : MySettings, screen: pygame.Surface ,\
        info : str) -> None:

        self.screen = screen 
        self.screen_rect = screen.get_rect()
        self.zoom_scale = 1.05
        self.hover = False

        # Set the dimensions and properties of the button
        (self.width, self.height) = (my_settings.button_width, \
            my_settings.button_height)
        self.button_color = my_settings.button_main_color_RGB
        self.button_main_color = my_settings.button_main_color_RGB
        self.button_hover_color = my_settings.button_hover_color_RGB
        self.text_color = my_settings.button_text_color_RGB
        self.font = pygame.font.SysFont(None,my_settings.button_text_size)

        # Build the buttons react object and center it
        self.rect = pygame.Rect(0,0,self.width,self.height) 
        self.rect.center = self.screen_rect.center

        #Turn info into a render image and center text on the button"""
        self.text_image = self.font.render(info,True,self.text_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center


    def draw_button(self):
        # Draw blank button and then draw message
        # adjus the button if the mouse hover above the button
        if not self.hover:
            self.button_color = self.button_main_color
            self.rect.width = self.width
            self.rect.height = self.height
        else:
            self.button_color = self.button_hover_color
            self.rect.width = int(self.width*self.zoom_scale)
            self.rect.height = int(self.height*self.zoom_scale)
        
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.text_image,self.text_image_rect)
