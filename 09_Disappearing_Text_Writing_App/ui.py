"""
class for handling the user interface - disappearing text app
"""

from settings import GUISettings
import tkinter as tk
import tkinter.ttk as ttk

class UI(tk.Tk):
    """
    class for handling the UI for disappearing text app
    """

    def __init__(self, ) -> None:
        super(UI,self).__init__()

        # creating the main window and its parameters/settings
        # color/ size/ title etc.
        self.title(GUISettings.MAIN_WINDOW_TITLE)
        self.config(
                padx = GUISettings.MAIN_WINDOW_PADDING_X,
                pady = GUISettings.MAIN_WINDOW_PADDING_Y,
                bg = GUISettings.COLORS.GREY,
        )
        self.resizable(False, False)
        self.geometry(f"{GUISettings.MAIN_WINDOW_WIDTH}x{GUISettings.MAIN_WINOW_HEIGTH}")

        # global variable for timer
        self.timer_started = False
        # global variable used to reset the timer
        self.reset_iteration_timer = False

        # creating objects of the app
        # creating intro object
        self.create_intro()
        # creating scores, display text for typing and user input box objects
        self.create_disappearing_text_box()
        # creating controls
        self.create_buttons()
        
    ############################################################################
    ########################## main gui parts ##################################
    ############################################################################
    def create_intro(self) -> None:
        """
        function for creating the intro - which includes, title and instuctions.
        """
        
        # title label
        self.disappearing_text_main_title = tk.Label(
            text=GUISettings.MAIN_TITLE_LABEL,
            font=GUISettings.FONT_DEFAULT(24,font_name="Times"),
            fg=GUISettings.COLORS.RED,
            bg=GUISettings.COLORS.GREY,
        ).grid(
            row=0,
            column=0,
            # pady=10,
            ) 
        # instructions label
        self.instructions_label = tk.Label(
            text=GUISettings.INSTRUCTIONS_LABEL,
            font=GUISettings.FONT_DEFAULT(12,font_name="Times"),
            fg=GUISettings.COLORS.WHITE,
            bg=GUISettings.COLORS.GREY,
        ).grid(
            row=1,
            column=0,
            pady=10,
            ) 

    def create_disappearing_text_box(self):
        """
        creating the two main component for the speed test,
        first is the text area,
        second is time following widget
        """
        # 1: text area input - with timmer
        self._create_text_area_input()
        # 2: time following widget
        self._created_time_widget()

    def create_buttons(self):
        """
        creating button for restarting the app 
        """
        self.button_restart = self.__create_button(
            parent=None,
            text="Restart",
            bg=GUISettings.COLORS.WHITE,
            column=0,
            row=4,
            padx=(0,0),
            pady=(10,0),
            width = 20,
            command=self.__reset_to_start,
        )
        # disable the button at the start
        self.button_restart['state'] = tk.DISABLED

    ############################################################################
    ########################## subparts for gui ################################
    ############################################################################ 
    def _create_text_area_input(self) -> None:
        """
        creating user input box - text area
        """
        # the user input box
        self.user_input_box = tk.LabelFrame(
            # text=" Typing box ",
            border=2,
            bg = GUISettings.COLORS.GREEN,
            fg = GUISettings.COLORS.GREEN,
            width= 500,
            height = 250,
            font = GUISettings.FONT_DEFAULT(10),
            relief="ridge",
            labelanchor='n',        
        )
        self.user_input_box.grid(
            row=3,
            column=0,
            pady=(20,0),
        )
        self.user_input_box.grid_propagate(0)

        self.user_input = tk.Text(
            self.user_input_box,
            bg = GUISettings.COLORS.GREEN_ULTRA_LIGTH,
            width=60,
            height=17,
            font=GUISettings.FONT_DEFAULT(13,font_name="Times",font_type="bold"),
            wrap='word',
        )
        # centering our placeholder tag
        self.user_input.tag_configure("placeholder", justify='center')
        self.user_input.pack()

        # insert placeholder
        self._insert_placeholder("Start typing...")

        # for getting rid of the placeholder - and setting default black color for the font
        self.user_input.bind("<FocusIn>",self._user_input_erase_placeholder)

        # binding to any key pressed in the text box
        self.user_input.bind("<Key>",self._reset_timer)



    def _insert_placeholder(self, text:str) -> None:
        """
        inserts placeholder in the user input
        """
        self.user_input.config(
            fg=GUISettings.COLORS.GREY,
            )
    
        self.user_input.delete('0.0',tk.END)
        self.user_input.insert('0.0',text)
        self.user_input.tag_add("placeholder", "0.0", "end")


    def _user_input_erase_placeholder(self, event_object) -> None:
        """
        function for erasing the placeholder from the user input and 
        setting the new color of the font
        """
        self.user_input.delete('0.0',tk.END)
        self.user_input.config(
            fg=GUISettings.COLORS.BLACK
        )

    def _reset_timer(self, event_object) -> None:
        """
        starting the countdown for timeer, only if the timer is currently NOT running
        """
        # start timmer only if the timer is not running yet
        if not self.timer_started:
            # setting a value to indicate the timer has started
            self.timer_started = True
            self.__start_count_down()
        
        # setting back the timer
        self.reset_iteration_timer = True


    def _created_time_widget(self) -> None:
        """
        creating a progess bar for the time widget - indication how much time is left
        """ 
         # the time progressbar
        self.time_progressbar = ttk.Progressbar(
            orient=tk.HORIZONTAL,
            length=550,
            mode= 'determinate',
            maximum=100,
            value=100,
        )
        self.time_progressbar.grid(
            row=2,
            column=0,
            pady=(0,0),
        )

    ############################################################################
    ############################# gui functions ################################
    ############################################################################  
    def __start_count_down(self, iteration_timer: int = 0, time:float=5.00) -> None:
        """
        start timer, update value of the timer, 
        every iteration is 50ms - start value,
        time is a value in seconds
        """
        max_count = time/0.05
        margin_max_count = (time - 1.5)/0.05

        self.time_progressbar['value'] = self.__get_value_for_progressbar(iteration_timer,max_count)

        # reseting the iteration 
        if self.reset_iteration_timer:
            iteration_timer = 0
            self.reset_iteration_timer = False
            self.time_progressbar['value'] = 100
        
        # changing the color of background - based on the timmer
        # changes to red if ony 1.5 seconds left, changing to green otherwise
        if iteration_timer > margin_max_count:
            self.user_input.config(
                bg = GUISettings.COLORS.RED_ULTRA_LIGTH,
                insertofftime = 0,
            )
        else:
            self.user_input.config(
                bg = GUISettings.COLORS.GREEN_ULTRA_LIGTH,
                insertofftime = 0,
            )
    

        if iteration_timer <= max_count:
            # every 50ms calling the same function with the increased iteration - recursive
            self.timer_counter = self.after(50,self.__start_count_down, iteration_timer + 1 )
        else:
            
            # posible to process the text from the user before deletion ?
            # user_text_inputed = self.user_input.get("0.0", tk.END)
            # print(user_text_inputed)

            # time is up - erasing all the data in the box
            # add setting a placeholder 
            self._insert_placeholder("Time is UP!")
            # disable text input box
            self.user_input.config(state=tk.DISABLED)
            # unbinding events 
            self.user_input.unbind("<Key>")
            # cancel the timer
            self.after_cancel(self.timer_counter)
            # global variable for idicating the timer has stoped
            self.timer_started = False
            # setting the progess bar to 0
            self.time_progressbar['value'] = 0
            # enable the restart to start button
            self.button_restart['state'] = tk.NORMAL


    def __get_value_for_progressbar(self, iteration_timer: int = 0, max_iteration: int = 100) -> int:
        """
        calulates a value between 0 - 100 for the porgressbar
        based on the arguments, where
        iteration_timer - is the curretn iteration
        max_iteration - max iteration value
        max time is equel to 100 and out of time is equel to 0
        """
        assert iteration_timer >= 0 , "iteration_timer has to be positive!"
        assert max_iteration >= 0 , "max_iteration has to be positive!"

        if int(iteration_timer) <= 0:
            return 100
        elif int(iteration_timer) >= int(max_iteration):
            return 0
        else:
            return int(100-(100*iteration_timer/max_iteration))


    def __create_button(self, parent: tk.LabelFrame, text: str, **kwargs) -> tk.Button :
        """
        creating Button with the given parameters, and for teh given position,
        returns tk.Button
        it can take parameters:
        - bg - for background_color,
        - fg - for forground_color,
        - padx - for padding_x in grid,
        - row_num - for row in grid,
        - column_num - for column in grid,
        - text - to be displayed for the label
        - parent element - the parent frame it shoudl belong to
        - command - for command to the tk.Button
        """
        background_color = kwargs.get('bg', GUISettings.COLORS.WHITE)
        forground_color = kwargs.get('fg', None)
        padding_x = kwargs.get('padx', (0,0))
        padding_y = kwargs.get('pady',(0,0))
        row_num = kwargs.get('row', 0)
        button_width = kwargs.get('width',None)
        column_num = kwargs.get('column', 0)
        command = kwargs.get("command",None)

        new_button = tk.Button(
            parent,
            text=text,
            bg=background_color,
            fg=forground_color,
            width=button_width,
            command=command,
        )
        new_button.grid(
            column=column_num,
            row=row_num,
            padx=padding_x,
            pady=padding_y,
        )

        return new_button


    def __reset_to_start(self) -> None:
        """
        restart to start condition
        """
        # disable the button at the start
        self.button_restart['state'] = tk.DISABLED
        
        # starting config for input box
        self.user_input.config(
            state=tk.NORMAL,
            bg = GUISettings.COLORS.GREEN_ULTRA_LIGTH,
            )

        # insert placeholder
        self._insert_placeholder("Start typing...")

        # binding to any key pressed in the text box
        self.user_input.bind("<Key>",self._reset_timer)

        # setting the progess bar to 0
        self.time_progressbar['value'] = 100

        # changing the focus to the main window
        self.focus()