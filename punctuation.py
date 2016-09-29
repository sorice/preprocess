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

# Cleaning de text
"""Clean the text with regular expressions with the following principles:
- Chains of whitespace are not important in this step.
- Colect de ["!","?",":"(followed by \n),"."] subset an change them by the string "PUNTO"(end of sentence).
- Change the rest of punctuation marks by a whitespace, the objetive if don't lose the original position of the sentence.
- Restore "."(end of sentence) changing the 'PUNTO' string by dot.
"""
#This are simple rules without anti-trick.
#Note: support for non-indexing non-content doc section still pendent. E.g. "Reference" section OR "Apendix" section of a Book must no be indexed.
    #: support for collocations still pendent. E.g. 'Open Source'. Must be detected first with NLTK and markes as 'Open-Source'.
    #: support for date format expressions like day/month/year still pendent.
    #: support for source-code text AND seudo-code text still pendent. E.g. "object.function", "<file> chmod -R <###>"
    #: support for file routes like 'C:\file1\file2' still pendent. 

# Core '.' expressions.
replacement_patterns = [
# Section I: Expressions related to the period at the end of the sentence.

(r'(\w+?\s*?)[.?!](?=\s+?[A-Z])','\g<1> ##1'), # Correct & common end of sentence.

(r'[.?!](?=[\'"`]+?\s+?)','##1'), #Match cases were '.|?|!' are follow by [1 or n quote simbol][1 or n whitespace] -> means that detect the end or a quoted sentence. (Eg. "Where is it?" Jacob asked.)
(r'[.](?=\s+?[a-z]+?)', '_'),   #Note: Lower case at the begining of the sentence - spell error - isn't trated as uper(Exp1). View grammar and spell checker section article. (Eg1. "U.S. is the nation at north.")(Eg2. "Llegó a las 8 a.m. en auto.")
(r'[.](?=\s*?["\'`]+?\s*?\w+?)', '##1'), #Match cases were '.' are follow by [0 or n whitespace][1 or n quote simbol][follow by 0 or n whitespace][follow by any alphanumeric char. (Eg1. "He said.'We most go up.'"; Eg2. "He said. ' We most go up.'") 

# Standarize line skip before "paragraph end detection regular expression"
('\r\n','\n'),                      # Windows period convert to Unix period.
(r'[\t]','    '),                  # Tabs changed by \n.
(r'[.](?=\s*?\n)','##1\n'),         # Paragraph end detection
(r'(\w+?)\s*?\|','\g<1> ##1'),      # Rare divition in writed expression. (Explanation: some sentences in PAN corpus)
(r'(\w+)\n\n', '\g<1> ##1'),

#Section II: Regular expressions related to ":".
(r'[:](?=\s+?[A-Z]+?)', '##2'),
(r'[:](?=\s*?"+?[A-Z]+?)', '##2'),  #Match cases were ':' are follow by [0 or n whitespace][1 or n simbol chars like '"'][almost 1 uper case]
(r'[:](?=\s*?\n)','##2'),           #Match cases were ':' are follow by 0 or n whitespace, and then '\n', the next string is always an independent idea.

#Section III:: Relative to line skip.
(r'\n(?=\s*?\n)','##6'),        #found empty lines and deleted: "\n" follow by N-1 whitespace char + \n. 
(r'-\n',''),                    # Word division eliminated.
(r'\n(?=\s*?[a-z]+?)','##6'),   # Sentence division for end of margin. 
(r'\n(?=\s*?[A-Z]+?)','##3'),   # New line that start in CAPITAL LETTER is a new sentences. Problem: first name at the beginning.
(r'\n(?=\w+?)','##7'),          # Delete any '\n' follow by non-alphanumeric.
(r'\n(?=\s*?["$%()*+&,-/;:¿¡<=>@[\\]^`{\|}~]*?\s*?[A-Z]+?)','##1'), # salto línea [follow by 0-100 whitespace][follow by 0-100 punct marks][follow by 0-100 whitespace] follow by at least a CAPITAL letter. (Explanation: this kind of secuence can appear after pdftotext convertion)

#Section IV: Rare starts of a sentence 
(r'\xe2\x80\xa2','##5'),        # Soporte para las viñetas

#Section V: After all transformations clean the residuary punctuation marks.
(r'["$%()*+&,-/;:¿¡=@[]^`{}~\\]','##8'),
(r'[<>]','##8'),
(r'\|','##8'),                              #After some test it's prove that not work joined with other simbols.

(r'[\']','##9'),             # Contractions are not supported.

#Section VI: Postprocessing
#Clean other . non constituent an "sentence-end". E.g: "...",
(r'[.]','##0'),

# Change all founded exp by "." (The next two lines were made during development to recognize any failure)
(r'##1',' . '),(r'##2',' . '),(r'##3',' . '),(r'##4',' . '),(r'##5',' . '),
(r'##6',' '),(r'##7',' '),(r'##8',' '),(r'##9',' '),(r'##0',''),

# Delete consecutives points sections. 'apdb' is a rare code tha represent 'Abel Plagiarism Detection Branch'
(r'(\w+?\s*?)[.]','\g<1>apdb'),
#(r'[.](?=\s+?\w+?)', 'apdb'),       # Match '.' follow by alpha-numeric = sentence-end
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

