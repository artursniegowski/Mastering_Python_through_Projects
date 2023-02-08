# this is a class managing the convertsion text -> speach (audio)
#  https://www.voicerss.org/api/s
import requests
from env_variables import VoiceRSS_API_KEY, VoiceRSS_API_ENDPOINT


class LanguagesVoiceRSS:
    """
    possible languages
    Parameter name: 'hl'
    https://www.voicerss.org/api/
    """
    ENGLISH_CANADA = 'en-ca'
    ENGLISH_GREAT_BRITAIN = 'en-gb'	
    ENGLISH_UNITED_STATES = 'en-us'
    GERMANY = 'de-de'
    # default value
    DEFAULT = ENGLISH_UNITED_STATES

    @classmethod
    def is_included(cls, given_value: str) -> bool:
        """
        check if given value is part of the values in the class
        """
        return given_value in vars(cls).values()


class AudioCodecsVoiceRSS:
    """
    The speech audio codec
    Parameter name: 'c'
    https://www.voicerss.org/api/
    """
    MP3 = 'MP3'
    WAV = 'WAV'
    AAC = 'AAC'
    # default value
    DEFAULT = WAV

    @classmethod
    def is_included(cls, given_value: str) -> bool:
        """
        check if given value is part of the values in the class
        """
        return given_value in vars(cls).values()


class SpeedVoiceRSS:
    """
    The Speed for the app
    Parameter name: 'r'
    https://www.voicerss.org/api/
    """
    SLOW_SUPER = -10
    SLOW = -4
    NORMAL = 0
    FASTER = 2
    FAST = 4
    FAST_SUPER = 10
    # default value
    DEFAULT = NORMAL

    @classmethod
    def is_included(cls, given_value: str) -> bool:
        """
        check if given value is part of the values in the class
        """
        return given_value in vars(cls).values()

class TextAudioConverterSettings:
    """
    settings for the class TextAudioConverter for converting text to data
    VoiceRSS
    https://www.voicerss.org/api/
    """
    # languages
    voicerss_hl = LanguagesVoiceRSS()
    # audio codec
    voicerss_c = AudioCodecsVoiceRSS()
    # voice speed
    voicerss_r = SpeedVoiceRSS()

class TextAudioConverter():
    """
    This class manages the API VoiceRSS to convert the text to speach Audio
    """
    
    def __init__(self, api_endpoint:str = VoiceRSS_API_ENDPOINT, api_key:str = VoiceRSS_API_KEY) -> None:
        """
        init data for the VoiceRSS API
        """
        self.api_endpoint = api_endpoint
        self.api_key = api_key


    def convert_text_to_sound(self, text: str, 
                                file_name: str = "sound", 
                                format: AudioCodecsVoiceRSS = TextAudioConverterSettings.voicerss_c.DEFAULT, 
                                langugage: LanguagesVoiceRSS = TextAudioConverterSettings.voicerss_hl.DEFAULT,
                                voice_speed: SpeedVoiceRSS = TextAudioConverterSettings.voicerss_r.DEFAULT,
                                ) -> None:
        """
        converts the given text to sound
        and saves the sound in the given file
        """
        assert AudioCodecsVoiceRSS.is_included(format), f"Error: {format} is not included in defined AudioCodecsVoiceRSS class"
        assert LanguagesVoiceRSS.is_included(langugage), f"Error: {langugage} is not included in defined LanguagesVoiceRSS class"
        assert SpeedVoiceRSS.is_included(voice_speed), f"Error: {voice_speed} is not included in defined SpeedVoiceRSS class"
     

        # checking if the values provided are defined in the class
        if AudioCodecsVoiceRSS.is_included(format) and LanguagesVoiceRSS.is_included(langugage) :

            print("started - text to audio conversion ...")

            parameters = {
                'key': self.api_key,
                'hl': langugage,
                'c': format,
                'r': voice_speed,
                'src':text,
            }

            # making the api request
            response = requests.post(self.api_endpoint, params=parameters)
            response.raise_for_status()

            if response.status_code == 200:
                # if the respons was successful
                self.__save_data(
                    data=response.content,
                    file_name=file_name,
                    format=format,
                    )
            else:
                print(f"Error: the respons ended up with an error {response.status_code}!")
        else:
            print("Error: format or language have not the defined type!")

    def __save_data(self, data: bytes, file_name:str, format: AudioCodecsVoiceRSS) -> None:
        """
        saves the bytes as sound file with the given format
        """
        if AudioCodecsVoiceRSS.is_included(format):
            with open(f'{file_name}.{format}','wb') as f:
                f.write(data)
            print(f"You audiobook is ready: '{file_name}.{format}' .")
            print("completed - text to audio conversion.")
        else:
            print("Error: Wrong format!")