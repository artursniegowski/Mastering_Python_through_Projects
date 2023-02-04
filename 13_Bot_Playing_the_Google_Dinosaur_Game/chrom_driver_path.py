import os
from pathlib import Path
####################### SELENIUM SETTINGS ######################################
# adjust this path to wherever you have unpacked the chrome driver file !      
# dont forget that the verion of chrome drive has to match the verison of 
# chrome browser
# https://chromedriver.chromium.org/downloads
# relative path, 
# CHROME_DRIVER_PATH = "ChromeDriver_browser/chromedriver.exe"
# or you can use as well absolute path !
CHROME_DRIVER_PATH = (Path(__file__).parent / os.path.join("ChromeDriver_browser","chromedriver.exe" )).resolve()
################################################################################