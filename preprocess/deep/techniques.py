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

def ner(text, lang='en', interface='stanford', multioutput='raw_value'):
    """Name Entity Recognition.

     Parameters
    ----------
    text: string to parse, generally a sentence.

    lang: natural languaje of the text.

    interface: a tag of one of the implemented interfaces in preprocess.

    multioutput: string in ['raw_value', 'tuple_list', 'raw_tag']
                 Format type of the output.
                 Tuple list format is implemented for ngram generalization of
                 some token distances in textsim papckage.

    Returns
    -------

    parsed result : string output, list of tuples [(token, NE tag)].

    :Explanation:

    The returned string structure is build to use textsim string and token distances.

    """
    if interface == 'stanford':
        result = __stanford_ner(text, lang, multioutput)
    if interface == 'freeling':
        result = ''

    return result

def __stanford_ner(text,lang='en',multioutput='raw_value'):
    """Interface for NLTK Stanford Name Entity Tagger interface.
    """

    st = StanfordNERTagger(stanford_ner_model[lang], stanford_ner_jar,'utf8')
    tuple_list = st.tag(text.split())
    string = ''
    raw_tag = ''
    for (word,tag) in tuple_list:
        if tag == 'O':
            string += word +' '
            raw_tag += word + ' '
        else:
            string += word +'/'+tag+' '
            raw_tag += tag + ' '

    if isinstance(multioutput, str):
        if multioutput == 'raw_value':
            return string
        if multioutput == 'tuple_list':
            return tuple_list
        if multioutput == 'raw_tag':
            return raw_tag

if __name__ == '__main__':
    s1=input("Input text A:")
    print("The inputed text can be lexicalized '%s'" % ner(s1))
