# this is a class used to convert a list of dictionaries to a a csv files
import pandas as pd
from pathlib import Path
import os

class DictCsvConverterSettings:
    """settings for the class DictCsvConverter
    """
    DEFAULT_FOLDER = 'output'

class DictCsvConverter:
    """this class is used to convert a list of dictioraies into a csv file
    and saving this file in the outpur folder
    """
    def __init__(self, file_name: str="my_file_out.csv") -> None:
        self.file_name = file_name

    def save_to_csv(self, food_list : list[dict]) -> bool:
        """
        function that saves the list of dictionaries into a csv file
        returns True if successful and False if not 
        """
        print("Log: Start saving...")
        # converitng data into a pandas DataFrame, this way it will be easy to save it later
        if food_list:
            df = pd.DataFrame(food_list)
            path_to_save = self.__get_the_path_to_save_file()
            df.to_csv(path_to_save, index=True, header=True)
            print("Log: Saving to file successful!")
            print(f"Log: saved to {path_to_save}.")
            return True

        print("Log: Saving to file Failed!")
        return False

    def __get_the_path_to_save_file(self) -> str:
        """returns the absolute path where to save the file
        """
        return (Path(__file__).parent / os.path.join(DictCsvConverterSettings.DEFAULT_FOLDER, self.file_name )).resolve()

    def set_new_file_name(self, new_file_name:str) -> None:
        """setting new file name, like Example: output.csv
        """
        self.file_name = new_file_name

    @property
    def file_name(self):
        """getter for file_name"""
        return self.__file_name
    
    @file_name.setter
    def file_name(self, value):
        """setter for file_name"""
        assert isinstance(value,str), "Error: file_name has to be of type str!"
        assert 'csv' in value, "Error: Wrong file_name! Example: output.csv - did you forget the csv?"
        assert '.' in value, "Error: Wrong file_name! Example: output.csv - did you forget the dot?"
        assert len(value)>4 , "Error: Wrong file_name! Example: output.csv - did you forget the name of the file?"
        
        self.__file_name = value