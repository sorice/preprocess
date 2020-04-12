from .ngrams import ngrams, sngrams, stopword_ngrams, contextual_ngrams
from .collocations import CollocationList

__techniques__ = {}

TECHNIQUES = {
    'ngrams':ngrams,
    'sngrams':sngrams,
    'stopword_ngrams':stopword_ngrams,
    'contextual_ngrams':contextual_ngrams,
    'collocations':CollocationList,
    }

_NLTKImportError = False
try: #check if NLTK is installed
    import nltk
except ImportError:
    _NLTKImportError = True
    print("NLTK package isn't installed.")
    pass
finally:    #check if NLTK Stanford parser is installed.
    if not _NLTKImportError:
        from .ngrams import skipgrams
        TECHNIQUES['skipgrams'] = skipgrams

# append all ngram verified techniques in module importing argument ALL
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