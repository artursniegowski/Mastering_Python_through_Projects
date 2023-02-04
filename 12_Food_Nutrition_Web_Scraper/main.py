from food_web_scrapper import FoodScraper, MyHeader
from dict_csv_converter import DictCsvConverter
from main_messages import (
    ASCI_ART_INTRO, 
    message_welcome_01,
    message_welcome_02,
    message_welcome_03 )

# creating the food nutrion scraper object
food_nutrition_scraper = FoodScraper(headers=MyHeader.HEADER)

# creating the dict csv converter object
converter_dict_csv = DictCsvConverter(file_name="food_nutrition_out.csv")

# creating the starting nutrition food list
nutrtion_food_list = []

# intro
print(ASCI_ART_INTRO)
print(message_welcome_01)
print(message_welcome_02)

# waiting for user input - interaction
while not (user_input := input(message_welcome_03)).strip().lower() in {'q'}:
    food_extracted = food_nutrition_scraper.return_nutrition(user_input)
    if food_extracted:
        nutrtion_food_list.append(food_extracted)
else:

    # saving data to a csv file - easy to read
    converter_dict_csv.save_to_csv(nutrtion_food_list)




