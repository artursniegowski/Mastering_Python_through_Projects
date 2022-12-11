"""
class for handling the user interface - speed test app
"""

import random
from settings import GUISettings
import tkinter as tk


class UI(tk.Tk):
    """
    class for handling the UI for speed test app
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

        # global settings for the timer - checking if the itmmer is running
        self.count_down_timer_finished = True

        # creating the object for text and typing
        # creating intro object
        self.create_intro()
        # creating scores, display text for typing and user input box objects
        self.create_speed_text_box()
        
    ############################################################################
    ########################## main gui parts ##################################
    ############################################################################
    def create_intro(self) -> None:
        """
        function for creating the intro - which includes, title and instuctions.
        """
        
        # title label
        self.typing_speed_test_label = tk.Label(
            text=GUISettings.MAIN_TITLE_LABEL,
            font=GUISettings.FONT_DEFAULT(24,font_name="Times"),
            fg=GUISettings.COLORS.WHITE,
            bg=GUISettings.COLORS.GREY,
        )
        self.typing_speed_test_label.grid(
            row=0,
            column=0,
            pady=10,
            ) 
        # instructions label
        self.instructions_label = tk.Label(
            text=GUISettings.INSTRUCTIONS_LABEL,
            font=GUISettings.FONT_DEFAULT(12,font_name="Times"),
            fg=GUISettings.COLORS.WHITE,
            bg=GUISettings.COLORS.GREY,
        )
        self.instructions_label.grid(
            row=1,
            column=0,
            pady=10,
            ) 

    def create_speed_text_box(self):
        """
        creating the three main component for the speed test,
        first are the scores,
        second is the text to be typed in
        third is the input where we should type the text
        """
        # 1: SCORES
        self._create_score_board()
        # 2: the text to be typed
        self._created_text()
        # 3: input for typing
        self._create_user_input()


    ############################################################################
    ########################## subparts for gui ################################
    ############################################################################ 
    def _create_user_input(self) -> None:
        """
        creating user input box
        """
        # the user input box
        self.user_input_box = tk.LabelFrame(
            border=2,
            bg = GUISettings.COLORS.GREEN,
            fg = GUISettings.COLORS.GREEN,
            borderwidth=2,
            highlightthickness=2,
            highlightcolor=GUISettings.COLORS.GREEN,
            width= 500,
            height = 50,
            font = GUISettings.FONT_DEFAULT(10),
            relief="ridge",
            labelanchor='n',        
        )
        self.user_input_box.grid(
            row=4,
            column=0,
            pady=(0,0),
        )
        self.user_input_box.grid_propagate(0)

        self.user_input = tk.Entry(
            self.user_input_box,
            bg = GUISettings.COLORS.GREEN_ULTRA_LIGTH,
            width=40,
            font=GUISettings.FONT_DEFAULT(18,font_name="Times",font_type="roman"),
            highlightcolor=GUISettings.COLORS.ORANGE,
            highlightbackground=GUISettings.COLORS.ORANGE,
            highlightthickness=4,
            justify=tk.CENTER,
        )
        self.user_input.pack()

        # insert placeholder
        self._insert_placeholder("type the words here")

        # for getting rid of the placeholder - and setting default black color for the font
        self.user_input.bind("<FocusIn>",self._user_input_erase_placeholder)
        # adding the spacebar/enter checks - everytime the spacebar/enter is pressed
        self.user_input.bind("<space>",self._check_user_word)
        self.user_input.bind("<Return>",self._check_user_word)
        # binding to any key
        self.user_input.bind("<Key>",self._start_timer)

    def _insert_placeholder(self, text:str) -> None:
        """
        inserts placeholder in the user input
        """
        self.user_input.config(
            fg=GUISettings.COLORS.GREY,
            state=tk.NORMAL,
        )
        self.user_input.delete(0,tk.END)
        self.user_input.insert(0,text)

    def _start_timer(self, event_object) -> None:
        """
        starting the countdown for time, only if the timer is currently NOT running
        """
        # restart the timer only if the timer has finished
        if self.count_down_timer_finished:
            self.__start_count_down(count=self.timer_count)
            # deactivaiting the binding
            self.user_input.unbind("<Key>")


    def _check_user_word(self, event_object) -> None:
        """
        checking user input if it matches the current word, and moving to the next one
        """
        if (user_word := self.user_input.get().strip()) != '': # check only if there is anything in the box
            # check if word list is out of range !!
            assert len(self.words_list) > (self.select_word_num + 1), "words_list is out of range!"
            if len(self.words_list) > (self.select_word_num + 1):
                # saving the curretn word into the old word so we can move to the next word
                self.old_word_index = self.__search_for_word_in_text(self.words_list[self.select_word_num])
    
                # if the words match
                if user_word == self.words_list[self.select_word_num]:
                    # selecting the corect word tag for the previous word
                    self.__create_correct_word_tag(self.old_word_index[0],self.old_word_index[1])

                    # addin values to the
                    self.CPM_count += len(user_word)
                    self.WPM_count += 1
                    # updating scores
                    self.__set_value_CPM(self.CPM_count)
                    self.__set_value_WPM(self.WPM_count)

                else:
                    # selecting the incorect word tag for the previous word
                    self.__create_incorrect_word_tag(self.old_word_index[0],self.old_word_index[1])

                # selecting the next word and finding its index
                self.select_word_num += 1
                self.current_word_index = self.__search_for_word_in_text(self.words_list[self.select_word_num])

                # moving the current tag to the next word
                self.__create_current_word_tag(self.current_word_index[0],self.current_word_index[1])

                # cleaning the entry widget
                self.user_input.delete(0,tk.END)
            else: # if it is out of range / raise an error
                raise ValueError("words_list is out of range !")

    def _user_input_erase_placeholder(self, event_object) -> None:
        """
        function for erasing the placeholder from the user input and 
        setting the new color of the font
        """
        self.user_input.delete(0,tk.END)
        self.user_input.config(
            fg=GUISettings.COLORS.BLACK
        )


    def _created_text(self) -> None:
        """
        creating text that is displayed and marked accordingly
        """
        self.text_box = tk.LabelFrame(
            # text=" TYPE THE TEXT ",
            bg = GUISettings.COLORS.GREY,
            fg = GUISettings.COLORS.WHITE,
            border=2,
            borderwidth=2,
            highlightthickness=2,
            highlightcolor=GUISettings.COLORS.WHITE,
            width= 500,
            height = 150,
            font = GUISettings.FONT_DEFAULT(10),
            relief="ridge",
            labelanchor='n',        
        )
        self.text_box.grid(
            row=3,
            column=0,
            pady=(0,0),
        )
        self.text_box.grid_propagate(0)

        # text intput
        self.text_to_type = tk.Text(
            self.text_box,
            width=40,
            height=3,
            font=GUISettings.FONT_DEFAULT(18,font_name="Times",font_type="roman"),
            state='disable',
            wrap='word',
            spacing1=5,
            spacing2=5,
            spacing3=2,
            bg=GUISettings.COLORS.GREY_LIGTH,
            padx=5,
        )
        self.text_to_type.pack()

        # adding words to the text wiget
        self.__create_words_for_text_widget()


        # starting with first word - index 0
        self.select_word_num = 0
        # make sure that the word list has actually words
        assert len(self.words_list) > 0, "Error: Your word list is empty. Check if your file data/words.txt has words in it!"
        
        # returns string index - start and end - position of the word
        self.current_word_index = self.__search_for_word_in_text(self.words_list[self.select_word_num])
        # selecting current word - with a tag
        self.__create_current_word_tag(self.current_word_index[0], self.current_word_index[1])

        # adding tags
        # adding incorrect - word tags base configuration
        self.text_to_type.tag_configure('incorrect_word',foreground=GUISettings.COLORS.RED)
        # adding correct word tags
        self.text_to_type.tag_configure('correct_word',foreground=GUISettings.COLORS.GREEN)


    def _create_score_board(self) -> None:
        """
        creates the scores, time left and reset button
        """
        # 1: SCORES - board
        self.speed_text_box = tk.LabelFrame(
            text=" STATS ",
            bg = GUISettings.COLORS.GREY,
            # fg = GUISettings.COLORS.WHITE,
            width= 500,
            height = 52,
            font = GUISettings.FONT_DEFAULT(10),
            relief="ridge",
            labelanchor='n',        
        )
        self.speed_text_box.grid(
            row=2,
            column=0,
            pady=(20,0),
        )
        self.speed_text_box.grid_propagate(0)


        self.label_correct_CPM = self.__create_label(
            self.speed_text_box,
            text="Correct CPM:",
            bg=GUISettings.COLORS.GREY,
            column=0,
            row=0,
            padx=(40,5),
        )
        self.label_correct_CPM_value = self.__create_label(
            self.speed_text_box,
            text="0",
            bg=GUISettings.COLORS.WHITE,
            column=1,
            row=0,
            padx=(0,15),
        )
        
        self.label_correct_WPM = self.__create_label(
            self.speed_text_box,
            text="Correct WPM:",
            bg=GUISettings.COLORS.GREY,
            column=2,
            row=0,
            padx=5,
        )
        self.label_correct_WPM_value = self.__create_label(
            self.speed_text_box,
            text="0",
            bg=GUISettings.COLORS.WHITE,
            column=3,
            row=0,
            padx=(0,15),
        )


        self.label_time_left = self.__create_label(
            self.speed_text_box,
            text="Time left:",
            bg=GUISettings.COLORS.GREY,
            column=4,
            row=0,
            padx=5,
        )
        self.label_time_left_value = self.__create_label(
            self.speed_text_box,
            text="0",
            bg=GUISettings.COLORS.WHITE,
            column=5,
            row=0,
            padx=(0,15),
        )

        self.button_restart = self.__create_button(
            self.speed_text_box,
            text="Restart",
            bg=GUISettings.COLORS.GREY,
            column=6,
            row=0,
            padx=(40,40),
            command=self.__reset_to_start,
        )

        # setting start values for the timer, WPM and CPM
        self.__reset_values_CPM_WPM_timer()


    ############################################################################
    ########################## helper gui parts ################################
    ############################################################################
    def __create_current_word_tag(self, start_index:str, end_index:str )-> None:
        """
        adds the current word tag to the text widget
        start_index and end_index are presented as string index
        """
        assert int(start_index.split('.')[1]) <= int(end_index.split('.')[1]), 'start_index has to be euqul smaller than end_index'
    
        # current word tag
        # first delete the current tags so we can add and leave only one on the text screen
        self.text_to_type.tag_delete('current_word')
        # self.text_to_type.tag_add('current_word','1.20','1.24')
        self.text_to_type.tag_add('current_word',start_index,end_index)
        self.text_to_type.tag_configure('current_word',background=GUISettings.COLORS.GREEN_LIGTH)
        # move to visibility the given index
        # self.text_to_type.see("1.173")
        self.text_to_type.see(start_index)

    def __create_incorrect_word_tag(self, start_index:str, end_index:str )-> None:
        """
        adds the incorrect word tag to the text widget
        start_index and end_index are presented as string index
        """
        assert int(start_index.split('.')[1]) <= int(end_index.split('.')[1]), 'start_index has to be euqul smaller than end_index'
        
        # adding incorrect word tag
        # self.text_to_type.tag_add('incorrect_word','1.6','1.8')
        self.text_to_type.tag_add('incorrect_word',start_index,end_index)

    def __create_correct_word_tag(self, start_index:str, end_index:str )-> None:
        """
        adds the correct word tag to the text widget
        start_index and end_index are presented as string index
        """
        assert int(start_index.split('.')[1]) <= int(end_index.split('.')[1]), 'start_index has to be euqul smaller than end_index'

        # adding correct word tag
        # self.text_to_type.tag_add('correct_word','1.0','1.4')
        self.text_to_type.tag_add('correct_word',start_index,end_index)

    def __create_words_for_text_widget(self) -> None:
        """
        loads words and fills into the text widget
        """
        # loading words from a file
        self.file_name ='data/words.txt'
        self.words_list = self.__load_words_from_file(self.file_name)
        # creating words as a string for the text widget
        TEXT_TO_ADD = "  ".join(self.words_list) # adding double spacing for readability

        # adding text to the widget
        self.__add_text_to_text_widget(TEXT_TO_ADD)


    def __add_text_to_text_widget(self, text:str) -> None:
        """
        adding text to text widget
        """
        # adding words tot the text widget
        self.text_to_type.config(state=tk.NORMAL)
        # self.text_to_type.insert(tk.END,TEXT_TO_ADD)
        self.text_to_type.delete('0.0',tk.END)
        self.text_to_type.insert('0.0',text)
        self.text_to_type.config(state=tk.DISABLED)

    def __create_label(self, parent: tk.LabelFrame, text: str, **kwargs) -> tk.Label :
        """
        creating label with the given parameters, and for teh given position,
        returns tk.Label
        it can take parameters:
        - bg - for background_color,
        - fg - for forground_color,
        - padx - for padding_x in grid,
        - row_num - for row in grid,
        - column_num - for column in grid,
        - text - to be displayed for the label
        - parent element - the parent frame it shoudl belong to
        """
        background_color = kwargs.get('bg', GUISettings.COLORS.WHITE)
        forground_color = kwargs.get('fg', None)
        padding_x = kwargs.get('padx', (0,0))
        row_num = kwargs.get('row', 0)
        column_num = kwargs.get('column', 0)

        new_label = tk.Label(
            parent,
            text=text,
            bg=background_color,
            fg=forground_color,
        )
        new_label.grid(
            column=column_num,
            row=row_num,
            padx=padding_x,
        )

        return new_label

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
        row_num = kwargs.get('row', 0)
        column_num = kwargs.get('column', 0)
        command = kwargs.get("command",None)

        new_button = tk.Button(
            parent,
            text=text,
            bg=background_color,
            fg=forground_color,
            command=command
        )
        new_button.grid(
            column=column_num,
            row=row_num,
            padx=padding_x,
        )

        return new_button

    ############################################################################
    ############################# gui functions ################################
    ############################################################################  
    def __start_count_down(self, count:int=60) -> None:
        """
        start timer, update value of the timer, 
        """
        if count > 0:
            self.count_down_timer_finished = False
            # updating the value of the counter
            self.__set_value_timer(count)
            # every second (1000ms) calling the same function with the count one second less
            self.timer_counter = self.after(1000,self.__start_count_down, count -1)
        else: 
            self.__set_value_timer(0)
            self.count_down_timer_finished = True


            self.user_input.delete(0,tk.END)
            self.user_input.config(
                disabledforeground=GUISettings.COLORS.RED,
            )
            self.user_input.insert(0,"Time is up! CHECK YOUR SCORE!")
            # deactivating the user input
            self.user_input.config(
                state=tk.DISABLED,
            )

            # unbinding events 
            self.user_input.unbind("<space>")
            self.user_input.unbind("<Return>")

            # highlight scores !
            self.label_correct_CPM_value.config(
                bg=GUISettings.COLORS.YELLOW,
            )
            self.label_correct_WPM_value.config(
                bg=GUISettings.COLORS.YELLOW,
            )


    
    def __reset_values_CPM_WPM_timer(self) -> None:
        """
        reseting back to start the values for CPM, WPM and timmer
        """

        self.CPM_count = 0
        self.WPM_count = 0
        self.timer_count = 60

        self.__set_value_CPM(self.CPM_count)
        self.__set_value_WPM(self.WPM_count)
        self.__set_value_timer(self.timer_count)


    def __reset_to_start(self) -> None:
        """
        reseting everything to the state as it was before starting,
        start again, stoping timer 
        """
        # stoping the timer , and setting back the timer global variable
        if not self.count_down_timer_finished: # if timer is runing stop it
            self.after_cancel(self.timer_counter)
        self.count_down_timer_finished = True

        # binding to any key - for starting the timer
        self.user_input.bind("<Key>",self._start_timer)
        # adding the spacebar/enter checks - everytime the spacebar/enter is pressed
        self.user_input.bind("<space>",self._check_user_word)
        self.user_input.bind("<Return>",self._check_user_word)

        # reseting the score values
        self.__reset_values_CPM_WPM_timer()

        # adding placeholder - reseting values
        self._insert_placeholder("type the words here")

        # reseting the text to type widget - reloading the words
        self.__create_words_for_text_widget()

        # change focus to the main text
        self.text_to_type.focus_set()

        # starting with first word - index 0
        self.select_word_num = 0
        self.current_word_index = self.__search_for_word_in_text(self.words_list[self.select_word_num])

        # moving the current tag to first word
        self.__create_current_word_tag(self.current_word_index[0],self.current_word_index[1])

        # changing back to normal the color of background
        self.label_correct_CPM_value.config(
            bg=GUISettings.COLORS.WHITE,
        )
        self.label_correct_WPM_value.config(
            bg=GUISettings.COLORS.WHITE,
        )


    def __set_value_timer(self, value:int = 0) -> None:
        """
        function for setting the value for the timer
        """
        self.label_time_left_value.config(text=str(value))

    def __set_value_CPM(self, value:int = 0) -> None:
        """
        function for setting the value for CPM (Character per minute)
        """
        self.label_correct_CPM_value.config(text=str(value))

    def __set_value_WPM(self, value:int = 0) -> None:
        """
        function for setting the value for WPM (word per minute)
        """
        self.label_correct_WPM_value.config(text=str(value))

    def __load_words_from_file(self, file_name: str) -> list[str]:
        """
        loads words from a txt file and converts them to a list
        at the end change the order of words in the list to make it more random
        and return the list
        if file not found then it returns a emty list
        """
        words = []
        try:
            with open(file_name,'r') as f:
                words = f.read().splitlines()
        except FileNotFoundError:
            print(f"ERROR: File not Found: {file_name}\nDo you have the right directory?\nDoes the path {file_name} exist?")
            raise FileNotFoundError(f"cant locate {file_name}")
        else:
            # change the order to make it more random
            random.shuffle(words)

        return words
    
    def __search_for_word_in_text(self, word:str, start_index_for_search:str = "1.0") -> tuple[str, int]:
        """
        Searching for a given word in the text widget 
        if found returns the start and end position of the word as text index 
        if not found returns emty tuple of strings
        """
        # find the word - start index , and length of the variable

        # for the length
        size_var = tk.IntVar()
        # for the start index
        start_index_word = self.text_to_type.search(
                r"\y{search_word}\y".format(search_word=word),
                index=start_index_for_search,
                stopindex=tk.END, 
                count=size_var, 
                regexp=True,
                )

        # calulating the end index based on the start index and its length
        # adding two values
        end_index_word = ''
        if start_index_word:
            # '1.12'
            new_index = start_index_word.split('.')
            new_index[1] = str(size_var.get()+int(start_index_word.split('.')[1]))
            end_index_word = '.'.join(new_index)
            
        return (start_index_word,end_index_word)