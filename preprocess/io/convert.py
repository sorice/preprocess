#!/usr/bin/env python 3.6

from PyPDF2 import PdfFileReader 

class pdf:
    """Class wrapper to extract full information from a pdf."""
    def __init__ (self, fpath):
        self.pdf_path = fpath
        self.pdfR = PdfFileReader(self.pdf_path)

    def extractText(self):
        """Return text from a pdf"""
        self.text = ''
        for page in range(self.pdfR.getNumPages()): 
            self.text += self.pdfR.getPage(page).extractText()
        return self.text 

    def index(self):
        """TODO return content index"""
        return

    def notes(self):
        """TODO return content pdf notes"""
        return

#TODO doing a test PyPDF2 fail in a book processing. 
# The same book was processed by pdftotext without problems.