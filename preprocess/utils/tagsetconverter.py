#!/usr/bin/env python
# -*coding: utf-8 -*-

""" This is an utility function to integrate all the possible tagsets
available in the NLP interfaces ()

First version will use the maps of tagsets made by nltk project.

"""

from nltk.tag.mapping import tagset_mapping

treebank_tagset = """\{220}
CC 	 Coordinating conjunction
CD 	 Cardinal number
DT 	 Determiner
EX 	 Existential there
FW 	 Foreign word
IN 	 Preposition or subordinating conjunction
JJ 	 Adjective
JJR  Adjective, comparative
JJS  Adjective, superlative
LS 	 List item marker
MD 	 Modal
NN 	 Noun, singular or mass
NNS  Noun, plural
NNP  Proper noun, singular
NNPS Proper noun, plural
PDT  Predeterminer
POS  Possessive ending
PRP  Personal pronoun
PRP$ Possessive pronoun
RB 	 Adverb
RBR  Adverb, comparative
RBS  Adverb, superlative
RP 	 Particle
SYM  Symbol
TO 	 to
UH 	 Interjection
VB 	 Verb, base form
VBD  Verb, past tense
VBG  Verb, gerund or present participle
VBN  Verb, past participle
VBP  Verb, non-3rd person singular present
VBZ  Verb, 3rd person singular present
WDT  Wh-determiner
WP 	 Wh-pronoun
WP$  Possessive wh-pronoun
WRB  Wh-adverb"""

universal_tagset = """\{220}
VERB verbs (all tenses and modes)
NOUN nouns (common and proper)
PRON pronouns
ADJ  adjectives
ADV  adverbs
ADP  adpositions (prepositions and postpositions)
CONJ conjunctions
DET  determiners
NUM  cardinal numbers
PRT  particles or other function words
X    other: foreign words, typos, abbreviations
.    punctuation
"""

#Func parse_tags based on scipy.constants.parse_constants

def parse_tags(d):
    """pendent function for future tags not included in nltk_data/taggers/. Eg my-own-tagset"""
    tags = {}
    for line in d.split('\n'):
        name = line[:55].rstrip()
        val = line[55:77].replace(' ', '').replace('...', '')
        val = float(val)
        uncert = line[77:99].replace(' ', '').replace('(exact)', '0')
        uncert = float(uncert)
        units = line[99:].rstrip()
        constants[name] = (val, units, uncert)
    return constants

def ptb2universal(tagged_text: list) -> list:
    """Convert Pen Tree Bank POS extended tag set (36 tags) into 
    universal tag set (12 tags).

    Parameters
    ----------

    tagged_text: list
                 A list of (word,POS Tag) returned by a pos tagger
                 in the extended form Eg. VBD, VBG, VBN, VBP, VBZ.

    Return
    ------

    new_text: list
              The same list of (word, POS Tag) but in the universal
              form, the above tags are change by VERB.

    """
    new_text = []
    mapa = tagset_mapping('en-ptb','universal')
    for word,pos in tagged_text:
        new_text.append((word,mapa[pos]))
    return new_text

