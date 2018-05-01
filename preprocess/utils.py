#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Utilitie functions to standarize the IN-object to the preprocessing method.
If the user enter a path to preprocess a list of document, or a doc the module will no fail.
Created on Fry Sept 02 2016
Modified by analysis on
Finish on
.. version: 0.1
.. release: 0.1-RC1
.. author: Abel Meneses abad
"""

import re
from preprocess.methods import add_text_end_dot, abbrev_recognition_support
from preprocess.methods import contiguos_string_recognition_support, del_contiguous_point_support

def read_name_files_in_path(path=None):
    """Return a list with the file's names on a path."""

    if path == None:
        path = os.getcwd()

    try: # Por lo tanto le digo que lo intente
        os.system('ls '+ path + ' > ficheros.txt')
    except: # y lanzo una excepción si no se puede
        print ('No existe esta ruta o está mal escrita.') # Luego veremos como detectar si está mal o es que no existe.

    lista_ficheros = open('ficheros.txt','r').read()

    # File with the list of files in path
    count = 0
    nombres = {}

    for nombre_de_fichero in lista_ficheros.split('\n'):
        nombres[count] = nombre_de_fichero
        count+=1

    return nombres

def alignSentences(preprocessed_text, original_text):
    """Align preprocessed sentences vs original sentences returning the original boundaries.
    Useful for real applications, to recover the original sentence position or fragment position
    and show in a web or desktop application view.

    :param preprocessed_text: preprocessed text string
    :param original_text: original text string
    :returns alignedSentences: [(sent ID, preprocessed sentence, offset original sent, length orig sent)]
    :rtype: list of tuples

    .. author: Abel Meneses abad
    Finish on Fri, 9 Sept 2016
    Next_revision on (an Optimization is predicted)
    """
    alignedSentences = []
    offsetB = 0
    norm_orig_text = extra_normalize(original_text)

    #if norm_orig_text.count('.') < preprocessed_text.count('.'):
     #   raise Exception("Preprocess Error: number of preprocessed periods most be less or equal than normalize original text periods.")

    for i, (sentA, offsetA, lengthA) in enumerate(getSentA(preprocessed_text)):
        maxScore =-1; score = 0
        prevPoint = 0#len(sentA)-2
        nextPoint = 0
        iqualScore = 0;prevFrag='';jaccard_measure = 0; X = {()}; Y={()}
        prev_jaccard_measure = 1.0
        k = 0.5

        if len(sentA) > 200:
             k = 0.1
        else: k=0.5

        #Sí llegamos a la última oración entonces
        if i == preprocessed_text.count('.')-1:
            lengMax = len(norm_orig_text)
            tuple = (i, sentA, offsetB, lengMax)
            alignedSentences.append(tuple)
            break

        #Sí no es la última oración compara hasta encontrar el score max.
        while(score >= maxScore):
            prev_jaccard_measure = jaccard_measure; prev_setA = X; prev_setB = Y
            lengMax = nextPoint
            maxScore = score

            #Get sentence B and prepare it to calc distances
            sentB, nextPoint, prevPoint = getSentB(norm_orig_text, offsetB, nextPoint, prevPoint)
            sentB = sentB.replace('\n',' ') #avoid some bugs on swalign function

            #Calc distances Jaccard
            jaccard_measure, X, Y = jaccard ( sentA , sentB) #Second measure only to lookfor errors
            score = jaccard_measure

            #The same consecutives sentence exception
            if prevFrag == sentB[-round(len(sentA)*k):]:
                break
            prevFrag = sentB[-round(len(sentA)*k):] #keep the previous fragment to know if the next sent is the same as before. SmithWaterman move forward to the next sentence.

            #Short sentence exceptions
            if len(sentA) < 14:
                maxScore = score
                lengMax = nextPoint
                break

            #Infinite loop exception
            if score == maxScore:
                iqualScore += 1
            if iqualScore == 20:
                break

        tuple = (i, sentA, offsetB, lengMax)
        alignedSentences.append(tuple)

        offsetB = lengMax

    return alignedSentences

def getSentA(doc1):
    """
    alignSentences auxiliar function to get the sentences of the preprocessed text.
    """
    offset = 0
    for i in re.finditer('\.',doc1):
        sentA = doc1[offset:i.end()]
        yield sentA, offset, i.end()
        offset = i.end()+1

def getSentB(text2, offsetB, nextPoint,sentLength):
    """
    alignSentences auxiliar function to get the sentences of the original text.
    """
    posB = text2[offsetB+sentLength:].find('.')
    sentLength += posB+1
    sentB = text2[offsetB:offsetB+sentLength]
    nextPoint = offsetB + sentLength
    return sentB, nextPoint, sentLength

def extra_normalize(text_orig):
    """
    This function allows a simple normalization to the original text to make
    possible the aligning process.

    The replacement_patterns were obtained during experimentation with real text
    it is possible to add more or to get some errors without new rules.

    :Note: very important, every rule in replacement_patterns do not change the
    length of the original text, only replace patterns with same length string.
    This process is different to the in preProcessFlow.
    """
    replacement_patterns = [(r'[:](?=\s*?\n)','##1'),
                            (r'\xc2|\xa0',' '),
                            (r'(\w\s*?):(?=\s+?[A-Z]+?)|(\w\s*?):(?=\s*?"+?[A-Z]+?)','\g<1>##2'),
                            (r'[?!]','##3'),
                            (r'(\w+?)(\n)(?=["$%()*+&,-/;:¿¡<=>@[\\]^`{|}~\t\s]*(?=.*[A-Z0-9]))','\g<1>##4'), # any alphanumeric char
                            # follow by \n follow by any number of point sign follow by a capital letter, replace by alphanumerig+.
                            (r'(\w+?)(\n)(?=["$%()*+&,-/;:¿¡<=>@[\\]^`{|}~\t\s\n]*(?=[a-zA-Z0-9]))','\g<1>##5'),# any alphanumeric char
                            # follow by \n follow by any number of point sign follow by a letter, replace by alphanumerig+.
                            (r'[:](?=\s*?)(?=["$%()*+&,-/;:¿¡<=>@[\\]^`{|}~\t\s]*[A-Z]+?)','##6'),
                            (r'(\w+?\s*?)\|','\g<1>##7'),
                            (r'\n(?=\s*?[A-Z]+?)','##8'),
                            (r'##\d','apdbx'),
                            ]

    for (pattern, repl) in replacement_patterns:
            (text_orig, count) = re.subn(pattern, repl, text_orig)

    text_orig = del_contiguous_point_support(text_orig)
    text_orig = contiguos_string_recognition_support(text_orig)
    text_orig = abbrev_recognition_support(text_orig)
    text_orig = re.sub(r'apdbx+','.', text_orig)
    text_orig = add_text_end_dot(text_orig)#append . final si el último caracter no tiene punto, evita un ciclo infinito al final.
    return text_orig

def jaccard(text1,text2):
    sentA1 = re.sub(r'[!"#$%&()\'*+,-/:;<=>?@\\^_`{|}~.\[\]]',' ', text1)
    sentB1 = re.sub(r'[!"#$%&()\'*+,-/:;<=>?@\\^_`{|}~.\[\]]',' ', text2)
    setA = set(sentA1.split())
    setB = set(sentB1.split())
    if len(setA.union(setB)) == 0:
        return 0, sentA1, sentB1
    else:
        return len(setA.intersection(setB))/float(len(setA.union(setB))), sentA1, sentB1

class Pipeline():
    """An easier function or class that allow to make a full Pipeline
    with the parameters that user wants. This will be implemented in version 2.0

    TODO: review sklearn Pipeline class to take ideas about how to do it.
    """
    steps = {
    urls: True,
    abbrev: True,
    contractions = False,
    }
