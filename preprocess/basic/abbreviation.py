import preprocess
import re
from ast import literal_eval

def expand_abbrevs(text: str, lang='en', type="classic") -> str:
    """Abbreviations expansion. Extend classical abbreviations with
    its corresponding long form written in a list of international
    abbreviations.

    Cite
    ----

    https://en.wikipedia.org/wiki/Abbreviation
    https://en.wikipedia.org/wiki/List_of_classical_abbreviations
    """

    with open(preprocess.__path__[0]+'/data/abbreviations.'+lang) as doc:
        txt = doc.read()
    abb = literal_eval(txt)
    newtext = ''

    #abbreviations/acronyms without dot separator
    for i in re.finditer('[A-Z]+\s', text):
        word = text[i.start():i.end()-1]
        if word in abb.keys():
            if newtext == '':
                newtext = text[:i.start()]+ abb[word]
                p = i.end()
            else:
                newtext = newtext + text[p-1:i.start()] + abb[word]
                p = i.end()
    if newtext != '':
        newtext = newtext + text[p-1:]
        text = newtext
        newtext = ''

    #abbreviations with not white space in between 
    for i in re.finditer('[A-Z]+?[a-z]*?[.]*?\S*[A-Z]+?[.](?=[ \t\r\f\v]+(?![A-Z]))',text):
        word = text[i.start():i.end()]
        if word in abb.keys():
            if newtext == '':
                newtext = text[:i.start()]+ abb[word]
                p = i.end()
            else:
                newtext = newtext + text[p:i.start()] + abb[word]
                p = i.end()
    if text != newtext:
        newtext = newtext + text[p:]
        text = newtext
        newtext = ''
    
    #abbreviations with white space in between
    for i in re.finditer('[A-Z]+?[a-z]*?[.]??\s+?[A-Z]+?[A-Za-z .]*[.](?!\n)', text):
        word = text[i.start():i.end()]
        if word in abb.keys():
            if newtext == '':
                newtext = text[:i.start()]+ abb[word]
                p = i.end()
            else:
                newtext = newtext + text[p:i.start()] + abb[word]
                p = i.end()
    if text != newtext:
        newtext = newtext + text[p:]
        text = newtext

    return text

    #TODO: in the future implement type=twitter, to expand and replace
    #twitter abbreviations
    #TODO: incorporate abbreviations.en as parquet format data, and test performance
    #TODO: program a helper funct that takes the repeated code, pass a
    #list of RE and return the expanded text
    #TODO: review duplicated abbreviations.keys with different value (E.g. "A.D.")
    #TODO: add a "list" parameter to expand only that list


def normalize_abbrevs(text: str, lang='en') -> str:
    """Recognize abbreviations marked with periods between initials and
    a dot after the last initial or the whole abbreviation. Usually
    some entity name abbreviations are written like this. The matched
    dots are underscored.

    This function is made to help sentence tokenizers with end-of-
    sentence ambiguities introduced by some of this dots. For helping
    with semantic analysis use abbreviation expansion 
    (``expand_abbrevs``), or deep Name Entity Tagging techniques.

    Abbreviation Definition
    ------------------------

    An abbreviation is a shortened form of a written word or phrase.
    Abbreviations may be used to save space and time [Merriam-Webster2020a]_.
    The accepted style here is "to use periods after uppercase letters,
    and after mixed-case abbreviations (E.g.: Jr., Mrs., A.M., ...)".

    Note
    ----

    In the case of U_S. the function will expect you filter at the end
    of preprocessing the conditions of dot in the expression. If a capital
    letter follows then this dot match with and end of sentence, other
    case must be erased.
    
    Warning
    -------

    Full lowercase abbreviations are not supported yet (E.g.: a.m., etc., ...).

    References
    ----------
    
    .. [Merriam-Webster2020a] . Definition of Abbreviation
        Merrian-Webster, 2020

    """

    #Proper name initials and acronyms normalization/underscoring
    text = re.sub('([A-Z]+?[a-z]*?)[.](?!\n)','\g<1>_',text)

    #TODO normalize abbreviations which includes lower letters 
    #E.g. 'p.' (pages), 'b. C.' (before Christ)

    return text


#https://www.researchgate.net/post/What_is_the_best_technique_to_detect_abbreviations_in_a_text
#
# First Approach
# --------------
#
# James Dominic O'Shea
# Manchester Metropolitan University
# I have developed a "brute force" approach for a similar problem I had
# with recognising what is someone's actual name in a text string. You
# could use a similar (divide and conquer" scheme. First, you could use
# a list of the most frequently occuring cases of positive cases
# (abreviations / acronyms). Second you could use a list of most
# frequently occurring words in the english language to rule out
# negative cases. This will leave a set of uncertain wrods which have
# lower frequency of occurrence to deal with. At this point I would
# investigate using an n-gram based classifier (e.g. trigrams or
# quadragrams of letters) trained on the two high frequency sets.
#
# Whatever approach you took, I would work by winnowing down the
# unknown cases in successive stages.
#
# You need to take account of misclassification - misses and false
# alarms which may occur either because an acronym is actually a real a
# real word e.g. Fuzzy Algorithm for Similarity Testing (FAST) or
# because a real word is so obscure it looks like an  abbreviation e.g.
# syzygy - an alignment of three celestial objects.
#
# Whatever apporach you take it sounds like it's going to be fun.!

# Second approach
# ---------------
#
# Tiago A. Almeida
# Universidade Federal de São Carlos
# We have designed a framework to normalize and expand noise and short
# text messages, such as SMS, tweets, etc. Basically, the most common
# slangs, typos, symbols and abbreviations are detected and replaced
# for their standard english words. You can also enrich the text sample
# by inserting concepts semantically related with the message context.
#
# We have proved that such preprocessing can greatly improve the
# classification and clustering performances.
#
# The TextExpansion tool is open-source and publicly available at
# http://lasid.sor.ufscar.br/expansion/
#
# Moreover, you can find other uselful machine learning tools available
# at http://lasid.sor.ufscar.br/ml-tools/