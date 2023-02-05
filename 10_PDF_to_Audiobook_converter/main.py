from api_converter import TextAudioConverter, TextAudioConverterSettings
from pdf_converter import PdfTextConverter

FOLDER_NAME = "pdf/"
INPUT_MESSAGE = "PDF file name: "

# creating the text audio converter object
text_audio_converter = TextAudioConverter()

# creating the pdf text converter
# pdf converter can convert one page or the whole pdf to text
pdf_converter_manager = PdfTextConverter()


############################## MAIN PROGRAM ###############################

print("\n*** Welcome to the PDF -> Audiobook converter ***\n")
print("Please enter the pdf file you want to convert to audiobook.")
print("The file has to exists in the '/pdf' folder located in the project.")
print("The Audiobook will be save also in the same location.")
print("Type 'q' to quit.")
print("Example input: example_pdf_file.pdf\n")


# main loop with the user input
# the user can exit by typing 'q'
while not ((file_name := input(INPUT_MESSAGE)).strip().lower() == 'q') :
    file_name = file_name.strip()

    # updating the pdf reader
    pdf_converter_manager.pdf_file_path = FOLDER_NAME + file_name

    # if file actually exists
    if pdf_converter_manager.reader_exists:
        # extacting the pdf text
        pdf_text = pdf_converter_manager.return_text()
        # converting the text to audiobook and saving it
        # creating a sound file with the converter
        text_audio_converter.convert_text_to_sound(
            text=pdf_text,
            file_name=f"pdf/audiobook_{file_name.strip().replace('.pdf','')}",
            format= TextAudioConverterSettings.voicerss_c.MP3,
            voice_speed= TextAudioConverterSettings.voicerss_r.FASTER,
        )
    else:
        print(f"The pdf file '{file_name}' dosent exist in the '{FOLDER_NAME}' folder! Try again or type'q' to quit. Did you forget about .pdf?\n")

else:
    print("Bye Bye!")