# class used for extracting the color from a image file / photo
import numpy as np # importing numpy
from PIL import Image, UnidentifiedImageError  # for reading the images into np
# these libraries are necessary to passing the image without saving the file on the server
import base64 
import io

class ColorExtractor():
    """
    class for extracting colors from the given image
    """
    def __init__(self, image_file="") -> None:
        self.image_to_open = image_file
    
    @property
    def image_to_open(self) -> str:
        """
        getter for the property image_to_open
        """
        return self._image_to_open

    @image_to_open.setter
    def image_to_open(self, value: str) -> None:
        """setter for the property image_to_open
        """
        self._image_to_open = value
        # every time a new file was sett we will try to read the file
        if (self.image_to_open):
            try:    
                self.__my_image = Image.open(self.image_to_open)

            except FileNotFoundError:
                print(f"Error: Cant find file: {self.image_to_open}")
                self.__my_image = None
            except UnidentifiedImageError:
                print(f"Error: Cant open and identify the file: {self.image_to_open}")
                self.__my_image = None
        else:
            self.__my_image = None

        # creating an numpy 2D array out of the image
        if self.__my_image:
            self.__my_image_array = np.array(self.__my_image.convert("RGB"))
        else:
            self.__my_image_array = None

    def image_url_from_memory(self) -> str | None:
        """This function is used to retrvie the url from the memory to the img tag,
        for html file. So it makes it possible to use render images without saving them on 
        the serve. 
        transfering the image we saved as in-memory to html (for the src tag in html img)
        """
        if self.__my_image:
            # Get the in-memory info
            data_in_memory = io.BytesIO()
            # We use the in-memory info we get using BytesIO in the save() function inside the PIL library.
            self.__my_image.save(data_in_memory,"PNG")
            # Finally, we use base64encode to transfer the image we saved as in-memory to html.
            encoded_img_data_in_memory = base64.b64encode(data_in_memory.getvalue())
            # encoded image to html
            # <img id="picture" src="data:image/jpeg;base64,{{ img_data }}">
            return f"data:image/png;base64,{encoded_img_data_in_memory.decode('utf-8')}"
        return ""

    def retrun_list_of_colors(self, count_top_colors: int = 3000, treshold: int = 60) -> list[str]:
        """returns a list of colors based on the input image
        if image was empty it will return an empty list,
        the count_top_colors is the number of colors taken into account
        for finding the most common and uniqe colors, it is kind of like sensivity,
        the higher this number the more colors will be compare and the higher chance of finding more unique colors,
        treshold - is the number for distinc r , g , b colors, the higher th enumebr the more distinct colors !
        """
        if np.any(self.__my_image_array):
            # how many colors are we taking into account - top
            N = count_top_colors
            # returns the number of unique colors and how often they appeared 
            uniq_values, count = np.unique(self.__my_image_array.reshape(-1,self.__my_image_array.shape[-1]), axis=0, return_counts=True)
            # taking the partion, the Nth elemtn will be it is final sorted position 
            # so all bigger values of indexes Nth will be after the N, and all smaller will be before Nth element
            # this is why we pass -N into argpartition, to get the last N elements that will be after it
            # and then we use list slicing to retrive the end of the list with the biggest values- but they are not ordered!!
            # at this point we are only sure they are the biggest
            # topNidx = np.argpartition(count,-N)[-N:]
            # in stead of -N we will pass a list of indexes that should be in their finall position
            # so we use range to select the last element
            # like so 
            # adjusting N in case our image is smaller, and will have less than N points in a picture
            if count.size < N:
                N = count.size

            topNidx = np.argpartition(count,range(-N,0))[-N:]
            # so the most often colors are the first elements
            topNidx = np.flip( topNidx)
            # print(count[topNidx])
            # print(uniq_values[topNidx])
            # print(topNidx)


            # sorting the most common colors for unique colors, 
            # colors that look alike will not be taken into account
            # starting with the most often
            unique_colors = []
            
            # checking the colors ar close to each other not to count
            for RGB_element in uniq_values[topNidx]:
                if unique_colors:
                    for current_rgb_element in unique_colors:
                        value =  (abs(int(current_rgb_element[0]) - int(RGB_element[0])) + abs(int(current_rgb_element[1]) - int(RGB_element[1])) + abs(int(current_rgb_element[2]) - int(RGB_element[2])))
                        if value > treshold: # this value represent by how much colors need to be differetn to each other to be take into account
                            continue
                        else:
                            break
                    else:
                        unique_colors.append([RGB_element[0], RGB_element[1], RGB_element[2]])
                else:
                    unique_colors.append([RGB_element[0], RGB_element[1], RGB_element[2]])
            
            # print(unique_colors)
            # print(len(unique_colors))
            if unique_colors:
                # returning a list of hash codes representing the colors example: #ffffff
                return [f"#{((n[0]<<16)+(n[1]<<8)+n[2]):06x}" for n in unique_colors]

        return []