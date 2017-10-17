#!/usr/bin/env python

"""
Deep parsing techniques for NLP text
=========================================

Techniques to transform text into informed strings not just the senteces.

Text can gain more information if:
- Name Entity Recognition

This module concentrate the majority of deeper parsing techniques identified
in Paraphrase Detection papers.

"""

__author__ = 'Abel Meneses-Abad'

from configparser import ConfigParser
import preprocess
import os

#TODO verify what happen if nltk there is not.
try:
    from nltk.tag.stanford import StanfordNERTagger
except:
    pass

config = ConfigParser()
config.read(preprocess.__path__[0]+'/stanford.ini')
stanford_ner_model = {}

stanford_ner_dir = os.path.relpath(config['NER']['stanford_ner_dir'][2:])
stanford_ner_model['en'] = os.path.relpath(stanford_ner_dir[:-1] + config['NER']['stanford_ner_eng_model'][2:-1])
stanford_ner_jar = os.path.relpath(stanford_ner_dir[:-1]+config['NER']['stanford_ner_jar'][2:-1])

def ner(text, lang='en'):
    """Name Entity Recognition.

    :Model:

    StanfordNERTagger

    :Explanation:

    The returned string structure is build to use textsim string and token distances.

    """
    st = StanfordNERTagger(stanford_ner_model[lang], stanford_ner_jar,'utf8')
    result = st.tag(text.split())
    string = ''
    for (word,tag) in result:
        if tag == 'O':
            string += word+' '
        else:
            string += word+'/'+tag+' '
    return string

if __name__ == '__main__':
    s1=input("Input text A:")
    print("The inputed text can be lexicalized '%s'" % ner(s1))
