#!/usr/bin/env python 3.5

import re
import string
from .methods import *

def preProcessFlow(text):
    """Text Preprocessing Flow demo"""

    #-------------------Special tokens recognition and normalization
    text = urls_modification(text)
    #print ('processing urls\n', text)

    text = replace_symbols(text)
    #print ('processing symbols like Greek letters',text)

    text = remove_contiguous_points(text)
    #print ('cleaning contiguous dots\n',text)

    text = add_extra_space_for_sentence_ending_point(text)

    text = abbrev_modification(text)
    #print ('abbrev recognition and normalization\n',text)

    # Esta demora mucho, hay que ver porque
    text = multi_part_words_modification(text)
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
