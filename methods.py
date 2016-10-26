#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Set de funciones para normalización de textos.
Created on Wed Aug 20 2014
Modified by analysis on Thu Aug 28 2014
Finish on (esto espera a que termine el experimento 14)
.. version: 0.2
.. release: 0.2-RC1
.. author: Abel Meneses abad
"""

import re, os
import string

LETTERS = ''.join([string.ascii_letters,'ñÑáéíóúÁÉÍÓÚüÜ'])

def url_string_recognition_support(text):
    for i in re.finditer('www\S*(?=[.]+?\s+?)|www\S*(?=\s+?)|http\S*(?=[.]+?\s+?)|http\S*(?=\s+?)',text):
        for j in range(i.start(),i.end()):
            if text[j] in string.punctuation:
                text = text[:j]+'_'+text[j+1:]
    return text

def punctuation_filter(text):
    #Asociados a signos de puntuación
    text = re.sub('\xc2|\xa0','  ',text)
    text = re.sub('\\xe2\\x80\\x9d|\\xe2\\x80\\x9c','"',text) #Del “” en ascii.
    text = re.sub(u'\u2022',' . ',text) #Viñeta tamaño medio.
    text = re.sub(u'\u201c|\u201d',' ',text) #Del “” en utf8.
    text = re.sub('\\xe2\\x80\\x99|\\xe2\\x80\\x98','\'',text) # Del ‘’ en ascii.
    text = re.sub(u'\u2018|\u2019','\'',text) # Del ‘’ en unicode
    text = re.sub('\\xe2\\x80\\x93',' - ',text) # Elimina guion largo ó – en ascii.
    text = re.sub(u'\u2013|\u2014|\u2015|\u2212',' - ',text)     #Guión largo codificación utf8.
    #~ text = re.sub('["]|[\']',' ',text) #Del comillas dobles y simples sin decodificar.
    text = re.sub(u'\u25cf',' . ',text) #Viñeta gigante.
    text = re.sub(u'\u2026','...',text) #Tres puntos.
    text = re.sub(u'\u2192','->',text) #Flecha sentido a la derecha.
    text = re.sub(u'\u2190','<-',text) #Flecha sentido a la izquierda.
    text = re.sub(u'\u2193|\u2191|\u2195',' ',text) #Flecha sentido hacia abajo/arriba.
    text = re.sub(u'\u2217','*',text) #Asterisco.
    text = re.sub(u'\u200b|\u21a8',' ',text) #Espacio en blanco o algo así.
    text = re.sub(u'\x0c','\n',text) #Caracter de control aparece a veces al inicio de un epígrafe

    #Based on letters
    text = re.sub(u'\ufb01','fi',text) #Error que introduce pdf2txt en el string 'fi'
    text = re.sub(u'\ufb00|\ufb03','ff',text) #Error que introduce pdf2txt en el string 'ff'
    text = re.sub(u'\ufb02','fl',text) #Error que introduce pdf2txt en el string 'fl'
    text = re.sub(u'\ufb04','nl',text) #Error que introduce pdf2txt en el string 'nl'
    #Todo: faltan más letras pero en Getting Real no están.
    
    #Greek symbols
    text = re.sub(u'\u03bb','Lambda',text) #Letras griegas.
    text = re.sub(u'\u03b8|\u0398','Theta',text) #Letras griegas.    
    text = re.sub(u'\u03bc','My',text) #Letras griegas.    
    text = re.sub(u'\u03b5|\u0395|\u03ad','Epsilon',text) #Letras griegas.    
    text = re.sub(u'\u03b1','Alfa',text) #Letras griegas.    
    text = re.sub(u'\u03b4|\u0394','Delta',text) #Letras griegas.    
    text = re.sub(u'\u03b9','Iota',text) #Letras griegas.    
    text = re.sub(u'\u03ba|\u039a','Kappa',text) #Letras griegas.    
    text = re.sub(u'\u03bd','Ny',text) #Letras griegas.
    text = re.sub(u'\u03c0','Pi',text) #Letras griegas.    
    text = re.sub(u'\u03c1','Ro',text) #Letras griegas.    
    #~ text = re.sub(u'\u03c2','P',text) #Letras griegas.    
    text = re.sub(u'\u03c3|\u03a3','Sigma',text) #Letras griegas.
    text = re.sub(u'\u03c4','Tau',text) #Letras griegas.  
    text = re.sub(u'\u03c5','Ipsilon',text) #Letras griegas.    
    text = re.sub(u'\u03c6|\u03a6','Fi',text) #Letras griegas.    
    text = re.sub(u'\u03c9|\u03a9','Omega',text) #Letras griegas.    
    text = re.sub(u'\u03cc|\u03bf','Omicron',text) #Letras griegas.    
    text = re.sub(u'\u03c2','Dseta',text) #Letras griegas.    
    
    
    #Math symbols
    text = re.sub(u'\u2260',' no-igual ',text) #desigual.
    text = re.sub(u'\u2229',' intersect ',text) #.
    text = re.sub(u'\u2264',' menor-o-igual ',text) #.
    text = re.sub(u'\u2265',' mayor-o-igual ',text) #.
    text = re.sub(u'\u2208',' existe ',text) #.
    text = re.sub(u'\u211d',' reales ',text) #.
    text = re.sub(u'\u2248',' aproximadamente-igual-a ',text) #.
    text = re.sub(u'\u266f','#',text) #.
    text = re.sub(u'\u2032','-',text) # Grados
    text = re.sub(u'\u2033','"',text) # 
    text = re.sub(u'\u2219','*',text) # 
    text = re.sub(u'\u2261',' congruente ',text) # 
    text = re.sub(u'\uf0ce',' en ',text) # 
    
    #Foreing chars
    text = re.sub(u'\u010d','c',text) #
    text = re.sub(u'\u0107','c',text) #
    text = re.sub(u'\u015b|\u0161','s',text) #
    text = re.sub(u'\u0155','r',text) #
    text = re.sub(u'\u010c','C',text) #
    text = re.sub(u'\u016f','u',text) #
    text = re.sub(u'\u0141','L',text) #
    text = re.sub(u'\u011b','e',text) #
    text = re.sub(u'\u0151','o',text) #
    
    #Fonetics chars
    text = re.sub(u'\u02d0','_',text) #
    text = re.sub(u'\u0261','g',text) #
    text = re.sub(u'\u0279|\u0159','r',text) #
    text = re.sub(u'\u025b','e',text) #
    return text

def del_contiguous_point_support(text):
    """ Allows to change continuous dot secuences by the same amount of spaces.

    ..Nota: no se puede reimplementar sin el finditer.
    Esta expresión r'(\w+)[.]\s*[.]+[\s|[.]]*' los cambia pero no hay como manejar el # de espacios.
    Y esta función se utiliza luego en la normalización del texto para el text-alignment.
    """
    for i in re.finditer('[.]\s*?[.]+?[\s|[.]]*',text): 
        for j in range(i.start(),i.end()):
            if text[j] == '.' or text[j]==' ':
                text = text[:j]+' '+text[j+1:]
    return text

def space_sentence_dot(text):
    text = re.sub('[.]\s*\n',' .\n ',text) #Garantizo que todos los puntos al final de las oraciones seran separados por si hay algun acronimo.
    return text

def contiguos_string_recognition_support(text):
    text = re.sub('(\w+)[-@.](?=\w+?)','\g<1>_',text) 

    #Added for Llanes, is under analisis if it most be here.
    text = re.sub('[.](?=,)|[.](?=;)|[.][[]|[.][]]',' ',text) #Este hay que modificarlo si vamos a usar abbrev
    text = re.sub('[.][)](?=\s*\n)|[.]["](?=[\s|)]*\n)|[.][:](?=\s*\n)','. ',text) #Este modificarlo si vamos a usar el replacers1
    text = re.sub('[.][)](?=\s*\w)|[.]["](?=\s*[\w)[])|[.][:](?=\s*\w)','. ',text) #Este modificarlo si vamos a usar el replacers1
    text = re.sub('[.][)](?=\s*[.])|[.][)](?=[,])',')',text)
    text = re.sub('[.][)](?=\s*")|[.]["](?=\s*")','. ',text)
    text = re.sub('[.]["](?=\s*[.])|[.][:](?=\s*")',' ',text)
    return text

def abbrev_recognition_support(text):
    """Proper names and abbrev recognition based on regular expressions.

    .. Note: In the case of U_S. the function will expect you filter at the end 
    of preprocessing the conditions of the dot in the expression. If a cappital 
    letter follows then this dot match with and end of sentence, else must be
    erased.
    """    
    
    #Proper names acronyms recognition and normalization
    text = re.sub('(\s[A-Z])[.](?!\n)','\g<1>_',text) 
    
    #Abbrev recognition and normalization
    text = re.sub('(Lic|Ph|Corp|Ms|Ing|Dr).','\g<1>_',text)

    return text

def del_char_len_one(text):
    text = re.sub('\s\w\s',' ',text)
    return text 

def add_text_end_dot(text):
     """
     .. function:: add_text_end_dot

     Procede de clean punctuation, pero ha sido despojada de todas sus funciones exceptuando la de agregar un punto al final del texto.
     Esta función ha sido rediseñada a partir de considerar que es el primer paso después de tener seccionado el texto al que se tratará con NLP.

     :param text: text to process.
     :param type: string.

     :returns text: The last char will be a dot, this is important for other functions that need to process the last sentence.

     .. author: Abel Meneses abad
     Created on Fri, 28 Feb 2014 
     Modify on Son Dic 6 2015
     Finish on XXXXX 2014
     .. release: 0.2
     """
     # Este fragmento de código coloca un punto en el final del texto. Objetivo: luego hay funciones que necesitan que el último caracter sea el punto final de la última oración.
     
     first_end_dot = text.rfind('.')      # posición del último punto final
     fragment = text[first_end_dot+1:]    # fragmento final después del punto
     
     A = set(LETTERS)
     B = set(fragment)
     
     if len(B.intersection(A)) != 0: #sí hay letras válidas en el fragmento
          text += ' .' 

     return text
