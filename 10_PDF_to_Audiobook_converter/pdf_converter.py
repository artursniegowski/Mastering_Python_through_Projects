# this is a class managing the convertsion pdf -> text
from PyPDF2 import PdfReader


class PdfTextConverter:
    """
    class managing the convertsion pdf to txt
    """

    def __init__(self, pdf_file_path: str = None) -> None:
        self.pdf_file_path = pdf_file_path


    @property
    def pdf_file_path(self) -> str:
        """
        getter for the property pdf_file_path
        """
        return self._pdf_file_path

    @pdf_file_path.setter
    def pdf_file_path(self, value:str) -> None:
        """
        setting the property pdf_file_path
        """
        self._pdf_file_path = value
        # every time a new file path was sett updating the reader
        if (self.pdf_file_path):
            print("started - PDF reading ...")
            self.reader = self._read_in_pdf(self.pdf_file_path)
        else:
            self.reader = None
        # updating the total number of pages
        if (self.reader): # if the reader exists
            self.pages_count = len(self.reader.pages)
        # reader exists 
        # if sucesful created reader than it will be true otherwise false
        self.reader_exists = True if (self.reader) else False


    def return_text(self, page_num: int | None = None) -> str | None:
        """
        returns text for the given page,
        if not defined then then returns text for all the pages
        page_num starts with 0 ! 
        """
        if self.reader_exists:
            print("started - PDF text extraction ...")
            if page_num:
                if page_num < self.pages_count:

                    print("completed - PDF text extraction.")
                    return self.reader.pages[page_num].extract_text()
                    
                else:
                    print(f"Error: page number {page_num} is out of range of the possible {self.pages_count} pages. First page is at 0!")
            else:
                # get the whole text from the pdf, and returns it
                text = ''
                for num in self.reader.pages:
                    text += num.extract_text()

                print("completed - PDF text extraction.")
                return text
        else:
            print("Error: pdf reader dosent exist! Define 'pdf_file_path'!")
            return None

    def _read_in_pdf(self, pdf_name: str) -> PdfReader | None:
        """
        reads in pdf , adn returns a pdf object
        """
        # tries to read in the given pdf
        try:
            reader = PdfReader(pdf_name)
        except FileNotFoundError:
            # if error return an a None object
            print(f"Error: Cant read in the '{pdf_name}'. Check the directory and if the pdf file exists!")
            return None
        else:
            print("completed - PDF reading.")
            return reader 