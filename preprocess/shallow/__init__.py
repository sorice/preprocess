from configparser import ConfigParser
import os
from nose import SkipTest
import preprocess
from ..utils.ngrams import ngrams

#TODO add the rest of shallow techniques
from ..normalize import (lowercase, replace_urls, replace_symbols,
                        replace_point_sequence, multipart_words,
                        abbreviations, expand_contractions,
                        replace_punctuation,
                        extraspace_for_endingpoints,
                        add_doc_ending_point,
                        del_char_len_one)

#TODO add underscore to all variables in the __init__.py to avoid
#tab completion.

#This dict strategy is based on sklearn.metrics.pairwaise code example
TECHNIQUES = {
    'lowercase':lowercase,
    'ngrmas':ngrams,
    'replace_urls':replace_urls,
    'replace_symbols':replace_symbols,
    'replace_point_sequence':replace_point_sequence,
    'multipart_words':multipart_words,
    'abbreviations':abbreviations,
    'expand_contractions':expand_contractions,
    'replace_punctuation':replace_punctuation,
    'extraspace_for_endingpoints':extraspace_for_endingpoints,
    'add_doc_ending_point':add_doc_ending_point,
    'del_char_len_one':del_char_len_one
    }

__techniques__ = {}

config = ConfigParser()
config.read(preprocess.__path__[0]+'/cfg/stanford.cfg')

#Import nltk distances from ~/nltk/metric/distance.py and modify after with decorators
_NLTKImportError = False
StanfordParserImportError = False
StanfordPOSTaggerModelJar = False

try: #check if NLTK is installed
    import nltk
except ImportError:
    _NLTKImportError = True
    print("NLTK package isn't installed.")
    pass
finally:    #check if NLTK Stanford parser is installed.
    if not _NLTKImportError:
        from .techniques import remove_stopwords
        TECHNIQUES['remove_stopwords'] = remove_stopwords
        try:
            from nltk.parse.stanford import StanfordParser
        except ImportError:
            StanfordParserImportError = True
            print("Some shallow preprocessing techniques will not work due to NLTK package isn't installed.")
            pass
        finally:
            if not StanfordParserImportError:
                from nltk.tag import StanfordPOSTagger

                #Test if POS.jar and POS model still there after installation
                stanford_pos_dir = os.path.abspath(config['POS']['stanford_pos_dir'][2:])
                stanford_pos_eng_model = os.path.abspath(stanford_pos_dir[:-1] + config['POS']['stanford_pos_eng_model'][2:-1])
                stanford_pos_jar = os.path.abspath(stanford_pos_dir[:-1]+config['POS']['stanford_pos_jar'][2:-1])

                try:
                    st = StanfordPOSTagger(model_filename=stanford_pos_eng_model, path_to_jar=stanford_pos_jar)
                    StanfordPOSTaggerModelJar = True
                except LookupError:
                    print('Loading Stanford POS Tagging because one of the stanford parser or CoreNLP jars doesn\'t exist')
                    pass

                if StanfordPOSTaggerModelJar:
                    from .techniques import pos

                    #This dict strategy is based on sklearn.metrics.pairwaise code example
                    TECHNIQUES['pos'] = pos
                    

#After compute performance results, default techniques are stablished.
#from .distances import levenshtein_similarity_jellyfish as levenshtein_similarity #TODO change this

# append all verified techniques in module importing argument ALL
__all__ = []

for technique in TECHNIQUES:
	__all__.append(technique)
	__techniques__[technique] = TECHNIQUES[technique]

__not_implemented__ = [
    ''
]

__not_documented__ = [
    ''
]
