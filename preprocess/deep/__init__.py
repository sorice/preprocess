#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser
import os
from nose import SkipTest
import preprocess

#This dict strategy is based on sklearn.metrics.pairwaise code example
TECHNIQUES = {}

config = ConfigParser()
config.read(preprocess.__path__[0]+'/cfg/stanford.cfg')

#Import nltk distances from ~/nltk/metric/distance.py and modify after with decorators
NLTKImportError = False
StanfordParserImportError = False
StanfordNERTaggerModelJar = False

try: #check if NLTK is installed
    import nltk
except ImportError:
    NLTKImportError = True
    print("NLTK package isn't installed.")
    pass
finally:    #check if NLTK Stanford parser is installed.
    if not NLTKImportError:
        try:
            from nltk.parse.stanford import StanfordParser
        except ImportError:
            StanfordParserImportError = True
            print("Some deeper preprocessing techniques will not work due to NLTK package isn't installed.")
            pass
        finally:
            if not StanfordParserImportError:
                from nltk.tag import StanfordNERTagger
                from nltk.parse.stanford import StanfordDependencyParser

                #Test if NER.jar and NER model still there after installation
                stanford_ner_dir = os.path.abspath(config['NER']['stanford_ner_dir'][2:])
                stanford_ner_eng_model = os.path.abspath(stanford_ner_dir[:-1] + config['NER']['stanford_ner_eng_model'][2:-1])
                stanford_ner_jar = os.path.abspath(stanford_ner_dir[:-1]+config['NER']['stanford_ner_jar'][2:-1])

                try:
                    st = StanfordNERTagger(stanford_ner_eng_model, stanford_ner_jar, 'utf8')
                    StanfordNERTaggerModelJar = True
                except LookupError:
                    raise SkipTest('Fail to loading Stanford NER Tagging because\
                                    one of the stanford parser or CoreNLP jars \
                                    doesn\'t exist')

                if StanfordNERTaggerModelJar:
                    from .techniques import ner

                #Checking Stanford Dependency Parser models exist after installation
                stanford_parser_dir = os.path.realpath(config['SYND']['stanford_parser_dir'][2:])
                stanford_parser_eng_model = os.path.realpath(stanford_parser_dir[:-1] + config['SYND']['stanford_parser_eng_model'][2:-1])
                stanford_parser_jar = os.path.realpath(stanford_parser_dir[:-1]+config['SYND']['stanford_parser_jar'][2:-1])
                
                try:
                    st = StanfordDependencyParser(stanford_parser_eng_model, stanford_parser_jar)
                    StanfordSyntDepModelJar = True
                except LookupError:
                    raise SkipTest("""Fail to loading Stanford Syntactic Dependency Parser
                        because one of its stanford parser or CoreNLP jars doesn't exist""")

                if StanfordSyntDepModelJar:
                    from .techniques import syntdep


#This dict strategy is based on sklearn.metrics.pairwaise code example
TECHNIQUES['ner'] = ner
TECHNIQUES['syntdep'] = syntdep

#After compute performance results, default techniques are stablished.
#from .distances import levenshtein_similarity_jellyfish as levenshtein_similarity #TODO change this

# append all verified techniques in module importing argument ALL
__all__ = []
for technique in TECHNIQUES:
	__all__.append(technique)

__techniques__ = {
'NER':ner,
'SYNTDEP':syntdep
}

__not_implemented__ = [
    #'SRL':srl
]

__not_documented__ = [
    'NER'
    'SYNTDEP'
]
