"""
class containing the settings for the tkinter GUI - 
for Typing Speed Test Desktop App
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
    WHITE = "#EAEDED"
    YELLOW = "#E5DE00"

class GUISettings:
    """
    class with the settings for the GUI
    """
    # main window settings
    MAIN_WINDOW_TITLE = "Typing Speed Test App"
    MAIN_WINDOW_PADDING_X = 30
    MAIN_WINDOW_PADDING_Y = 30
    MAIN_WINDOW_WIDTH = 800 
    MAIN_WINOW_HEIGTH = 480
    # Labels - Fonts
    FONT_DEFAULT_NAME = "Courier"
    FONT_DEFAULT_TYPE = "bold"
    # default font tyes settings
    FONT_DEFAULT = lambda size, font_name = FONT_DEFAULT_NAME, font_type = FONT_DEFAULT_TYPE: (font_name,size,font_type)
    # colors
    COLORS = ColorSettigns()
    # Main title
    MAIN_TITLE_LABEL = "Typing Speed Test"
    # instructions
    INSTRUCTIONS_LABEL = """Test how fast you can type. Do this one-minute typing test to find out! 
    Press the space bar or enter after each word. You'll get your typing speed at CPM (characters per minute) 
    and WPM (word per minute). Press Reset button to start over. Good luck!"""