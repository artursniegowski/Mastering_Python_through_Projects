"""
class containing the setting for the tkinter GUI - 
for Image Watermarking Desktop App
"""
class GUISettings:
    """
    class with the settings for the GUI
    """
    MAIN_WINDOW_TITLE = "Image Watermarking App"
    MAIN_WINDOW_PADDING_X = 30
    MAIN_WINDOW_PADDING_Y = 30
    MAIN_WINDOW_WIDTH = 800 
    MAIN_WINOW_HEIGTH = 630
    # buttons
    BUTTON_UPLOAD_IMAGE_TEXT = 'Open Image'
    BUTTON_SAVE_IMAGE_TEXT = 'Save'
    BUTTON_ADD_WATERMARK_TEXT = 'Add Watermark'
    BUTTON_PADDING_X = 5
    BUTTON_PADDING_Y = 2
    # photo canvas
    CANVAS_WIDTH = 480
    CANVAS_HEIGHT = 480
    # Labels - Fonts
    FONT_NAME = "Courier"
    # canvas settings
    FONT_BOLD_COURIER = lambda size, FONT_NAME=FONT_NAME: (FONT_NAME,size,'bold')
    WATERMARK_LABEL_TEXT = "Watermark text:"
    # colors
    GREY = "#696464"
    WHITE = "#E9E5DD"
    ORANGE = "#FFA500"
    # input
    INPUT_WATERMARK_WIDTH = 27
    INPUT_WATERMARK_FONT = ('Arial', 14)
    #  Fonts ttf / paths to files
    FONTS_TTF = {
        'MONTSERRAT':'fonts/Montserrat-Regular.ttf',
        'RUBIKBUBBLES':'fonts/RubikBubbles-Regular.ttf',
        'PRESSSTART2P':'fonts/PressStart2P-Regular.ttf',
        'MONOTON':'fonts/Monoton-Regular.ttf',
        'RUBIKMOONROCKS':'fonts/RubikMoonrocks-Regular.ttf',
    }
    # Fonts size
    FONTS_SIZES = [num for num in range(8,94,2)]
    FONT_SIZE_MIN_MARGIN = 6
    FONT_SIZE_MAX_MARGIN = 250
    # Example font text
    EXAMPLE_FONT_TEXT = "Your FONT"
    # Slider settings
    SLIDER_LENGTH = 20
    SLIDER_WIDTH = 15
    SLIDER_SIZE_LENGTH = 200
    # Position X,Y and angle
    MIN_ANGLE_VALUE = 0
    MAX_ANGLE_VALUE = 360
    MAX_LENGTH_ANGLE_VALUE = 3
    X_VALUE_MARGIN = 0 # this value will be substracted
    Y_VALUE_MARGIN = 0 # this value will be substracted
    # Number of parts for deviding the picture for grid watermarks
    PARTS_NUM_FOR_GRID = 8
  