#!/usr/bin/env python 3.5

"""
.. module:: utils

This module includes some extra functions to
complement the shallow and deep module.

.. moduleauthor:: Abel Meneses-Abad <abelma1980@gmail.com>

"""

from .ngrams import ngrams, skipgrams, sngrams
from .extra import pipeline 
from .tagsetconverter import ptb2universal
from .extra import hypenation