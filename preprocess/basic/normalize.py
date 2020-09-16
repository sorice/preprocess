#!/usr/bin/env python 3.5

"""Module for popular text normalization techniques:

    - url replacement (func: replace_urls)
    - symbols replacement (func: replace_symbols)
    - abbreviations dot marking, with '_'
    - replace punctuation and other noisy chars
    - and other functions elaborated for txt comming from pdfMiner, pdf2txt

.. author: Abel Meneses abad
"""

import re, os
import string
from .punctuation import Replacer
from .symbols import replace as sreplace

#TODO Add decorator for importing external function's docstring

#Support for spanish texts
LETTERS = ''.join([string.ascii_letters,'ñÑáéíóúÁÉÍÓÚüÜ'])

#NORMALIZATION FUNCTIONS

def replace_urls(text: str) -> str:
    for i in re.finditer('www\S*(?=[.]+?\s+?|[.]\Z|\w\s)|http\S*(?=[.]+?\s+?|[.]\Z|\w\s)',text):
        for j in range(i.start(),i.end()):
            if text[j] in string.punctuation:
                text = text[:j]+'_'+text[j+1:]
    return text

def replace_symbols(text: str) -> str:
    return sreplace(text)

def replace_dot_sequence(text: str) -> str:
    """
    Replace a contiguous dot sequence by the same amount of 
    whitespace.

    Please read carefully the documentation to see all the 
    conventions adopted to replace this sequences, and how to 
    maintain dot sentence delimiters for sentence tokenizers.

    Note
    ----

    It can't be implemented without the finditer function.
    This expression r'(\w+)[.]\s*[.]+[\s|[.]]*' changes the sequences 
    of points but it is impossible to handle the number of white spaces.
    This functions it is used also for the alignment process after 
    normalization, where maintaining the length of the original text is
    important.

    """

    for i in re.finditer('[.]\s*?[.]+?[\s|[.]]*',text):
        for j in range(i.start(),i.end()):
            if text[j] == '.' or text[j]==' ':
                text = text[:j]+' '+text[j+1:]
    return text

def multipart_words(text: str) -> str:
    """Hyphenated words like 'end-of-line' are called in NLP multi-part
    words.

    All hyphens in multi-part words are changed by underscore 
    character.

    Note
    ----

    That syllable segmentation of reach format text add extra
    hyphens to every text, those hyphens are removed in 
    :func: `replace_punctuation`.
    """
    text = re.sub('(\w+)[-@.](?=\w+?)','\g<1>_',text)
    
    return text

#----------------------CONTRACTIONS REPLACEMENT
#Contractions patterns based on NLTK Book suggestions
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

def expand_contractions(text: str, lang='en') -> str:
    """Expand english contractions.
    """
    for (pattern, repl) in contractions_patterns:
            (text, count) = re.subn(pattern, repl, text)
    return text

def replace_punctuation(text: str) -> str:
    """
    Replace all punctuation characters based on patterns contained in
    punctuation script. The Regular Expressions are ordered based on
    structural elements (E.g. word syllabic division), paragraph and
    sentence transformations.

    Note
    ----

    All the syntactic and morphologic transformations depending on
    punctuation signs, must be done before applying 
    replace_punctuation func.

    It is important to apply replace_symbols func before this func. 
    Also the abbreviation recognition, multipart words, replace_dots
    and replace urls, all these functions work with punctuation signs,
    so if they are not underscored or transformed, this func will take
    its own decisions with the remaining punct signs.
    For example the sentence tokenization will change in case of rare
    quotations: “.

    """
    #TODO: program this like re.sub(pattern, repl, text).
    punctuation = Replacer()
    text = punctuation.replace(text)
    return text
    #TODO: program this func to permit the addition of new RE by the
    #user like spacy

def lowercase(text: str) -> str:
    """Return lowercase of string.
    """
    if isinstance(text,str):
        return text.lower()
    else:
        print('Input must be a string')
    #TODO: after adding typing check delete if/else structure

#PREPROCESSING FUNCTIONS

def extraspace_for_endingpoints(text: str) -> str:
    """
    Add an extra whitespace (if there isn't any) between the last 
    sentence letter and the ending point, allowing an easier way 
    of parsing all sentences by a very distinctive ending point.

    This function allows to avoid abbrev dots during the sentence
    parsing subprocess.

    The original objective of this func was to preserve \n in datasets
    with one sentence by line (E.g. paraphrase detection, STS).

    Note
    ----

    Replace punctuation also intend to do this, but because of the
    complexity of RE in replace_punctuation this function guarantee the
    100% of sentence dots are separated at list by a whitespace by any
    other char.

    """
    text = re.sub('[.]\s*\n',' .\n ',text)
    return text

    #TODO: look comments in CHANGELOG for v0.3.3

def add_doc_ending_point(text: str) -> str:
    """
    Add Final Text Dot

    Comes from clean_punctuation script but with less functionalities, except
    adding an ending point at the end of the document.

    Note
    -----

    This is a function to garantied that the last sentence have an ending
    point. The sentence tokenization process can be standardized because every
    sentence, even the last one, have an ending point.

    Parameters
    -----------

    text : str
           text to process

    Returns
    -------

    text: str
          The same text but, if missing, with a dot at the end
    """
    # Este fragmento de código coloca un punto en el final del texto. Objetivo: luego hay funciones que necesitan que el último caracter sea el punto final de la última oración.

    first_ending_point = text.rfind('.')     #last ending point position
    fragment = text[first_ending_point+1:]   #text fragment after endindg point

    A = set(LETTERS)
    B = set(fragment)

    if len(B.intersection(A)) != 0: #if there are valid letters after ending point insert a new one
        text += ' .'

    return text

def del_tokens_len_one(text: str) -> str:
    """Delete tokens with length = 1.

    This is kind of a basic stopword filtering.
    """
    text = re.sub('(\s)\w(\s)',' ',text)
    return text

# TODO: implement Deep Learning for sentence parsing. This is experimental,
# because after preProcessFlow all sentences are well defined by char '.'.