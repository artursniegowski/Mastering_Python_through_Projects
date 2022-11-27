"""This is a class used to convert text to morse code"""
class MorseConverterSettings:
    """
    Settings for the class MorseConverter
    """
    # the code and decode from/to morse
    STR_MORSE_CONVERTER = {
        'A':'.-',
        'B':'-...',
        'C':'-.-.',	
        'D':'-..',
        'E':'.',
        'F':'..-·',
        'G':'--.',
        'H':'....',
        'I':'..',
        'J':'.---',
        'K':'-.-',
        'L':'.-..',
        'M':'--',
        'N':'-.',
        'O':'---',
        'P':'.--.',
        'Q':'--.-',
        'R':'.-.',
        'S':'...',
        'T':'-',
        'U':'..-', 
        'V':'...-',
        'W':'.--',	
        'X':'-..-',	
        'Y':'-.--',	
        'Z':'--..',
        '0':'-----',
        '1':'.----',
        '2':'..---',
        '3':'...--',
        '4':'....-',
        '5':'.....',
        '6':'-....',
        '7':'--...',
        '8':'---..',
        '9':'----.',
    }


class MorseConverter:
    """
    This is a class used to convert text to morse code
    """

    def __init__(self) -> None:
        """
        defining the converter dictionary 
        """
        self._dict_str_morse_converter = MorseConverterSettings.STR_MORSE_CONVERTER
        # swaping keys and values from _dict_str_morse_converter
        self._dict_morse_str_converter = { v:k for k,v in self._dict_str_morse_converter.items() }


    def str_to_morse(self, your_input: str) -> str:
        """
        takes a string as input - message to be converted to morse code
        returns a morse code as string as output
        """
        converted_code = ""
        your_input = (str(your_input)).strip()

        print(f"\nConverting: {your_input}")

        for char in your_input:
            if char == ' ': # convert to double space - long space
                # escaping the trap of extra spaces
                if len(converted_code) > 2:
                    if converted_code[-2::] != '  ':
                        converted_code += ' '
                else:
                   converted_code += '  '
            elif char in self._dict_str_morse_converter or \
                char.upper() in self._dict_str_morse_converter:
                # addin a space at the end
                converted_code += self._dict_str_morse_converter[char.upper()] + ' '
            else:
                print(f"Error: Cant convert '{char}'. Not in morse code!!")
                print("Adding: a '#' sign instead.")
                # for a characters that dosent exists in the morse code
                converted_code += '# ' 

        print(f"Morse Code: {converted_code}")
        return converted_code

    def morse_to_str(self, your_input: str) -> str:
        """
        takes a string as input (morse code)
        returns a str - converted message
        """
        hidden_message = ""
        your_input = (str(your_input)).strip()

        print(f"\nConverting: {your_input}")

        your_morse_input = your_input.split(' ')

        for morse_char in your_morse_input:
            if morse_char == '':
                # escaping the trap of extra space
                if len(hidden_message) > 1:
                    if hidden_message[-1] != ' ':
                        hidden_message += ' '
                else:
                    hidden_message += ' '
            elif morse_char in self._dict_morse_str_converter:
                hidden_message += self._dict_morse_str_converter[morse_char]
            else:
                print(f"Error: Cant convert '{morse_char}'. Not int morse code !!")
                print("Adding: a '#' sign instead.")
                hidden_message += '#'

        print(f"Hidden message: {hidden_message}")
        return hidden_message