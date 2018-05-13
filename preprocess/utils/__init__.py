#!/usr/bin/env python 3.5

"""
The :mod:`preprocessing` module includes normalization,
abbr recognition, stopword filter, lemmatization,
part of speech tagging.
"""

from .ngrams import ngrams, skipgrams, sngrams
from .others import pipeline 
from .tagsetconverter import ptb2universal
