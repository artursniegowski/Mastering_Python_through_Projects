# loading env variables
from dotenv import load_dotenv
load_dotenv()
import os

################################################################################
## sensitive data ###
#####################
# env variables ! - dont change here !
################################################################################
# Your viceRSS API KEY
# https://www.voicerss.org/api/
# https://www.voicerss.org/personel/
VoiceRSS_API_KEY = os.environ.get("VoiceRSS_API_KEY")
# VoiceRSS - API Endpoint
VoiceRSS_API_ENDPOINT = os.environ.get("VoiceRSS_API_ENDPOINT")
################################################################################
