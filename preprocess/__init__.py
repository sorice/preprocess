#!/usr/bin/env python 3.5
# -*- coding: utf-8 -*-

"""
The :mod:`preprocessing` module includes normalization,
abbr recognition, stopword filter, lemmatization,
part of speech tagging.
"""

import sys
sys.path.append('/home/abelm')

from .punctuation import Replacer

from .methods import url_string_recognition_support
from .methods import symbols_filter
from .methods import del_contiguous_point_support
from .methods import contiguos_string_recognition_support
from .methods import abbrev_recognition_support
from .methods import del_char_len_one
from .methods import add_text_end_dot
from .methods import contractions

#from preprocess.techniques import shallow
from preprocess import shallow
from preprocess.shallow import *
