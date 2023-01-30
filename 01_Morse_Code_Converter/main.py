from messages import LOGO, WELCOME_MESSAGE, ENCODE_MESSAGE, DECODE_MESSAGE
from morse_converter import MorseConverter
import os

# settings for the converter
options = ['encode', 'decode', 'q']

# creating object for the morse converter
morse_codder = MorseConverter()

# Logo
print(LOGO)

while True:
    while (choice := input(WELCOME_MESSAGE).lower().strip()) not in options:
        print(f"\nYour choice '{choice}' is not valid! options: {options}")
    else:
        if choice == 'q':
            print("Bye Bye!")
            break
        elif choice == 'encode':
            to_encode = input(ENCODE_MESSAGE)
            print("\nENCODING...")
            morse_codder.str_to_morse(to_encode)
        elif choice == 'decode':
            print("\nDECODING...")
            to_decode = input(DECODE_MESSAGE)
            morse_codder.morse_to_str(to_decode)