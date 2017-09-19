#!/usr/bin/env python 3.5
# -*- coding: utf-8 -*-

import re
import string
from .methods import *
from .punctuation import Replacer



def preProcessFlow(text):
    """Text Preprocessing Flow"""

    #-------------------Special tokens recognition and normalization
    text = url_string_recognition_support(text)
    #print ('processing urls\n', text)

    text = symbols_filter(text)
    #print ('processing symbols like Greek letters',text)

    text = del_contiguous_point_support(text)
    #print ('cleaning contiguous dots\n',text)

    text = space_sentence_dot(text)

    text = abbrev_recognition_support(text)
    #print ('abbrev recognition and normalization\n',text)

    # Esta demora mucho, hay que ver porque
    text = contiguos_string_recognition_support(text)
    #print ('processing contiguos string recognition support\n', text)

    # Before erase all punctuation chars process contraction
    text = contractions(text)

    # Clean all punctuations
    punctuation = Replacer()
    text = punctuation.replace(text)
    #print ('processing punctuation signs: ,;:...-*=<>\n',text)

    # Add a final dot to the document.
    preproc_text = add_text_end_dot(text)
    #print ('adding end point if necessary\n',text)

    return preproc_text#,texta

if __name__ == "__main__":
    text = open("test/test_text.txt").read()
    print (preProcessFlow(text))
