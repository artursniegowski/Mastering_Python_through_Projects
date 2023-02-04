# the main file
from ui import UI

if __name__ == '__main__':
    # creating GUI object
    GUI_disappearing_text_app = UI()
    # waiting on the user to close the window
    GUI_disappearing_text_app.mainloop()