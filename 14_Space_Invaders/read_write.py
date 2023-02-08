# class managint the read and write operations of the game

from create_path import return_path
import json
from my_settings import MySettings


class read_write_game:
    """Class for managing the read and writing instruction for the game"""
    
    def __init__(self, my_settings : MySettings) -> None:
        
        self.my_settings = my_settings
        self.path = return_path(self.my_settings.subfolder_name,self.my_settings.file_name_json)

    def read_json(self, atribute : str = 'r') -> dict :
        """function for reading from the file"""
        return self.__write_read(atribute)

    def write_json(self, game_stats : dict, atribute : str = 'w') -> None :
        """function for writing to the file"""
        self.__write_read(atribute,game_stats)

    def __write_read(self, atribute : str, game_stats : dict =  {}) -> dict :
        """Function for reading and writing files"""
        """in read mode it returns a dict of the data read """
        """in write mode it returns a dict of data wrote"""
        json_data = game_stats 
        if atribute == 'r' or atribute == 'w':
            try: 
                with open(self.path,atribute) as file:
                    if atribute == 'r':
                        json_data = json.load(file)
                    elif atribute == 'w':
                        json.dump(json_data,file)
            except FileNotFoundError:
                with open(self.path,'w') as file:
                    json_data = {"high_score":0}
                    json.dump(json_data,file)
            except:
                print("Reading - Writing error file {}".format(self.path))
                print("Maybe an empty file or not json compatible")
        return json_data

    def return_high_score(self) -> int :
        """Returning high score from the file if the dictionary is not empty"""        
        dict_stats  =  self.read_json()
        if(len(dict_stats)>0) and "high_score" in dict_stats: # dict not empty
            # return high_score
            return dict_stats["high_score"] 
        else:
            return 0

    def write_high_score(self,high_Score: int, __key_dict : str = "high_score")-> None :
        """Writing high score to the file"""        
        dict_stats = {}
        dict_stats[__key_dict] = high_Score
        self.write_json(dict_stats)