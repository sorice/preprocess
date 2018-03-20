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
import os
from ..utils import sn_grams

#TODO verify what happen if nltk there is not.
try:
    from nltk.tag.stanford import StanfordNERTagger
    from nltk.parse.stanford import StanfordDependencyParser
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

    multioutput: Format type of the output.
                 string in ['raw_value', 'tuple_list', 'raw_tag']
                 * raw value - string format
                 * tuple list - format is implemented for ngram generalization of
                 some token distances in textsim papckage.
                 * raw tag - string with NE-tokens changed for its NE-tags.

    Returns
    -------

    parsed result : string output, list of tuples [(token, NE tag)],
                    NE-tags substituting NE-tokens string.

    :Explanation:

    The returned string structure is build to use textsim string and token
    distances.

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

stanford_parser_dir = os.path.realpath(config['SYND']['stanford_parser_dir'][2:])
stanford_parser_model['en'] = os.path.realpath(stanford_parser_dir[:-1] + config['SYND']['stanford_parser_eng_model'][2:-1])
stanford_parser_jar = os.path.realpath(stanford_parser_dir[:-1]+config['SYND']['stanford_parser_jar'][2:-1])

def syntdep(text, lang='en', interface='stanford', multioutput='triplet_list', N=2):
    """Syntactic Dependency Parser.

     Parameters
    ----------
    text: string to parse, generally a sentence.

    lang: natural languaje of the text.

    interface: a tag of one of the implemented interfaces in preprocess.
               default = stanford

    multioutput: Format type of the output.
                 string in ['triplet_list','triplet_list_tag' , 'sn_grams']
                 * triplet list - Original stanford output [(word,dep-tag,word)]
                 * triplet list tag - Stanford output [(POS-tag,dep-tag,POS-tag)]
                 * sn_grams - Syntactic N-grams based on [Sidorov2012]_.

    N: length of N-grams

    Returns
    -------

    parsed result : string output, list of tuples [(token, NE tag)],
                    NE-tags substituting NE-tokens string.

    :Explanation:

    The returned string structure is build to use textsim string and token
    distances.

    :Citation:

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
    print(stanford_parser_jar)
    SYNT = [list(parse.triples()) for parse in st.raw_parse(text)]
    triplet_list = []
    triplet_list_tag = []

    for governor, relation, dependent in SYNT[0]:
        triplet_list.append((governor[0],relation,dependent[0]))
        triplet_list_tag.append((governor[1],relation,dependent[1]))

    sn_gram = sn_grams(st, text,N)

    if isinstance(multioutput, str):
        if multioutput == 'triplet_list':
            return triplet_list
        if multioutput == 'triplet_list_tag':
            return triplet_list_tag
        if multioutput == 'sn_grams':
            return sn_gram

#TODO: Semantic Role Labeling

#TODO: variate type of ML technique, using StanfordNeuralDependencyParser

#TODO after have it we can test tensorflow, Torch, etc y ver los test con el PenTreeBank


if __name__ == '__main__':
    s1=input("Input text A:")
    print("The inputed text can be lexicalized '%s'" % ner(s1))
