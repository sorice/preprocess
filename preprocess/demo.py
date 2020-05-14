#!/usr/bin/env python 3.5

import re
import string
from preprocess.basic import *
import os

def preProcessFlow(text: str) -> str:
    """Text Preprocessing Flow demo"""
    if os.path.isfile(text):
        with open(text) as doc:
            text = doc.read()

    #-------------------Special tokens recognition and normalization
    text = replace_urls(text)
    #print ('processing urls\n', text)

    text = replace_symbols(text)
    #print ('processing symbols like Greek letters',text)

    text = replace_dot_sequence(text)
    #print ('cleaning contiguous dots\n',text)

    text = extraspace_for_endingpoints(text)

    text = normalize_abbrevs(text)
    #print ('abbrev recognition and normalization\n',text)

    # Esta demora mucho, hay que ver porque
    text = multipart_words(text)
    #print ('Process tokens like "end-of-line"\n', text)

    # TODO: collocations or multiword expressions modification
    #text = underscoring_multiword_expressions(text)

    # Expand contractions before erase punctuations including single cuote mark.
    text = expand_contractions(text)

    # Clean all punctuations
    text = replace_punctuation(text)

    # Add an ending point to the document.
    preproc_text = add_doc_ending_point(text)
    #print ('adding end point if necessary\n',text)

    return preproc_text#,texta

if __name__ == "__main__":
    text = open("test/test_text.txt").read()
    print (preProcessFlow(text))
