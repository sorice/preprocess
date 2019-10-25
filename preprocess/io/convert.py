#!/usr/bin/env python 3.6

from PyPDF2 import PdfFileReader 

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os 
import warnings

class pdf:
    """UNDER INVESTIGATION
    
    Class wrapper for PyPDF2 to extract full information from a pdf.
    This function is under study because fail with some pdf.
    The experiments shows that in some multicolumn layouts pdf, the
    PyPDF2 library extract the text better than pdfMiner and pdftotext.
    """
    def __init__ (self, fpath):
        self.pdf_path = fpath
        self.pdfR = PdfFileReader(self.pdf_path)

    def extractText(self):
        """Return text from a pdf
        """
        warnings.warn('This function could fail with some pdfs.')
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

def pdftotext(path, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(path, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close()
    return text