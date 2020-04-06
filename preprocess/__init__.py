#!/usr/bin/env python 3.5

"""
The :mod:`preprocessing` module includes normalization,
abbr recognition, stopword filter, lemmatization,
part of speech tagging.
"""

from .normalize import replace_urls
from .normalize import replace_symbols
from .normalize import replace_point_sequence
from .normalize import multipart_words
from .normalize import abbreviations
from .normalize import expand_contractions
from .normalize import replace_punctuation
from .normalize import lowercase
from .normalize import extraspace_for_endingpoints
from .normalize import add_doc_ending_point
from .normalize import del_tokens_len_one

#from preprocess.techniques import shallow
from preprocess.shallow import lowercase,remove_stopwords

#section to import all possible ngram techniques
from preprocess.grams import ngrams

#from preprocess.techniques import deep
from preprocess.deep import ner, syntdep

#importing utils
from preprocess.utils import pipeline

#file interaction utility functions
from preprocess.utils.io import files

#Experimental functions based on nltk, spacy, others.
from .collocations import CollocationList

from .demo import preProcessFlow as normalize

# This idea was taken from oscar project
# Use 'alpha', 'beta', 'rc' or 'final' as the 4th element to indicate release type.
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