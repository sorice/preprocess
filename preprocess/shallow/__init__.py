from configparser import ConfigParser
import os
from nose import SkipTest
import preprocess as prep

#TODO add underscore to all variables in the __init__.py to avoid
#tab completion.

LANGUAGES = {
    'en':'english',
    'es':'spanish',
}

#This dict strategy is based on sklearn.metrics.pairwaise code example
TECHNIQUES = {}

#TODO: reduce dependencies: sngrams depend on stanford models; stopword_ngrams depend on
# nltk_data stopwords files; contextual_ngrams depend on nltk_data 
# stopwords file and stemming SnowballStemmer class of nltk
# add this techniques to try/except routines; stemming depends on
# nltk_data wordnet corpus and stem.WordNetLemmatizer class.


__techniques__ = {}

config = ConfigParser()
config.read(prep.__path__[0]+'/data/cfg/stanford.cfg')

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
        TECHNIQUES['remove_stopwords'] = remove_stopwords
        TECHNIQUES['stemming'] = stemming
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
