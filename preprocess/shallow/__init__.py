from configparser import ConfigParser
import os
from nose import SkipTest
import preprocess
from ..utils.ngrams import ngrams,sngrams, stopword_ngrams, contextual_ngrams

#TODO add the rest of shallow techniques
from ..normalize import (lowercase, replace_urls, replace_symbols,
                        replace_point_sequence, multipart_words,
                        abbreviations, expand_contractions,
                        replace_punctuation,
                        extraspace_for_endingpoints,
                        add_doc_ending_point,
                        del_tokens_len_one)

#TODO add underscore to all variables in the __init__.py to avoid
#tab completion.

LANGUAGES = {
    'en':'english',
    'es':'spanish',
}

#This dict strategy is based on sklearn.metrics.pairwaise code example
TECHNIQUES = {
    'lowercase':lowercase,
    'replace_urls':replace_urls,
    'replace_symbols':replace_symbols,
    'replace_point_sequence':replace_point_sequence,
    'multipart_words':multipart_words,
    'abbreviations':abbreviations,
    'expand_contractions':expand_contractions,
    'replace_punctuation':replace_punctuation,
    'extraspace_for_endingpoints':extraspace_for_endingpoints,
    'add_doc_ending_point':add_doc_ending_point,
    'del_tokens_len_one':del_tokens_len_one,
    'ngrmas':ngrams,
    'sngrams':sngrams,
    'stopword_ngrams':stopword_ngrams,
    'contextual_ngrams':contextual_ngrams,
    }

#TODO: sngrams depend on stanford models; stopword_ngrams depend on
# nltk_data stopwords files; contextual_ngrams depend on nltk_data 
# stopwords file and stemming SnowballStemmer class of nltk
# add this techniques to try/except routines; stemming depends on
# nltk_data wordnet corpus and stem.WordNetLemmatizer class.


__techniques__ = {}

config = ConfigParser()
config.read(preprocess.__path__[0]+'/data/cfg/stanford.cfg')

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
        from .techniques import remove_stopwords, stemming, lemmatization
        from ..utils.ngrams import skipgrams
        TECHNIQUES['remove_stopwords'] = remove_stopwords
        TECHNIQUES['stemming'] = stemming
        TECHNIQUES['skipgrams'] = skipgrams
        TECHNIQUES['lemmatization'] = lemmatization
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
                stanford_pos_dir = os.path.abspath(config['POS']['stanford_dir'])
                stanford_pos_eng_model = os.path.abspath(os.path.join(stanford_pos_dir,config['POS']['stanford_eng_model']))
                stanford_pos_jar = os.path.abspath(os.path.join(stanford_pos_dir,config['POS']['stanford_jar']))

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
                    

# After compute performance results, default techniques are stablished.
# from .distances import levenshtein_similarity_jellyfish as levenshtein_similarity #TODO change this
# like in textsim pack when spacy funcs will be test it. 

# append all verified techniques in module importing argument ALL
__all__ = [LANGUAGES]

for technique in TECHNIQUES:
	__all__.append(technique)
	__techniques__[technique] = TECHNIQUES[technique]

__not_implemented__ = [
    ''
]

__not_documented__ = [
    ''
]
