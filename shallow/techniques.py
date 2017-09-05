#!/usr/bin/env python

"""
String Similarity Distances
==================================

Based on character similarity calculations.

"""

__author__ = 'Abel Meneses-Abad, Pablo Ulacia'

try:
    from nltk.metrics import edit_distance as edit_distance_nltk2
    from nltk.metrics import binary_distance as binary_distance_nltk
except:
    pass

try:
    from .jellyfish import levenshtein_distance as levenshtein_distance_jellyfish2
    from .jellyfish import jaro_distance as jaro_distance_jellyfish
    from .jellyfish import jaro_winkler as jaro_winkler_distance_jellyfish
    from .jellyfish import hamming_distance as hamming_distance_jellyfish
    from .jellyfish import damerau_levenshtein_distance as damerau_levenshtein_distance_jellyfish2
    from .jellyfish import match_rating_comparison as match_rating_comparison2
except:
    pass

from .pattern import levenshtein as levenshtein_distance_pattern2
from .pattern import levenshtein_similarity as levenshtein_similarity_pattern2
from .pattern import dice_coefficient as dice_coefficient_pattern2

from ..decorators import score_original, Appender
from .distances_doc import *
from ..utils import bigrams

from .smith_waterman import SmithWaterman
from .needleman_wunsch import NeedlemanWunsch
import numpy as np


def lcs(s1, s2):
    """Longest Common Substring
    """

    lengths = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(s1):
        for j, y in enumerate(s2):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(s1), len(s2)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert s1[x-1] == s2[y-1]
            result = s1[x-1] + result
            x -= 1
            y -= 1
    return result

@Appender(lcs_doc)
def lcs_distance(s1,s2):
    """Lenght of LCS.
    """
    return len(lcs(s1,s2))

@Appender(lcs_similarity_doc)
def lcs_similarity(s1,s2):
    """Longest Common Substring Similarity
    """
    LCS = len(lcs(s1, s2))
    p,q = LCS/s1.__len__(), LCS/s2.__len__()
    return float(2* p * q/( p + q ))

@Appender(damerau_levenshtein_dist_doc)
def damerau_levenshtein_distance_textsim(s1, s2):
    """Damerau variation of Levenshtein distance.
    """

    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in range(-1,lenstr2+1):
        d[(-1,j)] = j+1

    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                            d[(i-1,j)] + 1, # deletion
                            d[(i,j-1)] + 1, # insertion
                            d[(i-1,j-1)] + cost, # substitution
                            )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition

    return float(d[lenstr1-1,lenstr2-1])

# if not NLTKImportError:
@Appender(binary_distance_nltk.__doc__)
def binary_distance(s1,s2):
    if binary_distance_nltk(s1,s2):
        return 0.0
    else:
        return 1.0

@Appender(edit_distance_doc)
def edit_distance_nltk(s1,s2):
    """NLTK implementation of Levenshtein distance, also known as Edit distance.
    """
    return edit_distance_nltk2(s1,s2)

@Appender(edit_similarity_doc)
def edit_similarity_nltk(s1,s2):
    """NLTK implementation of Levenshtein similarity.
    """
    return 1 - edit_distance_nltk2(s1,s2)/float(max(len(s1),len(s2),1.0))

#from Jellyfish package
@Appender(edit_distance_doc)
def levenshtein_distance_jellyfish(s1,s2):
    """Jellyfish implementation of Levenshtein distance, also known as Edit distance.
    """
    return levenshtein_distance_jellyfish2(s1,s2)

@Appender(edit_similarity_doc)
def levenshtein_similarity_jellyfish(s1,s2):
    """Levenshtein similarity based on Jellyfish Levenshtein distance.
    """
    return 1 - levenshtein_distance_jellyfish(s1,s2)/float(max(len(s1),len(s2),1.0))

@Appender(jaro_dist_doc)
def jaro_distance(s1,s2):
    """Jaro distance based on Jellyfish Jaro distance implementation.
    """
    return jaro_distance_jellyfish(s1,s2)

@Appender(jaro_winkler_dist_doc)
def jaro_winkler_distance(s1,s2):
    """Jaro Winkler distance based on Jellyfish Jaro-Winkler distance implementation.
    """
    return jaro_winkler_distance_jellyfish(s1,s2)

@Appender(hamming_dist_doc)
def hamming_distance(s1,s2):
    """Jaro distance based on Jellyfish Jaro distance implementation.
    """
    return hamming_distance_jellyfish(s1,s2)

@Appender(damerau_levenshtein_dist_doc)
def damerau_levenshtein_distance_jellyfish(s1,s2):
    """Jaro distance based on Jellyfish Jaro distance implementation.
    """
    return damerau_levenshtein_distance_jellyfish2(s1,s2)

@Appender(match_rating_comparison_doc)
def match_rating_comparison(s1,s2):
    """Matching rating comparison.
    """
    return match_rating_comparison2(s1,s2)

#from Pattern package
@Appender(edit_distance_doc)
def levenshtein_distance_pattern(s1,s2):
    """Pattern implementation of Levenshtein distance, also known as Edit distance.
    """
    return levenshtein_distance_pattern2(s1,s2)

@Appender(edit_similarity_doc)
def levenshtein_similarity_pattern(s1,s2):
    """Pattern package implementation of Levenshtein similarity.
    """
    return levenshtein_similarity_pattern2(s1,s2)

@Appender(dice_doc)
def dice_coefficient_pattern(s1,s2):
    """Pattern package implementation of Dice coefficient.
    """
    return dice_coefficient_pattern2(s1,s2)

#From py_string package
@Appender(smith_waterman_dist_doc)
def smith_waterman_distance(s1,s2,match=2,mismatch=-1,gap_cost=1):
    """Smith-Waterman distance.
    """
    aligned = SmithWaterman(gap_cost=gap_cost,
            sim_func=lambda s1, s2: (int(match if s1 == s2 else mismatch)))
    return aligned.get_raw_score(s1,s2)

@Appender(needleman_wunsch_dist_doc)
def needleman_wunsch_distance_pystring(s1, s2, gap_cost=2, match=0):
    """Needleman-Wunsch distance also known as Seller metric.
    """
    aligned = NeedlemanWunsch(gap_cost=-gap_cost,
            sim_func=lambda s1, s2: (int(match if s1 == s2 else gap_cost)))
    return aligned.get_raw_score(s1,s2)

#Textsim self distances

@Appender(dice_doc)
def sorensen_distance_textsim(s1, s2):
    """Sorensen similarity also known as Dice similarity.

    TODO: generalizar con char ngrams
    """
    seq1 = bigrams(s1)
    seq2 = bigrams(s2)
    set1, set2 = set(seq1), set(seq2)
    return 2 * len(set1 & set2) / (float(len(set1) + len(set2)) or 1.0)

@Appender(needleman_wunsch_dist_doc)
def needleman_wunsch_distance_textsim(s1, s2, gap_cost=2):
    """Needleman Wunsch distance.
    """
    dist_mat = np.zeros((len(s1) + 1, len(s2) + 1), dtype=np.float)

    if isinstance(s1, bytes) or isinstance(s2, bytes):
        raise TypeError(_no_bytes_err)

    if s1 == s2:
        return 0
    rows = len(s1)+1
    cols = len(s2)+1

    if not s1:
        return cols-1
    if not s2:
        return rows-1

    prev = None
    cur = range(cols)
    for r in range(1, rows):
        prev, cur = cur, [r] + [0]*(cols-1)
        for c in range(1, cols):
            deletion = prev[c] + gap_cost
            insertion = cur[c-1] + gap_cost
            edit = prev[c-1] + (0 if s1[r-1] == s2[c-1] else gap_cost)
            cur[c] = min(edit, deletion, insertion)
            dist_mat[r, c] = cur[c]

    return cur[-1]

@Appender(needleman_wunsch_dist_doc)
def needleman_wunsch_similarity(s1, s2, gap_cost = 2, match = 0):
    """Is defined as a harmonic mean of Needleman Wunsch distance divided by the
    length of both strings.
    """
    p = needleman_wunsch_distance_pystring(s1,s2)/len(s1)
    q = needleman_wunsch_distance_pystring(s1,s2)/len(s2)

    sim = 2 * p * q / (p + q) if p + q > 0 else 0.

    return sim

@Appender(containment_similarity_doc)
def containment_distance(s1, s2):
    """Textsim Containment Similarity implementation.
    """
    seq1 = bigrams(s1)
    seq2 = bigrams(s2)
    set1, set2 = set(seq1), set(seq2)
    return len(set1 & set2) / (float(len(set1)) or 1.0)

if __name__ == '__main__':
    s1=input("Input text A:")
    s2=input("Input text B:")
    print("La subsecuencia mas larga con el metodo LCS es '%s'" % lcs(s1,s2))
    print("LCS distance:",longlcs(s1,s2))
    print("Damerau levenshtein distance:",damerau_levenshtein_similarity_textsim(s1,s2))
