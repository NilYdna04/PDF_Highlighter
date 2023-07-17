PDF_Highlighter    
    PDF_Highliter is a tool that can highlight text in a PDF document. Text can
    provided as a string or a list of strings. Lists of strings must be provided as 
    a text file in terminal, but can be given manually when working with the 
    highlighter class in a project. Individual pages can also be targeted, as 
    well as the document as a whole. Documents are saved in a file with the 
    following syntax:

    "Originalname_highlighted.pdf"
    
    This tool can either be run in terminal or imported into an existing
    project. The Highlighter module is found in PDF_Highlighter.py. This file
    can be copied and pasted into any project containing the PyMuPDF/"fitz"
    package. To install this package, run the following command in terminal:

    pip install fitz

Usage in Terminal
    In order to highlight a PDF document in terminal, navigate to the directory
    of this project and run the following command:


    Python main.py [filename] ("Text to highlight" OR  "listfilename.txt") [ flags (OPTIONAL)] [pageNumber (OPTIONAL)]


    flags:
        1. -single_page: indicates that a single page is to be highlighted 
        2. -list: indicates that the data provided is to be interpreted as a list
            a. The list should be a text file with words seperated by "#". Each word or phrase
               will be treated as an item in the list. An example list file is provided.

    NOTE: the filename must also include the file extension or the program will not be able to detect the document

    If highlighting a list or a text in one page is desired, include the optional flag and page number.
    "-single_page" and "pageNumber".
    
    NOTE: page number must be last argument if -single_page is included.

    Not including -single_page will result in the entire document being highlighted

Usage in a Project
    Start by copying the PDF_Highlighter.py file into the directory of your project. Then, include
    the following statement at the beginning of your project.

    "from PDF_Highlighter import highlighter"

    Then, a highlighter object can be created by using the highlighter's constructor. 

    "new_highlighter = highlighter(filename)"

    The highlighter has a couple of methods that can be used to highlight text, 
    open new documents, and write to a document. The PDF_Highlighter.py contains
    the documentation of how to use these methods. 

    Note: The Run method is for use with terminal. If using the highlighter in a project,
    disregard this method. 
