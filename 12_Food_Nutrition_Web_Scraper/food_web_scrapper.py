# class for scraping data
from bs4 import BeautifulSoup
import requests
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
import lxml # for parsing html
import re 

class MyHeader:
    """define your header
    You'll need to pass along some headers in order for the request to return the actual website HTML
    go to http://myhttpheader.com/ to check these values and update them accordingly. 
    """
    HEADER = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language":"en-US,en;q=0.9,de;q=0.6,la;q=0.5,ar;q=0.4",
        "Accept-Encoding":"gzip, deflate",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    }


class FoodScraperSettings:
    """class with the settings for FoodScraper
    """
    FOOD_NUTRITION_BASE_URL = "https://www.nutritionvalue.org"
    FOOD_NUTRITION_SEARCH_URL = "https://www.nutritionvalue.org/search.php?food_query="
    FOOD_SEARCH_WORD = lambda food_word:  food_word.strip().replace(" ","%20")
    # creating the search url of the given food
    SEARCH_URL = lambda food_name_to_search_for : f"{FoodScraperSettings.FOOD_NUTRITION_SEARCH_URL}{FoodScraperSettings.FOOD_SEARCH_WORD(food_name_to_search_for)}"


class FoodScraper:
    """class used for scraping nutrition data on various food from
    https://www.nutritionvalue.org/
    """
    def __init__(self, **kwargs) -> None:
        self.headers = kwargs.get('headers',None)

    def _serch_for_food(self, food: str) -> None | str:
        """
        this function will return all the links that shoudl be scraped for data nutrition
        returns None if cant find the value of an error occured
        returns the search link if successful
        """
        assert isinstance(food, str), "food variables has to be of type str!"
        assert len(food) > 0, "food variable cant be an empty string!"

        # first getting the raw data from the website - the serach url 
        # gets raw data from the given website,
        # the response will be populated with that data. 
        # the soup object will be poppulated with data
        # The text() method of the Request interface reads the request body and 
        # returns it as a promise that resolves with a String. 
        # The response is always decoded using UTF-8.
        response = requests.get(
            url = FoodScraperSettings.SEARCH_URL(food),
            headers = self.headers, 
        )
        # checking for Http error if one occured and terminate the porgram
        response.raise_for_status()
        # in case of encoding problems - if the encoding cant be resolved from the request
        # response.encoding = "UTF-8"
        # for debuging
        # print(response.encoding) 
        # print(response.status_code)
        # print(response.text)

        # if the website was properly read, and we got the rigth HTTP reponse
        if (response.status_code == 200):
            # getting bs4 / BeautifulSoup object
            soup = BeautifulSoup(response.text,"lxml")
            
            # look for all the links in response
            # first select up to 3 elements that include the class table_item_name
            # just in case we want later to check the first 3 elements
            all_table_items = soup.select(selector="a.table_item_name", limit=3)  

            if len(all_table_items) > 0:
                # getting the food link
                first_food_link = all_table_items[0].get('href')

                # returning the link under which the search food will be
                return FoodScraperSettings.FOOD_NUTRITION_BASE_URL+first_food_link
          
        return None


    def _retrive_table_element(self, soup_obj: BeautifulSoup, start_with: str, end_with: str="") -> tuple[str|None, str|None]:
        """retriving the text values from a table based on the text in these rows
        if not found it will return None, None
        """
        total = None
        if start_with and end_with:
            total = soup_obj.find("b",string=re.compile(f"^{start_with}.*{end_with}$"))
        elif start_with: # if endwith is not defined
            total = soup_obj.find("b",string=re.compile(f"^{start_with}.*"))
        else: # since we dont passed any start and end with then we dont need to look for aything
            return None, None
        
        # retriving the values from the table - single elements - only text values
        if total:
            all_fat = total.find_parent().find_parent()
            all_fat_td = all_fat.find_all("td")
            total_value = all_fat_td[0].contents[1].strip() if len(all_fat_td)>1 and len(all_fat_td[0].contents)>1 else None
            total_percent = str(all_fat_td[1].contents[0].string) if len(all_fat_td)>1 and len(all_fat_td[0].contents)>=1 else None
            if total_percent:
                total_percent = total_percent.encode('ascii','ignore').decode()
        else:
            total_percent = None
            total_value = None

        return total_value, total_percent
    
    
    def _retrive_table_indented_element(self, soup_obj: BeautifulSoup, start_with: str, end_with: str="") -> tuple[str|None, str|None]:
        """retriving the text values (intended) from a table based on the text in these rows
        if not found it will return None, None
        """

        # helper function for fidninf the td element in the table
        def has_current_words_starts_with(text):
            """helper function for finding the word that starts with the given string"""
            if text and start_with in text:
                new_text = str(text).strip()
                if new_text and new_text.startswith(f"{start_with}\xa0"):
                    return True
            return False

        # helper function for fidninf the td element in the table
        def has_current_words_starts_with_and_ends_with(text):
            """helper function for finding the word that starts with and ends with the given strings"""
            if text and start_with in text and end_with in text:
                new_text = str(text).strip()
                if new_text and new_text.split()[0] == start_with and new_text.split()[1] == end_with:
                    return True
            return False

        total = None
        if start_with and end_with:
            total = soup_obj.find("td",string=has_current_words_starts_with_and_ends_with)
        elif start_with: # if endwith is not defined
            total = soup_obj.find("td",string=has_current_words_starts_with)
        else: # since we dont passed any start and end with then we dont need to look for aything
            return None, None

        # retriving the values from the table - single elements - only text values
        if total:
            all_fat = total.find_parent()
            all_fat_td = all_fat.find_all("td")
            total_value = all_fat_td[0].contents[0].strip() if len(all_fat_td)>1 and len(all_fat_td[0].contents)>0 else None
            total_value = total_value.split()[-1] if total_value and len(total_value)>0 else None
            total_percent = str(all_fat_td[1].contents[0].string) if len(all_fat_td)>1 and len(all_fat_td[1].contents)>=1 else None
            if total_percent:
                total_percent = total_percent.encode('ascii','ignore').decode()
        else:
            total_percent = None
            total_value = None

        return total_value, total_percent

    def return_nutrition(self, food: str) -> dict | None:
        """
        returns the nutrition for the given food as a dictionary
        or returns None if this operation was not successful
        """
        assert isinstance(food, str), "food variables has to be of type str!"
        assert len(food) > 0, "food variable cant be an empty string!"
        

        print(f"Log: Retrieving... data for {food}.")
        nutrition_link = self._serch_for_food(food)

        if nutrition_link:
                
                # getting the raw data from the search link
                response = requests.get(
                    url=nutrition_link,
                    headers=self.headers,
                )
                # checking for any HTTP errors
                response.raise_for_status()
                # in case of encoding problems - if the encoding cant be resolved from the request
                # response.encoding = "UTF-8"
                # print(response.encoding)

                # if evertyhign was ok we continue
                if (response.status_code == 200):
                    
                    # creating the soup object from the raw data
                    soup = BeautifulSoup(response.text, "lxml")

                    # getting all the objects from the nutrition table
                    food_name = soup.select_one(selector="#food-name")
                    food_name = food_name.get_text(strip=True) if food_name else None
                    portion_size = soup.select_one(selector="#serving-size")
                    portion_size = portion_size.get_text(strip=True) if portion_size else None
                    calories = soup.select_one(selector="#calories")
                    calories = calories.get_text(strip=True) if calories else None

                    total_fat_value, total_fat_percent = self._retrive_table_element(soup,"Total","Fat")
                    saturated_fat_value, saturated_fat_percent = self._retrive_table_indented_element(soup,"Saturated","Fat")
                    cholesterol_value, cholesterol_percent = self._retrive_table_element(soup,"Cholesterol")
                    sodium_value, sodium_percent = self._retrive_table_element(soup,"Sodium")
                    total_carbohydrate_value, total_carbohydrate_percent = self._retrive_table_element(soup,"Total","Carbohydrate")
                    protein_value, protein_percent = self._retrive_table_element(soup,"Protein")
                    dietary_fiber_value, dietary_fiber_percent = self._retrive_table_indented_element(soup,"Dietary","Fiber")
                    sugar_value, sugar_percent = self._retrive_table_indented_element(soup,"Sugar")

                     
                    # creating the dictionary with the data
                    # food_data = {
                    #     "FoodName": food_name,
                    #     "NutritionFacts": {
                    #         "Portion Size": portion_size,
                    #         "Calories": calories,
                    #         "TotalFat": {
                    #             "PercentDailyValue": total_fat_percent,
                    #             "WeightValue":total_fat_value,
                    #             "SaturatedFat":{
                    #                 "PercentDailyValue": saturated_fat_percent,
                    #                 "WeightValue":saturated_fat_value,
                    #             }
                    #         },
                    #         "Cholesterol":{
                    #             "PercentDailyValue": cholesterol_percent,
                    #             "WeightValue":cholesterol_value,
                    #         },
                    #         "Sodium":{
                    #             "PercentDailyValue": sodium_percent,
                    #             "WeightValue":sodium_value,
                    #         },
                    #         "TotalCarbohydrate":{
                    #             "PercentDailyValue": total_carbohydrate_percent,
                    #             "WeightValue":total_carbohydrate_value,
                    #             "DietaryFiber":{
                    #                 "PercentDailyValue": dietary_fiber_percent,
                    #                 "WeightValue":dietary_fiber_value,
                    #             }, 
                    #             "Sugar":{
                    #                 "PercentDailyValue": sugar_percent,
                    #                 "WeightValue": sugar_value,
                    #             },
                    #         },
                    #         "Protein": {
                    #             "PercentDailyValue": protein_percent,
                    #             "WeightValue":protein_value,
                    #         }
                    #     },
                    # }

                    food_data = {
                        "FoodName": food_name,
                        "Portion Size": portion_size,
                        "Calories": calories,
                        "TotalFat_PercentDailyValue": total_fat_percent,
                        "TotalFat_WeightValue":total_fat_value,
                        "SaturatedFat_PercentDailyValue": saturated_fat_percent,
                        "SaturatedFat_WeightValue":saturated_fat_value,
                        "Cholesterol_PercentDailyValue": cholesterol_percent,
                        "Cholesterol_WeightValue":cholesterol_value,
                        "Sodium_PercentDailyValue":sodium_percent,
                        "Sodium_WeightValue":sodium_value,
                        "TotalCarbohydrate_PercentDailyValue":total_carbohydrate_percent,
                        "TotalCarbohydrate_WeightValue":total_carbohydrate_value,
                        "DietaryFiber_PercentDailyValue":dietary_fiber_percent,
                        "DietaryFiber_WeightValue":dietary_fiber_value,
                        "Sugar_PercentDailyValue": sugar_percent,
                        "Sugar_WeightValue": sugar_value,
                        "Protein_PercentDailyValue": protein_percent,
                        "Protein_WeightValue":protein_value,
                        "URL": nutrition_link,
                    }

                    print(f"Log: Retrieving data for {food} successful!")
                    return food_data

        print(f"Log: Retrieving data for {food} failed!")
        return None
