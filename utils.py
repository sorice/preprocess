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

import swalign
import re
from preprocess.methods import add_text_end_dot, abbrev_recognition_support

match = 2
mismatch = -1
scoring = swalign.NucleotideScoringMatrix(match, mismatch)
sw = swalign.LocalAlignment(scoring)

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

def alignSentences(preproc_text, original_text):
    """Align preprocessed sentences vs original sentences returning the original boundaries.
    Useful for real applications, to recover the original sentence position or fragment position
    and show in a web or desktop application view.

    :param preproc_text: preprocessed text string
    :param original_text: original text string
    :returns alignedSentences: [(sent ID, preprocessed sentence, offset original sent, length orig sent)]
    :rtype: list of tuples

    .. author: Abel Meneses abad
    Finish on Fri, 9 Sept 2016
    Next_revision on Sun Aug 3 2014
    """
    alignedSentences = []
    offsetB = 0
    norm_orig_text = normalize(original_text)

    if norm_orig_text.count('.') < preproc_text.count('.'):
        raise Exception("Preprocess Error: number of preproc periods most be less or equal than normalize original text periods.")


    for i, (sentA, offsetA, lengthA) in enumerate(getSentA(preproc_text)):
        maxScore =-1; score = 0
        prevPoint = 0#len(sentA)-2
        nextPoint = 0
        
        #Sí llegamos a la última oración entonces
        if i == preproc_text.count('.')-1:
            lengMax = len(norm_orig_text)
            tuple = (i, sentA, offsetB, lengMax)
            alignedSentences.append(tuple)
            break
        
        #Sí no es la última oración compara hasta encontrar el score max.
        while(score >= maxScore):
            lengMax = nextPoint
            maxScore = score
            #print('>>>>>>>>>>>>>>>>>>>>>>',offset, nextPoint, prevPoint)
            sentB, nextPoint, prevPoint = getSentB(norm_orig_text, offsetB, nextPoint, prevPoint)
            sentB = sentB.replace('\n',' ') #avoid some bugs on swalign function
            if i >= 37:
                print('-----offsetB:',offsetB,'---- from pos:', prevPoint, '-----to pos:',nextPoint)
            alignment = sw.align(sentA[-round(len(sentA)*0.5):], sentB[-round(len(sentA)*0.5):])
            score = alignment.score
            matches = alignment.matches
            if i >= 37:
                print('i',i,'score:',score,'maxScore:',maxScore, 'matches:',matches)
                print('frag-sentA:',sentA[-round(len(sentA)*0.5):],'frag-sentB:',sentB[-round(len(sentA)*0.5):])
            
            #Short sentence exceptions
            if len(sentA) < 10:
                maxScore = score
                lengMax = nextPoint
                break

        tuple = (i, sentA, offsetB, lengMax)
        alignedSentences.append(tuple)

        if i >= 0:
            print('#############RESULTADO de la ORACIÓN :', i)
            print('score max:',maxScore, 'offsetB:', offsetB, 'lengthB:',lengMax-offsetB)
            print('sentB:',original_text[offsetB:lengMax])
            print('sentA:',sentA)
            print('\n***************')

        offsetB = lengMax+1

    return alignedSentences

def getSentA(doc1):
    offset = 0
    for i in re.finditer('\.',doc1):
        sentA = doc1[offset:i.end()]
        yield sentA, offset, i.end()
        offset = i.end()+1

def getSentB(text2, offsetB, nextPoint,prevPoint):
    posB = text2[offsetB+prevPoint:].find('.')
    prevPoint += posB+1
    sentB = text2[offsetB:offsetB+prevPoint]
    nextPoint = offsetB + prevPoint
    return sentB, nextPoint, prevPoint

def normalize(text_orig):
    replacement_patterns = [(r'[:]\n','. '),
                            (r':(?=\s+?[A-Z]+?)|:(?=\s*?"+?[A-Z]+?)','.'),
                            (r'[?!]','.'),
                            (r'(\w+?)(\n)(?=["$%()*+&,-/;:¿¡<=>@[\\]^`{|}~\t\s]*(?=.*[A-Z0-9]))','\g<1>.'), # any alphanumeric char
                            # follow by \n follow by any number of point sign follow by a capital letter, replace by alphanumerig+.
                            (r'(\w+?)(\n)(?=["$%()*+&,-/;:¿¡<=>@[\\]^`{|}~\t\s\n]*(?=[a-zA-Z0-9]))','\g<1>.'),# any alphanumeric char
                            # follow by \n follow by any number of point sign follow by a letter, replace by alphanumerig+.
                            (r'[:](?=\s*?)(?=["$%()*+&,-/;:¿¡<=>@[\\]^`{|}~\t\s]*[A-Z]+?)','.'),
                            (r'(\w+?\s*?)\|','\g<1>.'),
                            (r'\n(?=\s*?[A-Z]+?)','.'),
                            ]
    text_orig, temp = re.subn(re.compile(replacement_patterns[0][0]),replacement_patterns[0][1],text_orig)
    text_orig, temp = re.subn(re.compile(replacement_patterns[1][0]),replacement_patterns[1][1],text_orig)
    text_orig, temp = re.subn(re.compile(replacement_patterns[2][0]),replacement_patterns[2][1],text_orig)
    text_orig, temp = re.subn(re.compile(replacement_patterns[3][0]),replacement_patterns[3][1],text_orig)
    text_orig, temp = re.subn(re.compile(replacement_patterns[4][0]),replacement_patterns[4][1],text_orig)
    text_orig, temp = re.subn(re.compile(replacement_patterns[5][0]),replacement_patterns[5][1],text_orig)
    text_orig, temp = re.subn(re.compile(replacement_patterns[6][0]),replacement_patterns[6][1],text_orig)
    text_orig, temp = re.subn(re.compile(replacement_patterns[7][0]),replacement_patterns[7][1],text_orig)
    text_orig = abbrev_recognition_support(text_orig)
    text_orig = add_text_end_dot(text_orig)#append . final si el último caracter no tiene punto, evita un ciclo infinito al final.
    return text_orig

