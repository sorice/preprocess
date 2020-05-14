#!/usr/bin/env python 3.5

"""
The :mod:`preprocessing` module includes: url replacement,
abbr recognition, stopword filter, lemmatization,
part of speech tagging.
"""

from preprocess.basic import replace_urls
from preprocess.basic import replace_symbols
from preprocess.basic import replace_dot_sequence
from preprocess.basic import multipart_words
from preprocess.basic import expand_abbrevs
from preprocess.basic import normalize_abbrevs
from preprocess.basic import expand_contractions
from preprocess.basic import replace_punctuation
from preprocess.basic import lowercase
from preprocess.basic import extraspace_for_endingpoints
from preprocess.basic import add_doc_ending_point
from preprocess.basic import del_tokens_len_one
from preprocess.basic import hyphenation

#from preprocess.techniques import shallow
from preprocess.shallow import remove_stopwords

#section to import all possible ngram techniques
from preprocess.grams import ngrams

#from preprocess.techniques import deep
from preprocess.deep import ner, syntdep

#importing utils
from preprocess.utils import pipeline

#file interaction utility functions
from preprocess.utils.io import files

#Experimental functions based on nltk, spacy, others.
from preprocess.grams import Collocations

from .demo import preProcessFlow as normalize

# This idea was taken from oscar project, this funcs are used in conf.py
# Use 'alpha', 'beta', 'rc' or 'final' as the 4th element to indicate 
# release type.
VERSION = (0, 3, 0, 'alpha')

def get_short_version():
    return '%s.%s' % (VERSION[0], VERSION[1])

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    # Append 3rd digit if > 0
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    elif VERSION[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
        version = '%s%s' % (version, mapping[VERSION[3]])
        if len(VERSION) == 5:
            version = '%s%s' % (version, VERSION[4])
    return version