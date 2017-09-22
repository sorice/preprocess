#!/usr/bin/env python 3.5

"""
The :mod:`preprocessing` module includes normalization,
abbr recognition, stopword filter, lemmatization,
part of speech tagging.
"""

from .normalize import urls_modification
from .normalize import replace_symbols
from .normalize import remove_contiguous_points
from .normalize import multi_part_words_modification
from .normalize import expand_contractions
from .normalize import abbrev_modification
from .normalize import del_char_len_one
from .normalize import add_doc_ending_point
from .normalize import lowercase


#from preprocess.techniques import shallow
from preprocess import shallow
from preprocess.shallow import *
