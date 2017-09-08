#!/usr/bin/env python

"""
Shallow parsing techniques for NLP text
=========================================

Techniques to transform text into informed strings not just the senteces.

Text are less complex if:
- stopwords are eliminated or not
- capital letters are deleted or not
- multiword are trated as is
- TODO: end this list

This module concentrate the majority of shallow parsing techniques identified
in Paraphrase Detection papers.

"""

__author__ = 'Abel Meneses-Abad'

from configparser import ConfigParser
import preprocess
import os
from nltk.tag.stanford import StanfordPOSTagger

config = ConfigParser()
config.read(preprocess.__path__[0]+'/stanford.ini')
stanford_pos_model = {}

stanford_pos_dir = os.path.relpath(config['POS']['stanford_pos_dir'][2:])
stanford_pos_model['en'] = os.path.relpath(stanford_pos_dir[:-1] + config['POS']['stanford_pos_eng_model'][2:-1])
stanford_pos_jar = os.path.relpath(stanford_pos_dir[:-1]+config['POS']['stanford_pos_jar'][2:-1])

def pos(text, lang='en'):
    """Part of Speech Tagging
    """
    st = StanfordPOSTagger(model_filename=stanford_pos_model[lang], path_to_jar=stanford_pos_jar)
    return st.tag(text.split())

if __name__ == '__main__':
    s1=input("Input text A:")
    print("The inputed text can be lexicalized '%s'" % pos(s1))
