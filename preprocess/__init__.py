#!/usr/bin/env python 3.5

"""
The :mod:`preprocessing` module includes normalization,
abbr recognition, stopword filter, lemmatization,
part of speech tagging.
"""

from .methods import urls_modification
from .methods import replace_symbols
from .methods import remove_contiguous_points
from .methods import multi_part_words_modification
from .methods import expand_contractions
from .methods import abbrev_modification
from .methods import del_char_len_one
from .methods import add_doc_ending_point


#from preprocess.techniques import shallow
from preprocess import shallow
from preprocess.shallow import *
