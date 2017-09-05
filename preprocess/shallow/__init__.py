
from . import pos

#This dict strategy is based on sklearn.metrics.pairwaise code example
TECHNIQUES = {
    'pos': pos,
    }

#Import nltk distances from ~/nltk/metric/distance.py and modify after with decorators
NLTKImportError = False
StanfordParserImportError = False
try:
    import nltk
except ImportError:
    NLTKImportError = True
    print("NLTK package isn't installed.")
    pass
finally:
    if not NLTKImportError:
        try:
            from nltk.parse.stanford import StanfordParser
        except ImportError:
            print("Some stringdists will not be available due to NLTK package isn't installed.")
            pass

        from nltk.parse.stanford import StanfordParser
        from nltk.parse.stanford import StanfordDependencyParser
        from nltk.parse.stanford import StanfordNeuralDependencyParser
        from nltk.tag.stanford import StanfordPOSTagger, StanfordNERTagger
        from nltk.tokenize.stanford import StanfordTokenizer

        PAIRED_DISTANCES['binary_distance'] = binary_distance


from .distances import dice_coefficient_pattern

PAIRED_DISTANCES['levenshtein_distance_pattern'] = levenshtein_distance_pattern

#After compute performance results, default techniques are stablished.
from .distances import levenshtein_similarity_jellyfish as levenshtein_similarity #TODO change this

PAIRED_DISTANCES['levenshtein_similarity'] = levenshtein_similarity
PAIRED_DISTANCES['edit_similarity'] = edit_similarity
PAIRED_DISTANCES['damerau_levenshtein_distance'] = damerau_levenshtein_distance
PAIRED_DISTANCES['levenshtein_distance'] = levenshtein_distance
PAIRED_DISTANCES['edit_distance'] = edit_distance
PAIRED_DISTANCES['dice_coefficient'] = dice_coefficient
PAIRED_DISTANCES['needleman_wunsch_distance'] = needleman_wunsch_distance

# append all verified techniques in module importing argument ALL
__all__ = []
for technique in TECHNIQUES:
	__all__.append(technique)

__techniques__ = {
'pos':POS,
}

__not_implemented__ = [
    'Gotoh distance',
    'Monge Elkan distance',
    'N-grams Overlap',
]

__not_documented__ = [
    'Containment distance'
]
