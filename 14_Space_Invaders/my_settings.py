# the main class encapsuplating all the settings
class MySettings():
    """This class represents all settings for the game"""

    def __init__(self) -> None:
        """Initilizing all the start values for the settings"""
        # Size of the Screen 
        self.screen_width = 800
        self.screen_height = 600
        # Background color
        self.background_color = (125,125,125)
        # Name of the window
        self.caption = "ALIEN INVASION V1.0"
        # Ship settings - speed
        self.ship_lives = 3
        # Rockets settings
        self.rocket_width = 2
        self.rocket_height = 12
        self.rocket_color_RGB = (100,0,0)
        self.rocket_capacity = 4
        # alien settins
        self.space_factor_x = 2.5
        self.space_factor_y = 1.5
        # setting default direction for alien space ships
        self.direction_alien_RIGHT = True
        # START button
        self.start_button_caption = "START"
        self.button_main_color_RGB = (0,0,160)
        self.button_hover_color_RGB = (0,0,255)
        self.button_text_color_RGB = (255,255,255)
        (self.button_width, self.button_height) = (200,50) 
        self.button_text_size = 45
        # Displaying score
        self.score_text_color_RGB = (70,0,0)
        self.score_text_size = 45
        # Path to read/save settings 
        self.subfolder_name = "data"
        self.subfolder_name_image = "images"
        self.name_alien_ship = "alien_ship.png"
        self.name_main_ship = "space_ship.png"
        self.file_name_json = "game_stats.json"

        self.init_settings_start_game()

    def init_settings_start_game(self) -> None:
        """Initiated the settings that will change over time"""
        # Max speed is 1.0 
        self.alien_ships_speed = 0.3
        # in pixels !
        self.alien_ships_speed_droping = 2
         # Rockets settings
        self.rocket_speed = 0.6
        # Ship settings - speed
        self.ship_speed = 0.2
        # starting score for alien ship
        self.alien_ship_points = 10
        # starting score for finishing a level
        self.next_level_points = 40



    def next_level(self) -> None:
        """Adjusting the sttings of the game to make it harder"""
        self.alien_ships_speed += 0.1
        self.alien_ships_speed_droping += 1
        self.rocket_speed += 0.2
        self.ship_speed += 0.1
        self.alien_ship_points += 5
        self.next_level_points += 15
