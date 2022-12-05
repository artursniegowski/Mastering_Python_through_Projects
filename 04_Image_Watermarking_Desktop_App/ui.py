"""
class for handling the user interface
"""
import os
from pathlib import Path
from PIL import Image, ImageTk, ImageDraw, ImageFont
from settings import GUISettings
import tkinter
from tkinter import ttk
from tkinter import filedialog

class UI(tkinter.Tk):
    """
    class for handling the UI for Watermarking App
    """
    
    def __init__(self, ) -> None:
        super(UI,self).__init__()
   
        self.title(GUISettings.MAIN_WINDOW_TITLE)
        self.config(
                padx = GUISettings.MAIN_WINDOW_PADDING_X,
                pady = GUISettings.MAIN_WINDOW_PADDING_Y,
                bg = GUISettings.GREY,
        )
        self.resizable(False, False)
        # self.minsize(640,400)
        self.geometry(f"{GUISettings.MAIN_WINDOW_WIDTH}x{GUISettings.MAIN_WINOW_HEIGTH}")

        # create canvas for the picture 
        self.create_canvas_for_image()
        # adding the three main buttons
        self.buttons_functions()
        # adding the label and input for the watermark
        self.adding_watermark_input()
        # adding the settings buttons for the watermarking
        self.color_settings_for_watermarking()
        # creating fonts settins for the watermakr text
        self.font_settings_watermark()
        # creating position and angle settings
        self.position_angle_settings_watermark()
        # creating radio box - layout
        self.layout_settings_for_watermark()


    def buttons_functions(self) -> None:
        """
        creating the main three buttons - functionality
        open image, add watermark, save image
        """
        self.button_upload_image = tkinter.Button(
            text=GUISettings.BUTTON_UPLOAD_IMAGE_TEXT,
            padx=GUISettings.BUTTON_PADDING_X,
            pady=GUISettings.BUTTON_PADDING_Y,
            command=self.browsefiles,
            )
        self.button_upload_image.grid(
            row=10,
            column=2,
            # padx=10,
            # pady=10,
            )

        self.button_add_watermark = tkinter.Button(
            text=GUISettings.BUTTON_ADD_WATERMARK_TEXT,
            padx=GUISettings.BUTTON_PADDING_X,
            pady=GUISettings.BUTTON_PADDING_Y,
            command=self.add_watermark,
            state='disabled',
            )
        self.button_add_watermark.grid(
            row=10,
            column=3,
            # padx=10,
            # pady=10,
            )

        self.button_save_image = tkinter.Button(
            text=GUISettings.BUTTON_SAVE_IMAGE_TEXT,
            padx=GUISettings.BUTTON_PADDING_X,
            pady=GUISettings.BUTTON_PADDING_Y,
            state='disable',
            command=self.save_photo,
            )
        self.button_save_image.grid(
            row=10,
            column=4,
            # padx=10,
            # pady=10,
            )

    def adding_watermark_input(self) -> None:
        """
        adding the label and input for the watermark text
        """
        # label for watermark
        self.label_watermark = tkinter.Label(
            text=GUISettings.WATERMARK_LABEL_TEXT, 
            fg=GUISettings.WHITE,
            font=GUISettings.FONT_BOLD_COURIER(14), 
            bg=GUISettings.GREY)
        self.label_watermark.grid(
            row=10,
            column=0,
            pady=10,
            ) 
        # watermark text input
        self.input_watermark = tkinter.Entry(
            width=GUISettings.INPUT_WATERMARK_WIDTH,
            font=GUISettings.INPUT_WATERMARK_FONT,
            bg=GUISettings.WHITE,
            highlightcolor='red',
            highlightbackground=GUISettings.WHITE,
            # highlightbackground='red',
            highlightthickness=2,
            )
        self.input_watermark.grid(
            row=10,
            column=1,
            pady=10,
            padx=(0,30),
            )

    def create_canvas_for_image(self) -> None :
        """
        creating canvas from the image
        """
        # creating canvas for displaying the photo
        # creating canvas witht the tomato pic and time value text
        self.canvas_photo = tkinter.Canvas(
            width=GUISettings.CANVAS_WIDTH, 
            height=GUISettings.CANVAS_HEIGHT, 
            highlightthickness=0,
            bg=GUISettings.WHITE,
            )

        self.canvas_img = self.canvas_photo.create_image(
            GUISettings.CANVAS_WIDTH/2,
            GUISettings.CANVAS_HEIGHT/2,
            # image=img_1,
            )
        # adding watermark
        # timmer_text_canvas = canvas.create_text(CANVAS_WIDTH/2,CANVAS_HEIGHT/2+20, \
        #     text="00:00", fill=CANVAS_FILL_TEXT_COLOR,font=CANVAS_TEXT_FONT)
        self.canvas_photo.grid(
            row=0,
            column=0,
            columnspan=2,
            rowspan=10,
            padx=(0,30),
            ) 

    def color_settings_for_watermarking(self) -> None:
        """
        creating buttons and widgets for choosing settings for
        the watermark
        """
        width_color_canvas = 170
        height_color_canvas = 30

        update_color_scale = lambda event : self.update_color_img(
            event,width_canvas=width_color_canvas, height_canvas=height_color_canvas)

        self.RGBA_elements = tkinter.LabelFrame(
            text=" Watermark - RGBA Color Model ",
            bg=GUISettings.GREY,
            font=('Time',8),
            labelanchor='n',
        )
        self.RGBA_elements.grid(
            column=2,
            columnspan=3,
            row=0,
            rowspan=3,
            padx=5,
            pady=2,
        )

        # four sliders for RGBA
        self.slider_R = self.create_a_slider(
            parent=self.RGBA_elements,
            row_pos=0,
            column_pos=2,
            label_text='RED',
            command_function = update_color_scale,
            )

        # setting values for R
        self.slider_R.set(100)

        self.slider_G = self.create_a_slider(
            parent=self.RGBA_elements,
            row_pos=1,
            column_pos=2,
            label_text='GREEN',
            command_function = update_color_scale,
            )
        
        # setting values for G
        self.slider_G.set(100)

        self.slider_B = self.create_a_slider(
            parent=self.RGBA_elements,
            row_pos=2,
            column_pos=2,
            label_text='BLUE',
            command_function = update_color_scale,
            )
        
        # setting values for B
        self.slider_B.set(200)

        self.slider_A = self.create_a_slider(
            parent=self.RGBA_elements,
            row_pos=3,
            column_pos=2,
            label_text='ALPHA - Opacity',
            command_function = update_color_scale,
            )

        # setting values for A
        self.slider_A.set(125)

        # creating a canvas with a dynamicaly chanign color based on the slide bars
        self.canvas_current_color = tkinter.Canvas(
            self.RGBA_elements,
            width=width_color_canvas, 
            height=height_color_canvas, 
            highlightthickness=0,
            bg="#E9E5DD",
            )

        self.canvas_current_color.create_text(80,15,text="COLOR",)
        self.color_img_show = ImageTk.PhotoImage(
            Image.new(
                "RGBA", 
                (width_color_canvas,height_color_canvas),
                (int(self.slider_R.get()),
                int(self.slider_G.get()),
                int(self.slider_B.get()),
                int(self.slider_A.get())))
        )
        self.canvas_current_color_img = self.canvas_current_color.create_image(
            width_color_canvas/2,
            height_color_canvas/2,
            image = self.color_img_show
        )
        self.canvas_current_color.grid(
            row=4,
            column=3,
            padx=10,
            pady=10,
            ) 

    def create_a_slider(self, row_pos:int, column_pos:int, label_text:str|None = None, \
                        parent: tkinter.LabelFrame|None = None, command_function:str|None = None) -> tkinter.Scale:
        """
        function for creating a slider
        """

        slider = tkinter.Scale(
            parent,
            from_=0,
            to=255,
            # tickinterval=1,
            sliderlength=GUISettings.SLIDER_LENGTH,
            length=GUISettings.SLIDER_SIZE_LENGTH,
            bg=GUISettings.GREY,
            orient='horizontal',
            width=GUISettings.SLIDER_WIDTH,
            highlightthickness=0,
            font=GUISettings.FONT_BOLD_COURIER(9),
            border=0,
            label=label_text,
            command=command_function,
        )
        slider.grid(
            row=row_pos,
            column=column_pos,
            columnspan=3,
            padx=10,
            pady=2,
        )

        return slider

    def update_color_img(self, event, width_canvas:int, height_canvas:int) -> None:
        """
        Function for updating the color on the canvas
        based on the values from the slide bars
        """
        
        self.img_color_slide = ImageTk.PhotoImage(
            Image.new(
                "RGBA", 
                (width_canvas,height_canvas),
                (int(self.slider_R.get()),
                int(self.slider_G.get()),
                int(self.slider_B.get()),
                int(self.slider_A.get())))
        )
        

        self.canvas_current_color.itemconfig(
                self.canvas_current_color_img,
                image = self.img_color_slide,
            )

    def font_settings_watermark(self) -> None:
        """
        function for definign the settings for font , type and sieze
        for the water mark
        """
        self.Fonts_settings_elements = tkinter.LabelFrame(
            text=" FONT - Type and Size ",
            font=('Time',8),
            bg=GUISettings.GREY,
            labelanchor='n',
        )
        self.Fonts_settings_elements.grid(
            column=2,
            columnspan=3,
            row=3,
            rowspan=2,
            padx=5,
            pady=5,
        )

        self.font_type_drop_box = ttk.Combobox(
            self.Fonts_settings_elements,
            state="readonly",
            values=list(GUISettings.FONTS_TTF.keys()),
            width=18,
        )
        self.font_type_drop_box.grid(
            column=2,
            columnspan=2,
            row=3,
            padx=10,
            pady=10,
        )
        self.font_type_drop_box.set(list(GUISettings.FONTS_TTF.keys())[0])
        self.font_type_drop_box.bind("<<ComboboxSelected>>",self.font_values_updated)

        self.font_size_drop_box = ttk.Combobox(
            self.Fonts_settings_elements,
            values=list(GUISettings.FONTS_SIZES),
            width=4,
        )
        self.font_size_drop_box.grid(
            column=4,
            columnspan=1,
            row=3,
            padx=10,
            pady=10,
        )
        self.font_size_drop_box.set(list(GUISettings.FONTS_SIZES)[len(GUISettings.FONTS_SIZES)//2])
        self.font_size_drop_box.bind("<<ComboboxSelected>>",self.font_values_updated)

        # example font type !
        example_text_font = ImageFont.truetype(
            GUISettings.FONTS_TTF[self.font_type_drop_box.get()], 
            size=20,
            ) 
        # creating an image for the exmaple text
        example_txt_img = Image.new(
            "RGBA", 
            # getting the size of the font / text
            (example_text_font.getsize(GUISettings.EXAMPLE_FONT_TEXT)[0]+20,example_text_font.getsize(GUISettings.EXAMPLE_FONT_TEXT)[1]+20), 
            (255,255,255,0)
            )
        # drawing the example text on the image
        draw = ImageDraw.Draw(example_txt_img)
        draw.text(
                xy = (0,0), 
                text = GUISettings.EXAMPLE_FONT_TEXT, 
                font = example_text_font,
                fill = (0,0,0,255), #RGBA - all integers 0-255
                )

        # creating a canvas for the text image
        self.canvas_exampple_text = tkinter.Canvas(
            self.Fonts_settings_elements,
            width=180, 
            height=35, 
            highlightthickness=0,
            bg=GUISettings.GREY,
            )

        self.examle_img_text = ImageTk.PhotoImage(example_txt_img)

        self.canvas_exampple_text_create_img =  self.canvas_exampple_text.create_image(
            (100,20),
            image = self.examle_img_text
        )
        self.canvas_exampple_text.grid(
            column=2,
            columnspan=3,
            row=4,
            padx=10,
        ) 

    def position_angle_settings_watermark(self) -> None:
        """
        Function for setting the position and angle of the watermark
        """
        self.position_angle_settings_elements = tkinter.LabelFrame(
            text=" Watermark - Position and Angle ",
            font=('Time',8),
            bg=GUISettings.GREY,
            labelanchor='n',
        )
        self.position_angle_settings_elements.grid(
            column=2,
            columnspan=3,
            row=5,
            rowspan=3,
            padx=5,
            pady=5,
        )

        self.position_x_label = tkinter.Label(
            self.position_angle_settings_elements,
            text='X',
            font=GUISettings.FONT_BOLD_COURIER(9),
            background=GUISettings.GREY,
        )
        self.position_x_label.grid(
            row=5,
            column=2,
        )

        # default values for the validation
        x_validation_function = (self.register(self._validate_angle_X_Y), '%P', -int(GUISettings.X_VALUE_MARGIN), 500, 10)

        self.position_x_input = tkinter.Entry(
            self.position_angle_settings_elements,
            width=8,
            bg=GUISettings.GREY,
            disabledbackground=GUISettings.GREY,
            state='disabled',
            justify='center',
            validate='all',
            validatecommand=x_validation_function,
        )                
        self.position_x_input.grid(
            row=6,
            column=2,
            padx=7,
            # pady=5,
        )
        self.position_x_input.insert(0,0)
        self.position_x_input.bind("<FocusOut>",self._check_angle_X_Y_value_by_exit)

        self.position_x_input_range = tkinter.Label(
            self.position_angle_settings_elements,
            text=f'{-int(GUISettings.X_VALUE_MARGIN)}-1000',
            font=('Times', 8),
            state='disabled',
            foreground=GUISettings.ORANGE,
            background=GUISettings.GREY,
        )
        self.position_x_input_range.grid(
            row=7,
            column=2,
        )

        self.position_y_label = tkinter.Label(
            self.position_angle_settings_elements,
            text='Y',
            font=GUISettings.FONT_BOLD_COURIER(9),
            background=GUISettings.GREY,
        )
        self.position_y_label.grid(
            row=5,
            column=3,
        )

        # default values for the validation
        y_validation_function = (self.register(self._validate_angle_X_Y), '%P', -int(GUISettings.Y_VALUE_MARGIN), 500, 10)

        self.position_y_input = tkinter.Entry(
            self.position_angle_settings_elements,
            width=8,
            bg=GUISettings.GREY,
            disabledbackground=GUISettings.GREY,
            state='disabled',
            justify='center',
            validate='all',
            validatecommand=y_validation_function,
        )                
        self.position_y_input.grid(
            row=6,
            column=3,
            padx=7,
            # pady=5,
        )
        self.position_y_input.insert(0,0)
        self.position_y_input.bind("<FocusOut>",self._check_angle_X_Y_value_by_exit)

        self.position_y_input_range = tkinter.Label(
            self.position_angle_settings_elements,
            text=f'{int(-GUISettings.Y_VALUE_MARGIN)}-1000',
            font=('Times', 8),
            state='disabled',
            foreground=GUISettings.ORANGE,
            background=GUISettings.GREY,
        )
        self.position_y_input_range.grid(
            row=7,
            column=3,
        )

        self.position_angle_label = tkinter.Label(
            self.position_angle_settings_elements,
            text='ANGLE',
            font=GUISettings.FONT_BOLD_COURIER(9),
            background=GUISettings.GREY,
        )
        self.position_angle_label.grid(
            row=5,
            column=4,
        )

        angle_validation_function = self.register(self._validate_angle_X_Y)

        self.position_angle_input = tkinter.Entry(
            self.position_angle_settings_elements,
            width=6,
            bg=GUISettings.GREY,
            justify='center',
            validate='all',
            validatecommand=(angle_validation_function, '%P', GUISettings.MIN_ANGLE_VALUE, GUISettings.MAX_ANGLE_VALUE, GUISettings.MAX_LENGTH_ANGLE_VALUE),
        )                
        self.position_angle_input.grid(
            row=6,
            column=4,
            padx=7,
            # pady=5,
        )
        self.position_angle_input.insert(0,0)
        self.position_angle_input.bind("<FocusOut>",self._check_angle_X_Y_value_by_exit)
        
        self.position_angle_input_range = tkinter.Label(
            self.position_angle_settings_elements,
            text='0-360',
            font=('Times', 8),
            foreground=GUISettings.ORANGE,
            background=GUISettings.GREY,
        )
        self.position_angle_input_range.grid(
            row=7,
            column=4,
        )

    def _check_angle_X_Y_value_by_exit(self, event) -> None:
        """
        checking if the angle was left empty if so
        we fill it with 0
        """

        if self.position_angle_input.get() == '':
            self.position_angle_input.delete(0,tkinter.END)
            self.position_angle_input.insert(0,0)

        if self.position_x_input.get() == '':
            self.position_x_input.delete(0,tkinter.END)
            self.position_x_input.insert(0,0)

        if self.position_y_input.get() == '':
            self.position_y_input.delete(0,tkinter.END)
            self.position_y_input.insert(0,0)


    def _validate_angle_X_Y(self, value_inserted, min_val:int, max_val:int, length_val:int=0) -> bool:
        """
        validate that the value inserted for angle is between 0-360
        validation for X, Y is variable and defined by the size of the picture loaded
        """ 
        # this function will allow only to type in vales that are in range
        # if value allowed return True otherwise retun False
   
        try:
            if value_inserted == '':
                value = 0
            else:
                value = int(value_inserted)
                if value > int(max_val) or value < int(min_val) or len(value_inserted) > int(length_val):
                    raise ValueError()
        except ValueError:
            return False
        
        return True
        
    def layout_settings_for_watermark(self) -> None:
        """
        adding the settings for watermark layout, 
        the options are:
        - a grid of watermarks, or 
        - a single watermark
        """
        self.layout_var = tkinter.IntVar()

        self.layout_settings_elements = tkinter.LabelFrame(
            text=" Watermark - Layout ",
            font=('Time',8),
            bg=GUISettings.GREY,
            labelanchor='n',
        )
        self.layout_settings_elements.grid(
            column=2,
            columnspan=3,
            row=8,
            rowspan=1,
            # padx=5,
            # pady=5,
        )

        self.layout_grid = tkinter.Radiobutton(
            self.layout_settings_elements,
            text="Single",
            font=GUISettings.FONT_BOLD_COURIER(9),
            value=1,
            variable=self.layout_var,
            command=self._selected_layout,
            background=GUISettings.GREY,
        )
        self.layout_grid.grid(
            column=2,
            row=9,
        )

        self.layout_single = tkinter.Radiobutton(
            self.layout_settings_elements,
            text="Grid",
            font=GUISettings.FONT_BOLD_COURIER(9),
            value=2,
            variable=self.layout_var,
            command=self._selected_layout,
            background=GUISettings.GREY,
        )
        self.layout_single.grid(
            column=3,
            row=9,
        )

        # default value for the radio button
        self.layout_var.set(1)
        self.parts = 1

    def _selected_layout(self) -> None:
        """
        setting the value of parts, depending on selected
        layout.
        single - 1 part - only one watermark
        grid - 8 parts - (deviding the main picture by 8) - base value distance for watermarks
        """
        if self.layout_var.get() == 1:
            self.parts = 1
        else:
            self.parts = int(GUISettings.PARTS_NUM_FOR_GRID)

    def font_values_updated(self, eventObject) -> None:
        """
        Function for updating the example text based on the 
        values in the drop box, if a value gets changed ,
        this function will update the styling (the font) of the example text
        but not its size since the size will be depicted on the main screen
        """

        example_text_font = ImageFont.truetype(
            GUISettings.FONTS_TTF[self.font_type_drop_box.get()], 
            size=20,
            ) 
        # creating an image for the exmaple text
        example_txt_img = Image.new(
            "RGBA", 
            # getting the size of the font / text
            (example_text_font.getsize(GUISettings.EXAMPLE_FONT_TEXT)[0]+20,example_text_font.getsize(GUISettings.EXAMPLE_FONT_TEXT)[1]+20), 
            (255,255,255,0)
            )
        # drawing the example text on the image
        draw = ImageDraw.Draw(example_txt_img)
        draw.text(
                xy = (0,0), 
                text = GUISettings.EXAMPLE_FONT_TEXT, 
                font = example_text_font,
                fill = (0,0,0,255), #RGBA - all integers 0-255
                )

        self.examle_img_text = ImageTk.PhotoImage(example_txt_img)

        self.canvas_exampple_text.itemconfig(
                self.canvas_exampple_text_create_img,
                image = self.examle_img_text,
            )

    def _check_font_size_value(self) -> int:
        """
        checking the value of the dropbox - size of the font
        """
        middle_value = GUISettings.FONTS_SIZES[len(GUISettings.FONTS_SIZES)//2]
        
        try:
            # if value set for size ist not a number / interger
            value = (int(self.font_size_drop_box.get()))
            # only value in range 6-150 will be excepted
            if  value < GUISettings.FONT_SIZE_MIN_MARGIN or value > GUISettings.FONT_SIZE_MAX_MARGIN:
                raise ValueError()
        except ValueError:
            self.font_size_drop_box.set(middle_value)

        return (int(self.font_size_drop_box.get()))

    def _return_input_value_angle(self) -> int:
        """
        checking the value input of angle
        """
        return self.__check_input_value(
            self.position_angle_input, 
            min_value=int(GUISettings.MIN_ANGLE_VALUE), 
            max_value=int(GUISettings.MAX_ANGLE_VALUE),
            )

    def _return_input_value_X(self) -> int:
        """
        checking the value input of X
        """
        return self.__check_input_value(
            self.position_x_input, 
            min_value=0-int(GUISettings.X_VALUE_MARGIN), 
            max_value=self.img_org.size[0]+int(GUISettings.X_VALUE_MARGIN),
            )

    def _return_input_value_Y(self) -> int:
        """
        checking the value input of Y
        """
        return self.__check_input_value(
            self.position_y_input, 
            min_value=0-int(GUISettings.Y_VALUE_MARGIN), 
            max_value=self.img_org.size[1]+int(GUISettings.Y_VALUE_MARGIN),
            )

    def __check_input_value(self, name_of_input: tkinter.Entry, min_value:int, max_value:int) -> int:
        """
        checking the value of given input and returns the value of this input
        if not valid or out of range a 0 will be inserted into to input and returned
        """
        try:
            # if value set for size ist not a number / interger
            value = (int(name_of_input.get()))
            # only value in range 6-150 will be excepted
            if  value < min_value or value > max_value:
                raise ValueError()
        except ValueError:
            # set to default value
            name_of_input.delete(0,tkinter.END),
            name_of_input.insert(0,0)

        return (int(name_of_input.get()))



    # functions !! for buttons and interaction with the gui elements
    def add_watermark(self) -> None:
        """
        adding the watermark
        """
        watermark_text = self.input_watermark.get().strip()
        if watermark_text == '':
            # getting users atention
            # chaning the border of the input box to red
            self.input_watermark['highlightbackground'] = 'red' 

        if watermark_text != '':

            # changing color of the input border back to normal
            self.input_watermark['highlightbackground'] = GUISettings.WHITE

            # we wait for the process to finish
            self.disable_add_watermark_button()

            # starting always with a fresh picture
            img_org_copy = self.img_org.copy()
            
            # creating two pictures and later converting them
            # to RGBA to achive transparetn text !
            img_org_copy = img_org_copy.convert("RGBA")


            # settings for the watermark font font
            font_watermark = ImageFont.truetype(
                GUISettings.FONTS_TTF[self.font_type_drop_box.get()], 
                size=self._check_font_size_value(),
                )
            
            # creating a img for txt to achive transparetn pictures
            # it has to be the size of the text to make it posible to rotate first
            txt_img = Image.new(
                "RGBA", 
                # getting the size of the font / text
                font_watermark.getsize(watermark_text), 
                (255,255,255,0)
                )

            draw = ImageDraw.Draw(txt_img)

            # draw text on image
            draw.text(
                xy = (0,0), 
                text = watermark_text, 
                font = font_watermark,
                fill = (
                    int(self.slider_R.get()),  
                    int(self.slider_G.get()),
                    int(self.slider_B.get()),
                    int(self.slider_A.get()),
                    ), #RGBA - all integers 0-255
                )
            

            # rotating the text image
            txt_img_rotated = txt_img.rotate(
                angle=self._return_input_value_angle(),
                expand=True,
            )


            self.img_with_watermark  = img_org_copy
            # ==================================================================
            # for loop for grid of watermarks
            # self.parts = 8
            start_x = img_org_copy.size[0]//self.parts
            start_y = img_org_copy.size[1]//self.parts
            for x_multiplication in range(0,self.parts,2):
                for y_multiplication in range(0,self.parts,2):
                    x_pos = start_x * x_multiplication
                    y_pos = start_y * y_multiplication

            # creating watermark image for positoining the text on the image
            # first we had to rotate the text and here we are setting
            # the starting positoins for the text / logo
            # the same size as orignal image and with transparent color
                    watermark_img = Image.new(
                        "RGBA",
                        img_org_copy.size,
                        (255,255,255,0),
                    )

                    # putting text on watermakrs image
                    watermark_img.paste(
                        txt_img_rotated,
                        # position X, Y
                        # (x_pos, y_pos)
                        (x_pos+self._return_input_value_X(), y_pos+self._return_input_value_Y()),
                    )

                    # combining the pictures
                    self.img_with_watermark = Image.alpha_composite(self.img_with_watermark, watermark_img)

            # ======================================================================

            # adding image to the canvas
            self.update_img_canvas(self.img_with_watermark)

            # enable the next step
            self.enable_save_button()

            # when process finished we unblock the button again
            self.enable_add_watermark_button()

    def save_photo(self) -> None:
        """
        saving the photo with the watermark
        """
        # first getting the coordinate for the x,y of watermark
        # and drawing it on the original size of the photo
        # and then saving it

        # creating the path to save the file to // absolute as recomended in PEP
        base_path = Path(__file__).parent
        file_name = self.img_file_name.split('.')[0]
        file_extension = self.img_file_name.split('.')[-1]

        # creating teh file path in the main application and saving the photo there
        file_path = (base_path / f"./img/watermarked_{file_name}.{file_extension}").resolve()
        
        # checking if path exists 
        # if it doses - we add a number to the file name and try again
        num = 1
        while os.path.isfile(file_path):
            file_path = (base_path / f"./img/watermarked_{file_name}({num}).{file_extension}").resolve()
            num += 1

        # Save watermarked image
        self.img_with_watermark.save(file_path)

        # changing the status of the buttons
        # to start from the begining
        self.disable_add_watermark_button()
        self.disable_save_button()   

        # erasing the previous image
        self.clear_after_save()

    def browsefiles(self) -> None:
        """
        getting the filename and path of the image
        and updating the image in the canvas
        """
        img_path_filename = filedialog.askopenfilename(
                                            initialdir = os.getcwd(),
                                            title = "Select an Image",
                                            filetypes = (
                                                ("PNG","*.png*"),
                                                ("JPG","*.jpg*"),
                                            ))
        # loading the image
        # if path is not empty
        if img_path_filename != '': 
            
            # getitng the file name
            self.img_file_name = img_path_filename.split('/')[-1]

            # print(img_path_filename)
            self.img_org = Image.open(img_path_filename)

            # adding image to the canvas
            self.update_img_canvas(self.img_org)

            # enable adding watermark
            self.enable_add_watermark_button()
            self.disable_save_button()
            # enable position inputs
            self._enable_positions_inputs_X_Y()

    def _enable_positions_inputs_X_Y(self) -> None:
        """
        funciton for enabling the inputs X and Y
        """   
        # Y position
        self.position_y_input['state'] = 'normal'
        self.position_y_input.delete(0,tkinter.END)
        self.position_y_input.insert(0,0)
        self.position_y_input_range['state'] = 'normal'
        y_min, y_max = -int(GUISettings.Y_VALUE_MARGIN), self.img_org.size[1]
        self.position_y_input_range['text'] = f'{y_min}-{y_max}'
        # updating the validation function 
        y_validation_function = (self.register(self._validate_angle_X_Y), '%P', y_min, y_max, len(str(y_max)))
        self.position_y_input.config(validatecommand=y_validation_function) 

        # X position
        self.position_x_input['state'] = 'normal'
        self.position_x_input.delete(0,tkinter.END)
        self.position_x_input.insert(0,0)
        self.position_x_input_range['state'] = 'normal'   
        x_min, x_max = -int(GUISettings.X_VALUE_MARGIN), self.img_org.size[0]
        self.position_x_input_range['text'] = f'{x_min}-{x_max}'
        # updating the validation function 
        x_validation_function = (self.register(self._validate_angle_X_Y), '%P', x_min, x_max, len(str(x_max)))
        self.position_x_input.config(validatecommand=x_validation_function) 

        self.position_angle_input.delete(0,tkinter.END)
        self.position_angle_input.insert(0,0)


    def _disable_positions_inputs_X_Y(self) -> None:
        """
        funciton for disabling the inputs X and Y
        """   
        self.position_y_input['state'] = 'disable'
        self.position_y_input.delete(0,tkinter.END)
        self.position_y_input.insert(0,0)
        self.position_y_input_range['state'] = 'disable'
        self.position_x_input['state'] = 'disable'
        self.position_x_input.delete(0,tkinter.END)
        self.position_x_input.insert(0,0)
        self.position_x_input_range['state'] = 'disable'  

        self.position_angle_input.delete(0,tkinter.END)
        self.position_angle_input.insert(0,0)


    def update_img_canvas(self, img: Image) -> None:
        """
        Updatig the photo on the canvas
        """
        if img:
            self.img = ImageTk.PhotoImage(
                img.resize(
                    (GUISettings.CANVAS_WIDTH, GUISettings.CANVAS_HEIGHT), 
                    Image.ANTIALIAS,)
                )

        self.canvas_photo.itemconfig(
                self.canvas_img,
                image = self.img,
            )

    def enable_save_button(self) -> None:
        """
        enable the save button
        """
        self.button_save_image.config(state='normal')

    def disable_save_button(self) -> None:
        """
        diable the save button
        """
        self.button_save_image.config(state='disable')

    def enable_add_watermark_button(self) -> None:
        """
        enable the save button
        """
        self.button_add_watermark.config(state='normal')

    def disable_add_watermark_button(self) -> None:
        """
        diable the save button
        """
        self.button_add_watermark.config(state='disable')

    def clear_after_save(self) -> None:
        """
        clearing all the pictures and data after saving
        """
        # setting back the image in the canvas to a white / clear image
        img_clean = Image.new(
            "RGBA",
            (100,100),
            GUISettings.WHITE,
            # (255,255,255,0),
        )
        self.update_img_canvas(img_clean)
        self.input_watermark.delete(0,tkinter.END)
        # X Y inputs disabled as long as the image is not loaded bc
        # we dont know the dimensions yet !
        self._disable_positions_inputs_X_Y()

