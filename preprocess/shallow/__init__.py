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
StanfordPOSTaggerModelJar = False

try: #check if NLTK is installed
    import nltk
except ImportError:
    NLTKImportError = True
    print("NLTK package isn't installed.")
    pass
finally:    #check if NLTK Stanford parser is installed.
    if not NLTKImportError:
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
                    raise SkipTest('Loading Stanford POS Tagging because one of the stanford parser or CoreNLP jars doesn\'t exist')

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

__techniques__ = {
'POS':pos,
}

__not_implemented__ = [
    ''
]

__not_documented__ = [
    ''
]
