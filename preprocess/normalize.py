#!/usr/bin/env python 3.5

"""Set de funciones para normalización de textos.
Created on Wed Aug 20 2014
Modified by comparing with other normalize packs on Tue May 8 28 2018
.. version: 0.2
.. release: 0.2-RC2
.. author: Abel Meneses abad
"""

import re, os
import string
from .punctuation import Replacer
from .symbols import replace as sreplace
#TODO Add decorator for importing docstring of external functions

LETTERS = ''.join([string.ascii_letters,'ñÑáéíóúÁÉÍÓÚüÜ'])

#NORMALIZATION FUNCTIONS

def replace_urls(text):
    for i in re.finditer('www\S*(?=[.]+?\s+?)|www\S*(?=\s+?)|http\S*(?=[.]+?\s+?)|http\S*(?=\s+?)',text):
        for j in range(i.start(),i.end()):
            if text[j] in string.punctuation:
                text = text[:j]+'_'+text[j+1:]
    return text

def replace_symbols(text):
    return sreplace(text)

def replace_point_sequence(text):
    """
    Replace a contiguous point sequence by the same amount of 
    whitespace.

    ..Note: can't be reimplemented without the finditer function.
    This expression r'(\w+)[.]\s*[.]+[\s|[.]]*' changes the sequences of points
    but it is impossible to handle the number of white spaces.
    This functions it is used latter for the alignment process after normalization.
    """

    for i in re.finditer('[.]\s*?[.]+?[\s|[.]]*',text):
        for j in range(i.start(),i.end()):
            if text[j] == '.' or text[j]==' ':
                text = text[:j]+' '+text[j+1:]
    return text

def multipart_words(text):
    """Hyphenated words like 'end-of-line' are called in NLP multi-part
    words.

    All hyphens in multi-part words are changed by underscore 
    character.

    .. Note that syllable segmentation of reach format text add extra
    hyphens to every text, those hyphens are removed in 
    `replace_punctuation` function.
    """
    text = re.sub('(\w+)[-@.](?=\w+?)','\g<1>_',text)

    #Added for Llanes, is under analisis if it most be here.
    text = re.sub('[.](?=,)|[.](?=;)|[.][[]|[.][]]',' ',text) #Este hay que modificarlo si vamos a usar abbrev
    text = re.sub('[.][)](?=\s*\n)|[.]["](?=[\s|)]*\n)|[.][:](?=\s*\n)','. ',text) #Este modificarlo si vamos a usar el replacers1
    text = re.sub('[.][)](?=\s*\w)|[.]["](?=\s*[\w)[])|[.][:](?=\s*\w)','. ',text) #Este modificarlo si vamos a usar el replacers1
    text = re.sub('[.][)](?=\s*[.])|[.][)](?=[,])',')',text)
    text = re.sub('[.][)](?=\s*")|[.]["](?=\s*")','. ',text)
    text = re.sub('[.]["](?=\s*[.])|[.][:](?=\s*")',' ',text)
    return text

def abbreviations(text, lang='en'):
    """Proper names and abbrev recognition and manipulation based on
    regular expressions.

    .. Note: In the case of U_S. the function will expect you filter at the end
    of preprocessing the conditions of the dot in the expression. If a cappital
    letter follows then this dot match with and end of sentence, else must be
    erased.
    """

    #Proper names acronyms recognition and normalization
    text = re.sub('(\s[A-Z])[.](?!\n)','\g<1>_',text)

    #Abbreviation recognition and normalization. 
    #TODO: implement to read the list of abbrev and compose the pattern 
    # r'(abbrev1|abbrev2|etc).'
    text = re.sub('(Lic|Ph|Corp|Ms|Ing|Dr).','\g<1>_',text)

    return text

#----------------------CONTRACTIONS REPLACEMENT

contractions_patterns = [
(r'won\'t', 'will not'),
(r'can\'t', 'can not'),
(r'i\'m', 'i am'),
(r'isn\'t', 'is not'),
(r'(\w+)\'ll', '\g<1> will'),
(r'(\w+)n\'t', '\g<1> not'),
(r'(\w+)\'ve', '\g<1> have'),
(r'(\w+)\'d(?=\w+ed)', '\g<1> had'),
(r'(\w+)\'s', '\g<1> is'),
(r'(\w+)\'re', '\g<1> are'),
(r'(\w+)\'d', '\g<1> would')
]

def expand_contractions(text, lang='en'):
    """Expand english contractions."""
    for (pattern, repl) in contractions_patterns:
            (text, count) = re.subn(pattern, repl, text)
    return text

def replace_punctuation(text):
    """
    Replace all punctuation characters based on patterns contained in
    punctuation script.

    #TODO: program this like re.sub(pattern, repl, text).

    """
    punctuation = Replacer()
    text = punctuation.replace(text)
    return text

def lowercase(text):
    """Return lowercase of string.
    """
    if isinstance(text,str):
        return text.lower()
    else:
        print('Input must be a string')

#PREPROCESSING FUNCTIONS

def add_extra_space_for_sentence_ending_point(text):
    """
    Add an extra whitespace (if there isn't any) between the last 
    sentence letter and the ending point, allowing an easier way 
    of parsing all sentences by a very distinctive ending point.

    This function allows to avoid acronym dots during the sentence
    parsing subprocess.
    """
    text = re.sub('[.]\s*\n',' .\n ',text)
    return text

def add_doc_ending_point(text):
     """
     .. function:: add_doc_ending_point

     Comes from clean_punctuation script but with less functionalities, except
     adding an ending point at the end of the document.

     :Explanation:

     This is a function to garantied that the last sentence have an ending
     point. The sentence tokenization process can be standardized because every
     sentence, even the last one, have an ending point.

     :param text: text to process.
     :param type: string.

     :returns text: The last char will be an ending point.

     .. author: Abel Meneses abad
     Created on Fri, 28 Feb 2014
     Modify on Son Dic 6 2015
     Finish on
     .. release: 0.2
     """
     # Este fragmento de código coloca un punto en el final del texto. Objetivo: luego hay funciones que necesitan que el último caracter sea el punto final de la última oración.

     first_ending_point = text.rfind('.')     #last ending point position
     fragment = text[first_ending_point+1:]   #text fragment after endindg point

     A = set(LETTERS)
     B = set(fragment)

     if len(B.intersection(A)) != 0: #if there are valid letters after ending point insert a new one
          text += ' .'

     return text

def del_char_len_one(text):
    """Delete tokens with length = 1.

    This is kind of a basic stopword filtering.
    """
    text = re.sub('\s\w\s',' ',text)
    return text

#TODO: implement Deep Learning to sentence parsing.

#TODO: implement collocations based on nltk