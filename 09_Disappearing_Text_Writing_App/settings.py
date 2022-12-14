"""
class containing the settings for the tkinter GUI - 
for Disappearing Text Desktop App
"""
class ColorSettigns():
    """
    class for handling different colors / base
    """
    BLACK = "#000000"
    GREY = "#4D5656"
    GREY_LIGTH = "#BFC9CA"
    GREEN = "#27AE60"
    GREEN_LIGTH = "#1fc600"
    GREEN_ULTRA_LIGTH = "#99ff99"
    ORANGE = "#ff8533"
    RED = "#E74C3C"
    RED_ULTRA_LIGTH = "#FF8A8A"
    WHITE = "#EAEDED"
    YELLOW = "#E5DE00"

class GUISettings:
    """
    class with the settings for the GUI
    """
    # main window settings
    MAIN_WINDOW_TITLE = "Disappearing Text App"
    MAIN_WINDOW_PADDING_X = 30
    MAIN_WINDOW_PADDING_Y = 30
    MAIN_WINDOW_WIDTH = 610 
    MAIN_WINOW_HEIGTH = 540
    # Labels - Fonts
    FONT_DEFAULT_NAME = "Courier"
    FONT_DEFAULT_TYPE = "bold"
    # default font tyes settings
    FONT_DEFAULT = lambda size, font_name = FONT_DEFAULT_NAME, font_type = FONT_DEFAULT_TYPE: (font_name,size,font_type)
    # colors
    COLORS = ColorSettigns()
    # Main title
    MAIN_TITLE_LABEL = "The Most Dangerous Writing App"
    # instructions
    INSTRUCTIONS_LABEL = """Don't stop writing, or all progress will be lost. You can only be idle for 5 seconds!"""