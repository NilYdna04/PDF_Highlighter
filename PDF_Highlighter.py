# PDF_highlighter
# by Andrew Lin
# 
# pdf_highlighter is a tool capable of locating text in a pdf document and
# highlighting the text. Lists of text can be highlighted at one time. It is 
# recommended to not use the run command manually, as it is meant to be used 
# with the main file with a terminal. Instead, call the methods manually to
# open a document, highlight text, and save the document.
# 

import fitz

class highlighter:
    document = None

    def __init__(self, filename):
       self.filename = filename
        # Open the document
       self.document = fitz.open(self.filename, filetype = "PDF")
        # Creates the name of the written file
       filename = filename.replace(".pdf", "")
       self.writename = filename + "_highlighted.pdf"
       
    
    # open_document
    # inputs:  str filename
    # outputs: none
    # returns: none
    # purpose: opens a different document
    def open_document(self, filename):
        self.document.close()
        self.filename = filename
        # Open the document
        self.document = fitz.open(self.filename, filetype = "PDF")
        # Creates the name of the written file
        filename = filename.replace(".pdf", "")
        self.writename = filename + "_highlighted.pdf"
        

    # highlight_text
    # inputs:  str of text and page number
    # outputs: highlights text in pdf
    # returns: none
    # purpose: highlights the text at a given page in the document
    def highlight_text(self, text, page_number):
        # fitz index the pages starting at 0, so the page number is reduced by one
        page_number = int(page_number) - 1
        page = self.document[page_number]
        for word in page.search_for(text, flags=fitz.TEXT_PRESERVE_WHITESPACE):
            page.add_highlight_annot(word)
            
    # highlight_list
    # inputs:  list of str of text and page number
    # outputs: highlights text in pdf
    # returns: none
    # purpose: highlights every phrase in the list at a given page in the document
    def highlight_list(self, list, page_number):
        for phrase in list:
            # fitz index the pages starting at 0, so the page number is reduced by one
            page_number = int(page_number) - 1
            page = self.document[page_number]
            for word in page.search_for(phrase, flags=fitz.TEXT_PRESERVE_WHITESPACE):
                page.add_highlight_annot(word)
    
    # highlight_all_text
    # inputs:  str of text
    # outputs: highlights text in pdf
    # returns: none
    # purpose: highlights the text in every page of the document
    def highlight_all_text(self, text):
        for index in range(len(self.document)):
            self.highlight_text(text, index)

    # highlight_all_list
    # inputs:  list of str of text
    # outputs: highlights text in pdf
    # returns: none
    # purpose: highlights every phrase in the list in every page of the document
    def highlight_all_list(self, list):
        for index in range(len(self.document)):
            self.highlight_list(list, index)

    # save
    # inputs:  none
    # outputs: saves and writes the document
    # returns: none
    # purpose: a manual way to save the document
    def save_document(self):
        self.document.save(self.writename)

    # run
    # inputs: bool for lists, bool for all pages, text/list, and page number if needed
    # outputs: highlights, saves, and writes the document
    # returns: none
    # purpose: allows the program to run off a terminal if needed
    def run(self, isAll, data, page):
        try:
            # determine if the data is a list or not
            if type(data) == list or type(data) == tuple:
                isList = True
            else: 
                isList = False
            # Highlight a list of words
            if isList:
                if isAll:
                    self.highlight_all_list(data)
                else:
                    self.highlight_list(data, page)
            # Highlight a singular piece of text
            else:
                if isAll:
                    self.highlight_all_text(data)
                else:
                    self.highlight_text(data, page)
            self.save_document()
        except Exception as error:
            print("An exception occurred:", type(error).__name__, "–", error)