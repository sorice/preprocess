#!/usr/bin/env python 3.5
# -*- coding: utf-8 -*-

import re
from punctuation import Replacer
import string
from methods import *

def preProcessFlow(doc_name):
    """Text Preprocessing Flow"""
    
    is_a_doc = False
    
    try:
        text = open(doc_name).read()
        is_a_doc = True
    except:
        text = doc_name
    
    #-------------------Special tokens recognition and normalization
    text = url_string_recognition_support(text)
    print ('processing urls\n', text)

    text = punctuation_filter(text)
    print ('processing punctuation signs: ,;:...-*=<>\n',text)
    
    text = del_contiguous_point_support(text)
    print ('cleaning contiguous dots\n',text)
    
    text = abbrev_recognition_support(text)
    print ('abbrev recognition and normalization\n',text)

    # Esta demora mucho, hay que ver porque
    text = contiguos_string_recognition_support(text) 
    print ('processing contiguos string recognition support\n', text)
    
    # Add a final dot to the document.
    text = add_text_end_dot(text)
    print ('adding end point if necessary\n',text)

    #-------------------Clean all punctuation sign
    replacer = Replacer()
    chunk = replacer.replace(text)
    print('chunk:',chunk)
    
    if is_a_doc:
        texto = open(doc_name+'_result','w')
        texto.write(chunk)
        texto.close()

if __name__ == "__main__":
    preProcessFlow("test/test_text.txt")