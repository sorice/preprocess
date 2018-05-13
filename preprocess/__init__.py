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
from preprocess.shallow import lowercase,ngrams

#from preprocess.techniques import deep
from preprocess.deep import ner, syntdep

from preprocess.utils import pipeline