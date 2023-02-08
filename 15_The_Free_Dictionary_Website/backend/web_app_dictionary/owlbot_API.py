# this is a class responsible for cuminicating with the public API : https://owlbot.info/
# to retrvide the word from the dictionary
import requests 
from env_variables import OWLBOT_API_Token

class OwlDataSettings:
    """settings for the public API https://owlbot.info/
    """
    # https://owlbot.info/api/v4/dictionary/{word}
    OWLBOT_ENDPOINT = "https://owlbot.info/api/v4/"

class OwlData:
    """class responsible for comunicating with the public API https://owlbot.info/
    """

    def __init__(self, owlbot_api_token:str = OWLBOT_API_Token, owlbot_api_endpoint:str = OwlDataSettings.OWLBOT_ENDPOINT) -> None:
        """init data for the API
        """
        self.endpoint_for_dictionary = owlbot_api_endpoint+"dictionary/"
        self.headers = {
            'Authorization': 'Token '+ owlbot_api_token
        }

    def get_data(self, search_word: str) -> dict:
        """making the request for the public API and returning the dictionary with data
        """
        assert isinstance(search_word,str), "Error: search_word has to be a string"
        assert len(search_word.strip())>1, "Error: search_word cant be an empty string"

        # adjusting the endpoint for thw search word
        self.search_endpoint = self.endpoint_for_dictionary + search_word

        # making the public API call
        response = requests.get(
            url=self.search_endpoint,
            headers=self.headers,
        )

        # for debuging
        # print(response.text)
        # print(response.content.decode("utf-8"))
        # print(response.status_code)
        # print(response.url)
        # print(response.content)
        # response.raise_for_status()
        try :
            # if we cant pars to json the response we will add an error message
            res: dict = response.json()
        except requests.exceptions.JSONDecodeError:
            res: dict = {}
            text = response.text
            # when the API returns a HTML file instead of JSON !!!
            error_message = text.split("<title>")[1].split("</title>")[0]
            res['exception'] = 'requests.exceptions.JSONDecodeError'
            res['status_code'] = response.status_code
        else:
            error_message = None

        # return data
        if response.status_code == 200:
            return {
                'status_code': response.status_code if not error_message else int(error_message[6:9]),
                'search_word': res.get('word', None),
                'pronunciation': res.get('pronunciation', None),
                'definitions': res.get('definitions',None),
                'exception': res.get('exception',None),
                'error_message': error_message
            }
        elif response.status_code == 404:
            return {
                'status_code': response.status_code,
                'info': res, #response.content.decode("utf-8")
                'error_message': error_message
            }
        elif response.status_code == 401 or response.status_code == 429:
            return {
                'status_code': response.status_code,
                'info': res, #response.content.decode("utf-8")
                'error_message': error_message
            }
        else: 
            return {
                'status_code': response.status_code,
            }