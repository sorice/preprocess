#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
from os.path import join, relpath
from preprocess.utils import ngrams

#TODO verify what happen if nltk there is not.
try:
    from nltk.tag import StanfordNERTagger
    from nltk.parse.stanford import StanfordDependencyParser
except:
    pass

config = ConfigParser()
config.read(preprocess.__path__[0]+'/data/cfg/stanford.cfg')
stanford_ner_model = {}

st4_ner_dir = relpath(config['NER']['stanford_dir'])
stanford_ner_model['en'] = relpath(join(st4_ner_dir,config['NER']['stanford_eng_model']))
stanford_ner_jar = relpath(join(st4_ner_dir[:-1],config['NER']['stanford_jar']))

def ner(text, lang='en', interface='stanford', multioutput='raw_value'):
    """Name Entity Recognition.

    Parameters
    ----------

    text : str
           String value to parse, generally a sentence.

    lang : str
           Natural language of the text.

    interface : str
                A tag of one of the implemented interfaces in preprocess.

    multioutput : str
                  Format type of the output. Is an string on this values
                  ['raw_value', 'tuple_list', 'raw_tag']
                    * raw_value - string format 'token tag'
                    * tuple_list - [(token, NE tag)]
                    * raw tag - string with NE-tokens changed for its NE-tags.

    Returns
    -------

    parsed text : string output, list of tuples [(token, NE tag)],
                    NE-tags substituting NE-tokens string.

    Note
    ----

    The returned string structure is build to use string and token
    distances of __textsim__ library.

    """
    if interface == 'stanford':
        result = __stanford_ner(text, lang, multioutput)
    if interface == 'freeling':
        result = ''

    return result

def __stanford_ner(text,lang='en',multioutput='raw_value'):
    """Interface for NLTK Stanford Name Entity Tagger.
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

stanford_parser_model = {}

st4_parser_dir = relpath(config['SYND']['stanford_parser_dir'])
stanford_parser_model['en'] = relpath(join(st4_parser_dir,config['SYND']['stanford_parser_eng_model']))
stanford_parser_jar = relpath(join(st4_parser_dir,config['SYND']['stanford_parser_jar']))

def syntdep(text, lang='en', interface='stanford', multioutput='triplet_list', N=2):
    """Syntactic Dependency Parser.

    The returned string structure is build to use textsim string and token 
    distances.

    Parameters
    ----------
    
    text :  string
            text to parse, generally a sentence.

    lang :  str
            natural languaje of the text.

    interface : str
                a tag of one of the implemented interfaces in preprocess.
            default = stanford

    multioutput :
                    Format type of the output. It is a string in ['triplet_list','triplet_list_tag' , 'sngrams']
                    - triplet list - Original stanford output [(word,dep-tag,word)]
                    - triplet list tag - Stanford output [(POS-tag,dep-tag,POS-tag)]
                    - sngrams - Syntactic N-grams based on [Sidorov2012]_.

    N : int
        length of N-grams

    Returns
    -------
    
    parsed text : list of tuples
                    Sequence of [(head token, DEP tag, dependent token)],
                    head POS-tags SYNTDEP-tag dependent POS-tag, or sngrams.


    References
    ----------

    .. [Sidorov2012] Grigori Sidorov et all (2012). Syntactic N-grams as Machine
        Learning Features for Natural Language Processing.
        Journal Expert Systems with Applications, 4(3): 853-860. Elsevier.

    """
    if interface == 'stanford':
        result = __stanford_parser(text, lang, multioutput, N)
    if interface == 'freeling':
        result = ''

    return result

def __stanford_parser(text,lang='en',multioutput='triplet_list', N=2):
    """Interface for NLTK Stanford Syntactic Dependency Parser.
    """

    st = StanfordDependencyParser(stanford_parser_model[lang], stanford_parser_jar)
    
    SYNT = [list(parse.triples()) for parse in st.raw_parse(text)]
    triplet_list = []
    triplet_list_tag = []

    for governor, relation, dependent in SYNT[0]:
        triplet_list.append((governor[0],relation,dependent[0]))
        triplet_list_tag.append((governor[1],relation,dependent[1]))

    sn_gram = ngrams.sngrams(st, text,N)

    if isinstance(multioutput, str):
        if multioutput == 'triplet_list':
            return triplet_list
        if multioutput == 'triplet_list_tag':
            return triplet_list_tag
        if multioutput == 'sngrams':
            return sn_gram

#TODO: Semantic Role Labeling

#TODO: variate type of ML technique, using StanfordNeuralDependencyParser

#TODO after have it we can test tensorflow, Torch, etc y ver los test con el PenTreeBank


if __name__ == '__main__':
    s1=input("Input text A:")
    print("The inputed text can be lexicalized '%s'" % ner(s1))
