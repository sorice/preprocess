#!/usr/bin/env python 3.5
# -*- coding: utf-8 -*-

"""Normalización de texto proveniente de pdftotx.
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
- Change the rest of punctuation chars by a whitespace, the objetive if don't lose the original position of the sentence.
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
# Exp1: Expresiones que tienen que ver con el signo '.'
(r'[.](?=\s+?[a-z]+?)', '_'),   #Note: Lower case at the begining of the sentence - spell error - isn't trated as uper(Exp1). View grammar and spell checker section article.
(r'[.](?=\s+\w+?)', '##1'), #Exp1: signos de "." al final de la oración seguido por 1 o más espacios en blanco cambiar por SPECIAL_STRING. 

(r'[\t|\f]','\n'),      # Tabs changed for \n
(r'[.](?=\s*\n)','##1\n'),              # Paragraph end

#Exp2: ":" seguido de mayúscula campiar por punto. 
#Note that can acept new cases in the form "char[n-whitespace][Uper-case-letter]"
(r'[:](?=\s+?[A-Z]+?)', '##2'),
(r'[:](?=\s*?"+?[A-Z]+?)', '##2'),  #Match cases were ':' are follow by [0 or n whitespace][1 or n simbol chars like '"'][almost 1 uper case]
(r'[:](?=\s*?\n)','##2'),           #Match cases were ':' are follow by 0 or n whitespace, and then '\n', the next string is always an independent idea.

('\r\n','\n'),  #Convert Windows end-of-line on Unix end-of-line.

#Exp3: found empty lines, and substitute N consecutives "\n" by N-1 whitespace char + \n. 
(r'\n(?=\s*?\n)','##3'),

#Exp4: Relative to line skip.
(r'-\n',''),                # Word division eliminated.
(r'\n(?=\s*?[a-z]+?)','##6'),   # Sentence division for end of margin. 
(r'\n(?=\w+?)','##7'),      # Delete any '\n' no follow by a letter(alpha-numeric).
(r'\n(?=\s{0,100}?["$%()*+&,-/;:¿¡<=>@[\]^`{|}~]{0,100}?\s{0,100}?[A-Z]+?)','##1'),

#Exp3: Los signos "!" y "?" cambiar por PUNTO
(r'[?!]','##5'), 
(r'\xe2\x80\xa2','##5'),        # Soporte para las viñetas

#Exp5: eliminar el resto de los signos de puntuación.
(r'["$%()*+&,-/;:¿¡<=>@[\]^`{|}~]','##8'),

(r'[\']','##9'),             # Contractions are not supported.

#Clean other . non constituent an "sentence-end". E.g: "...",
(r'[.]','##0'),

# Change all founded exp by "."
(r'##1',' . '),(r'##2',' . '),(r'##3',' . '),(r'##4',' . '),(r'##5',' . '),
(r'##6',' '),(r'##7',' '),(r'##8',' '),(r'##9',' '),(r'##0',''),

# Delete consecutives points sections. 'apdb' is a rare code tha represent 'Abel Plagiarism Detection Branch'
(r'[.](?=\s+?\w+?)', 'apdb'),       # Match '.' follow by alpha-numeric = sentence-end
(r'[.]',' '),                       # Every generated point not exactly follow by a letter -> clean

# Refining text
(r'apdb+',' .'),                        # return the "." char necessary for found_sentences method
(r'\n',' '),
(r'\s+(?=\s)',''),
]

class Replacer(object):
    def __init__(self, patterns=replacement_patterns):
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]
    def replace(self, text):
        s = text
        for (pattern, repl) in self.patterns:
            (s, count) = re.subn(pattern, repl, s)
        return s

