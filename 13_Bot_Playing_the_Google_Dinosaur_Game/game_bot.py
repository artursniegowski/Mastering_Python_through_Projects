# class for managing the bot - Playing_the_Google_Dinosaur_Game
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# for easy interaction witht he browser - like sending keys
# PyAutoGUI lets your Python scripts control the mouse and keyboard to automate 
# interactions with other applications. The API is designed to be simple
import pyautogui
# for managing the Image
from PIL import Image, ImageGrab
from io import BytesIO
# for managing time delays
import time
# for reading the absolute path to the files
from pathlib import Path
import os
# open Cv for image porcessing - it can detect obstacles faster than pyautogui
import cv2 as cv
import numpy as np

class GameBotSettings:
    """Settings for thr GameBot
    """
    # game url
    GAME_URL = "https://elgoog.im/t-rex/"
    # setting the option for the chrom webdriver - browse
    # make sure the indows start with full screen
    CHROME_OPTIONS = webdriver.ChromeOptions()
    CHROME_OPTIONS.add_argument('--hide-scrollbars')
    CHROME_OPTIONS.add_argument('--lang=en')
    CHROME_OPTIONS.add_argument('--force-device-scale-factor=1')
    # CHROME_OPTIONS.add_argument('--start-fullscreen')
    CHROME_OPTIONS.add_argument('--start-maximized')
    # adding an extensions
    CHROME_OPTIONS.add_argument('--load-extension={}'.format(r"C:\Users\AS-Computer\AppData\Local\Google\Chrome\User Data\Default\Extensions\ggaabchcecdbomdcnbahdfddfikjmphe\2.12.13_0"))
    # CHROME_OPTIONS.add_argument('--load-extension={}'.format(r"YOUR EXTENSION PATH GOES IN HERE"))
    # files names 
    FILE_NAMES = {
        'cactus_01':"cactus_01.png",
        'cactus_02':"cactus_02.png",
        'cactus_part_03':"cactus_part_03.png",
        'dino':"dino.png",
        'game_over': "game_over.png"
    }
    #  folder name for the files
    FOLDER_NAME = "templates"
    # file paths 
    FILE_PATHS_ABSOLUTE = {
        'cactus_01': str((Path(__file__).parent / os.path.join(FOLDER_NAME, FILE_NAMES['cactus_01'] )).resolve()),
        'cactus_02': str((Path(__file__).parent / os.path.join(FOLDER_NAME, FILE_NAMES['cactus_02'] )).resolve()),
        'cactus_part_03': str((Path(__file__).parent / os.path.join(FOLDER_NAME, FILE_NAMES['cactus_part_03'] )).resolve()),
        'dino': str((Path(__file__).parent / os.path.join(FOLDER_NAME, FILE_NAMES['dino'] )).resolve()),
        'game_over': str((Path(__file__).parent / os.path.join(FOLDER_NAME, FILE_NAMES['game_over'] )).resolve()),
    }
    


class GameBot:
    """class managing the Game bot
    """
    def __init__(self, chrome_driver_path: str) -> None:
        #  creating service for the chrome driver
        self.chrome_driver_service = Service(chrome_driver_path)
        # starting the chrom driver service
        self.chrome_driver_service.start()
        # creating the webdriver
        # self.driver = webdriver.Chrome(service=self.chrome_driver_service)
        self.driver = webdriver.Remote(self.chrome_driver_service.service_url, options=GameBotSettings.CHROME_OPTIONS)
        # to use action chains
        self.action_chains = ActionChains(self.driver)
        # load in the obstacles images for OpenCV
        # the 0 argument will make sure that the images will gget converted to gray scale
        self.CACTUS_01_PICTURE_CV = cv.imread(GameBotSettings.FILE_PATHS_ABSOLUTE['cactus_01'],0)
        self.CACTUS_02_PICTURE_CV = cv.imread(GameBotSettings.FILE_PATHS_ABSOLUTE['cactus_02'],0)
        self.CACTUS_PART_03_PICTURE_CV = cv.imread(GameBotSettings.FILE_PATHS_ABSOLUTE['cactus_part_03'],0)
        self.GAME_OVER_PICTURE_CV = cv.imread(GameBotSettings.FILE_PATHS_ABSOLUTE['game_over'],0)
        # treshold for openCV
        self.THRESHOLD_CV = 0.78
        # open the game website
        self.__start_game_website()

        # adjustem value for detecting obstacles
        self.adjustment = 0
        self.min_distance = 45

    

    def __start_game_website(self, url:str = GameBotSettings.GAME_URL) -> None:
        """function for opening the game website
        """
        self.driver.get(url)
        # wait for the website to load # Let the user actually see something!
        time.sleep(3)

    def close_the_game(self) -> None:
        """function for closing the webdriver
        """
        print("Closing the Web-driver...")
        self.driver.quit()


    def __wait_for_element(self, time_to_wait_in_sec: int, error_message: str, \
        locator_strategy: By, selector: str) -> WebElement:
        """function to wait for an element presence, and then returns this element
        if not found in a given time a Timeout exception will occure and the function will close the driver and 
        raise a TimeoutException
        """
        assert isinstance(time_to_wait_in_sec,int), "Error: time_to_wait_in_sec has to be an int"
        assert time_to_wait_in_sec > 0, "Error: time_to_wait_in_sec has to be greater than one sec"

        try:
            result_element = WebDriverWait(self.driver, time_to_wait_in_sec).until(
                EC.presence_of_element_located((locator_strategy, selector))
            )
            return result_element
        except TimeoutException as time_out:
            print(type(time_out))
            print(error_message)
            # quit the driver since the elemtn cant be found
            self.close_the_game()
            # raise a timeout exception
            raise TimeoutException

    def __dino_jump(self) -> None:
        """sends to the browser the up button -
        this makes the dino jump
        """
         # sending an arrow key up to the browser - this will make the dino jump
        # witouth selecting an element - with SELENIUM
        # self.action_chains.send_keys(Keys.UP).perform()
        ### OR ###
        # using pyautogui to press the up arrow - 
        pyautogui.press("up")
        # adjust for the speed
        self.__adjust_the_time_of_jump_for_the_speed_of_the_dino()
        # print("current_speed",self.__get_dino_current_speed())
        # print("adjustment",self.adjustment)



    def __get_dino_current_speed(self) -> float:
        """returns the curretn speed of the dino on the website, by taping into the javacript
        object created by the website and retriving the value of the speed for this object
        """
        return self.driver.execute_script("return Runner.instance_.currentSpeed")

    def __adjust_the_time_of_jump_for_the_speed_of_the_dino(self) -> None:
        """adjusting the variable self.min_distance which helps to determinate how much in advance should 
        the dino jump, this will be adjust based on the current speed of the dino
        """
        # self.min_distance for the speed to jump faster
        self.current_speed = self.__get_dino_current_speed()
        print("Current Speed",self.current_speed)
        if self.current_speed:
            if  int(self.current_speed-6) <= 4:
                self.min_distance = 48 + (int(self.current_speed-6))*33
            else: 
                self.min_distance = 70 + (int(self.current_speed-6))*27
        else: 
            print("Speed: None")
            self.min_distance = self.min_distance
        print(self.min_distance)


    def __define_regions_for_search(self) -> None:
        """function used to define the regions for the search for pyautogui
        """
        # regions used for pyautogui.locateOnScreen
        # (a 4-integer tuple of (left, top, width, height))
        self.region_to_search_dino=(
        int(self.dino_pos.left),
        int(self.dino_pos.top-self.dino_pos.height/2),
        int(self.main_frame_element.rect['width']/2),
        int(self.dino_pos.height+self.dino_pos.height/2+10)
        )
        self.region_to_search_cactus=(
        int(self.dino_pos.left+self.dino_pos.width-2),
        int(self.dino_pos.top-self.dino_pos.height/2),
        int(90),
        # int(self.main_frame_element.rect['width']/2-self.dino_pos.width/2),
        int(self.dino_pos.height+self.dino_pos.height/2+10)
        )

        # regions used for openCV function as 
        # bbox = left,upper,right,lower
        # https://chayanvinayak.blogspot.com/2013/03/bounding-box-in-pilpython-image-library.html
        self.region_for_openCV_search_cactus = (
            int(self.dino_pos.left+self.dino_pos.width-2),
            int(self.dino_pos.top-self.dino_pos.height/4),
            int(self.dino_pos.left + self.main_frame_element.rect['width']),
            # int(self.dino_pos.left + self.dino_pos.width*5),
            int(self.dino_pos.top+self.dino_pos.height*5/4),
        )
        # (694, 389, 854, 455)
        # print(self.region_for_openCV_search_cactus)
        self.region_for_openCV_search_game_over = (
        int(self.dino_pos.left+self.main_frame_element.rect['width']/2-50),
        int(self.dino_pos.top-50),
        int(self.dino_pos.left+self.main_frame_element.rect['width']/2+50),
        int(self.dino_pos.top+50)
        )

    def check_for_obstacles(self) -> None:
        """checks for obstacles and if necessary perfomr a jump
        """

        if self.dino_end_pos:
            # using the pyautogui.locateOnScreen is quiet slow this is why i choose to use openCV which is faster 
            # locateAllOnScreen
            # example with pyautogui
            # cactus_01 = pyautogui.locateOnScreen('templates/cactus_01.png',confidence=0.9, region=self.region_to_search_cactus, grayscale=True)
            # cactus_02 = pyautogui.locateOnScreen('templates/cactus_02.png',confidence=0.9, region=self.region_to_search_cactus, grayscale=True)
            # print(list(cactus_all_01))
            # print(list(cactus_all_02))
            # if cactus_01 and ((cactus_01.left - 60) <= self.dino_end_pos <= (cactus_01.left+15)):
            #     self.__dino_jump()
            # elif cactus_02 and ((cactus_02.left - 60) <= self.dino_end_pos <= (cactus_02.left+15)):
            #     self.__dino_jump()

            # using openCv to find the obstacles in the picture
            # bbox = left,upper,right,lower
            # grabing the image in front of the dino - this is the range that will be checked for obstacles
            img_current = ImageGrab.grab(bbox=self.region_for_openCV_search_cactus)
            img_current_game_over = ImageGrab.grab(bbox=self.region_for_openCV_search_game_over)
            # img_current_game_over.show()

            # getting the areaas of interest for the game
            img_current_grey_cv = cv.cvtColor(np.array(img_current), cv.COLOR_BGR2GRAY)
            img_current_game_over = cv.cvtColor(np.array(img_current_game_over), cv.COLOR_BGR2GRAY)
            # results of our search for game over image
            res_game_over = cv.matchTemplate(img_current_game_over, self.GAME_OVER_PICTURE_CV, cv.TM_CCOEFF_NORMED)
            # checking for obstacle number 1 - cactus type 1
            res_cactus_01 = cv.matchTemplate(img_current_grey_cv, self.CACTUS_01_PICTURE_CV, cv.TM_CCOEFF_NORMED)
            # checking for obstacle number 2 - cactus type 2
            res_cactus_02 = cv.matchTemplate(img_current_grey_cv, self.CACTUS_02_PICTURE_CV, cv.TM_CCOEFF_NORMED)
            # saving the results that satisfy the finding og the objects
            loc_res_1 = np.where(res_cactus_01 >= self.THRESHOLD_CV)
            # saving the results that satisfy the finding og the objects
            loc_res_2 = np.where(res_cactus_02 >= self.THRESHOLD_CV)

            # game over picture found
            if np.any(res_game_over >= self.THRESHOLD_CV):
                # setting back the adjustement value
                self.adjustment = 0
                # setting back the min distance for the jump
                self.min_distance = 0

                # start again after game over
                self.__dino_jump()
            else: # if not game over keep looking for obstacles
                
                # a list of x positions of the obstacles 
                min_positions_of_obstacles = []

                if np.any(loc_res_1[0]): 
                    # if the obstacle found in close proximity of the dino we send command to jump
                    # if loc_res_1[-1][0] < (self.min_distance + self.adjustment):
                    if np.min(loc_res_1[-1]) < (self.min_distance + self.adjustment):
                        # chaning ghee adjustment value back to initial value
                        self.adjustment = 0
                        # make the dino jump
                        self.__dino_jump()
                    
                    # print("new point res1")
                    # pt (x,y) - helpful if wanting to draw a rectagle
                    # https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html
                    list_set1 = set()
                    for pt in zip(*loc_res_1[::-1]):
                        # print("res1",pt)
                        list_set1.add(pt[0])
                    # prinint the found points of obstacles ! as a list 
                    # print(np.min(loc_res_1[-1]), list_set1)
                    
                    # creating the list with min values
                    if list_set1:
                        min_positions_of_obstacles.append(min(list_set1))
                        list_set1.remove(min(list_set1))
                        if len(list_set1) >= 1:
                            min_positions_of_obstacles.append(min(list_set1))
                            list_set1.remove(min(list_set1))

                    
                if np.any(loc_res_2[0]): 
                    # if the obstacle found in close proximity of the dino we send command to jump
                    # if loc_res_2[-1][0] < (self.min_distance + self.adjustment):
                    if np.min(loc_res_2[-1]) < (self.min_distance + self.adjustment):
                        # chaning ghee adjustment value back to initial value
                        self.adjustment = 0
                        # make the dino jump
                        self.__dino_jump()

                    # print("new point res2")
                    # pt (x,y) - helpful if wanting to draw a rectagle
                    # https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html
                    list_set2 = set()
                    for pt in zip(*loc_res_2[::-1]):
                        # print("res2",pt)
                        list_set2.add(pt[0])
                    # prinint the found points of obstacles ! as a list 
                    # print(np.min(loc_res_2[-1]), list_set2)

                    # creating the list with min values between obstacles to add the adjustement if the obctacles
                    # are close to each other so we can jump in between
                    if list_set2:
                        min_positions_of_obstacles.append(min(list_set2))
                        list_set2.remove(min(list_set2))
                        if len(list_set2) >= 1:
                            min_positions_of_obstacles.append(min(list_set2))
                            list_set2.remove(min(list_set2))

                if len(min_positions_of_obstacles) >= 2:
                    firs_min_x_obstacles = min_positions_of_obstacles.pop(min_positions_of_obstacles.index(min(min_positions_of_obstacles)))
                    second_min_x_obstacles = min_positions_of_obstacles.pop(min_positions_of_obstacles.index(min(min_positions_of_obstacles)))

                    if 70 < abs(firs_min_x_obstacles-second_min_x_obstacles) < 250:
                        print("Adjusted for earlier jump")
                        self.adjustment = 75
                    
        else:
            # locating the dino picture on the screen
            # this method is slow but good enough bc it will be called until the dino is located
            self.dino_pos = pyautogui.locateOnScreen(GameBotSettings.FILE_PATHS_ABSOLUTE['dino'],confidence=0.9)
            self.dino_end_pos = self.dino_pos.left + self.dino_pos.width
            self.__define_regions_for_search()


    def wait_for_bot_read(self) -> None:
        """getting the bot ready
        """
        # checking if we can find the canvas element with the dinosaur
        self.main_frame_element = self.__wait_for_element(
            time_to_wait_in_sec=5,
            locator_strategy=By.CLASS_NAME,
            selector="runner-canvas",
            error_message="Error: Cant find the main element frame!",
        )
        # dimensions of the frame element
        # print(self.main_frame_element.rect)
 
        # im.show()
        # locating the dino picture on the screen
        # this method is slow but good enough at the beginign to locate the picture - where the dino is
        self.dino_pos = pyautogui.locateOnScreen(GameBotSettings.FILE_PATHS_ABSOLUTE['dino'],confidence=0.9)
        if self.dino_pos:
            self.dino_end_pos = self.dino_pos.left + self.dino_pos.width
            self.__define_regions_for_search()
        else:
            self.dino_end_pos = None

        # start the game - with a jump you can start the game
        self.__dino_jump()