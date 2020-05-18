#!/usr/bin/env python 3.5
# -*- coding: utf-8 -*-

"""Normalización de texto proveniente de pdftotext.
Created on Sat Nov 30 2013
Modified by clean_punctuation on Thu Aug 14 2014
Modified by analysis on Thu Aug 28 2014
Modified by analysis on Sat Dic 27 2014
Finish on (esto espera a que termine el experimento 14)
.. version: 0.3.1
.. release: 0.2
.. author: Abel Meneses abad
"""

import re
import string

"""
Clean the text with regular expressions with the following principles:
    - Chains of whitespace are not important in this step.
    - Collect de ["!","?",":"(followed by \n),"."] subset an change them by the string "apdb"(end of sentence).
    - If possible try to change everything by the same length of whitespace, less problems in alignment or better efficiency.
    - Restore "."(end of sentence) changing the 'apdb' string by dot.
    - do not lowercase before abbreviation analysis
    - [A-Z]+[.]+\n must be replaced by [A-Z]+[..]\n in case that Abbreviation be at the end
        only after preprocess abbreviations, acronyms
"""

#: support for date format expressions like day/month/year still pendent.
#: support for source-code text AND seudo-code text still pendent. E.g. "object.function", "<file> chmod -R <###>"
#: support for paths like 'C:\file1\file2' still pendent. 

# Core '.' expressions.
replacement_patterns = [
# Section I Discourse Elements: end of paragraph, end of the sentence, .

# Related to paragraph-end-detection.
('\r\n','\n'),                      # Windows period convert to Unix period.
(r'[\t]','    '),                  # Tabs changed by four whitespace.
(r'[.](?=\s*?\n)','##1\n'),         # Paragraph end detection
(r'(\w+?)\s*?\|','\g<1> ##1'),      # Rare divition in writed expression. (Explanation: some sentences in PAN corpus)
(r'(\w+)\n\n', '\g<1> ##1'),

# Related to Sentence Boundaries Detection
(r'(\w+?\s*?)[.?!](?=\s+?[A-Z])','\g<1> ##1'), # Correct & common end of sentence.
(r'[?!]','##1'), #Problem: punctuations are not alphanum, so ? predeced by punctuation sign not detected in previous line

(r'[.?!](?=[\'"`]+?\s+?)','##1'), #Match cases were '.|?|!' are follow by [1 or n quote simbol][1 or n whitespace] -> means that detect the end or a quoted sentence. (Eg. "Where is it?" Jacob asked.)
(r'[.](?=\s+?[a-z]+?)', '_'),   #Note: Lower case after a dot sentence - grammar error - isn't analyzed as uppercase (##1). View grammar and spell checker in QtNLP-Linguist/doc/arquitectura/normalization article. (Eg1. "U.S. is the nation at north.")(Eg2. "Llegó a las 8 a.m. en auto.")
(r'[.](?=\s*?["\'-`]+?\s*?\w+?)', '##1'), #Match cases were '.' are follow by [0 or n whitespace][1 or n quote simbol][follow by 0 or n whitespace][follow by any alphanumeric char. (Eg1. "He said.'We most go up.'"; Eg2. "He said. ' We most go up.'") 

#Section II: Regular expressions related to ":".
(r'[:](?=\s*?\n)','##2'),           #Match cases were ':' are follow by 0 or n whitespace, and then '\n', the next string is always an independent idea.
(r'(\w\w):(?=\s+?[A-Z]+?)', '\g<1>##2'), #TODO review if this option is better replace by ' '.
(r'(\w\w):(?=\s*?"+?[A-Z]+?)', '\g<1>##2'),  #Match cases were ':' are follow by [0 or n whitespace][1 or n simbol chars like '"'][almost 1 uper case]


#Section III:: Relative to line skip.
(r'\n(?=\s*?\n)','##6'),        #found empty lines and deleted: "\n" follow by N-1 whitespace char + \n. 
(r'-\n(?=[a-z]+?)',''),                    # Word division eliminated.
(r'\n(?=\s*?[a-z]+?)','##6'),   # Sentence division for end of margin. 
(r'\n(?=\s*?[A-Z]+?)','##3'),   # New line that start in CAPITAL LETTER is a new sentences. 
                                # Problem: first name at the beginning.
(r'\n(?=\w+?)','##7'),          # Delete any '\n' follow by non-alphanumeric.
(r'\n(?=\s*?["$%()*+&,-/;:¿¡<=>@[\\]^`{\|}~]*?\s*?[A-Z]+?)','##1'), 
        # salto línea [?= 0-n whitespace][?= 0-n punct marks][?= by 0-n whitespace] 
        # ?= at least a CAPITAL letter. 
        #(Explanation: this kind of sequence can appear after pdftotext convertion)

#Section IV: Rare starts of a sentence 
(r'\xe2\x80\xa2','##5'),        # Soporte para las viñetas Problem: this line must be replaced/updated for python3

#Section V: After all transformations clean the residuary punctuation marks.
(r'["$%()*+&\',-/;:¿¡<=>@\\^`{\|}~]|\[|\]','##8'),

#Section VI: Postprocessing
#Clean other . non constituent an "sentence-end". E.g: "...",
(r'[.]','##0'),

# Change all founded exp by "." (The next two lines were made during development to recognize any failure)
(r'##1',' . '),(r'##2',' . '),(r'##3',' . '),(r'##4',' . '),(r'##5',' . '),
(r'##6',' '),(r'##7',' '),(r'##8',' '),(r'##9',' '),(r'##0',''),

# Delete consecutives points sections. 'apdb' is a rare code tha represent 'Abel Plagiarism Detection Branch'
(r'(\w+?\s*?)[.]','\g<1>apdb'),    # Match '.' follow by alpha-numeric = sentence-end
(r'[.]',' '),                       # Every generated point not exactly follow by a letter -> clean

# Refining text
(r'apdb+',' .'),                    # return the "." char necessary for found_sentences method
(r'\n',' '),                        # Erase any residual \n 
(r'\s+(?=\s)',''),                  # Erase any residual whitespace secuence
]

class Replacer(object):
    def __init__(self, patterns=replacement_patterns):
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]
    def replace(self, text):
        s = text
        for (pattern, repl) in self.patterns:
            (s, count) = re.subn(pattern, repl, s)
        return s

