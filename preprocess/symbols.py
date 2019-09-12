#!/usr/bin/env python 3.5

import re

def replace(text):
    """
    Replace none common symbols by more common similar char, symbols or tokens.
    E.g.: Greek symbols like 'α' is replaced by 'alpha'.

    :Explanation:

    Frecuently the PDF to Text transformation translates some chars into a
    different-meaning character or symbol. E.g.: 'fi' is changed into 'ﬁ', then
    the token 'file' is converted into 'ﬁle', changing the meaning completely.

    """
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
    text = re.sub(u'\x13',' ',text) #Caracter de control

    #Based on letters
    text = re.sub(u'\ufb01','fi',text) #Error que introduce pdf2txt en el string 'fi'
    text = re.sub(u'\ufb00|\ufb03','ff',text) #Error que introduce pdf2txt en el string 'ff'
    text = re.sub(u'\ufb02','fl',text) #Error que introduce pdf2txt en el string 'fl'
    text = re.sub(u'\ufb04','nl',text) #Error que introduce pdf2txt en el string 'nl'
    #Todo: faltan más letras pero en Getting Real no están.

    #Greek symbols
    # text = re.sub(u'\u03bb','Lambda',text) #Letras griegas.
    # text = re.sub(u'\u03b8|\u0398','Theta',text) #Letras griegas.
    # text = re.sub(u'\u03bc','My',text) #Letras griegas.
    # text = re.sub(u'\u03b5|\u0395|\u03ad','Epsilon',text) #Letras griegas.
    # text = re.sub(u'\u03b1','Alfa',text) #Letras griegas.
    # text = re.sub(u'\u03b4|\u0394','Delta',text) #Letras griegas.
    # text = re.sub(u'\u03b9','Iota',text) #Letras griegas.
    # text = re.sub(u'\u03ba|\u039a','Kappa',text) #Letras griegas.
    # text = re.sub(u'\u03bd','Ny',text) #Letras griegas.
    # text = re.sub(u'\u03c0','Pi',text) #Letras griegas.
    # text = re.sub(u'\u03c1','Ro',text) #Letras griegas.
    # #~ text = re.sub(u'\u03c2','P',text) #Letras griegas.
    # text = re.sub(u'\u03c3|\u03a3','Sigma',text) #Letras griegas.
    # text = re.sub(u'\u03c4','Tau',text) #Letras griegas.
    # text = re.sub(u'\u03c5','Ipsilon',text) #Letras griegas.
    # text = re.sub(u'\u03c6|\u03a6','Fi',text) #Letras griegas.
    # text = re.sub(u'\u03c9|\u03a9','Omega',text) #Letras griegas.
    # text = re.sub(u'\u03cc|\u03bf','Omicron',text) #Letras griegas.
    # text = re.sub(u'\u03c2','Dseta',text) #Letras griegas.


    #Math symbols
    # text = re.sub(u'\u2260',' no-igual ',text) #desigual.
    # text = re.sub(u'\u2229',' intersect ',text) #.
    # text = re.sub(u'\u2264',' menor-o-igual ',text) #.
    # text = re.sub(u'\u2265',' mayor-o-igual ',text) #.
    # text = re.sub(u'\u2208',' existe ',text) #.
    # text = re.sub(u'\u211d',' reales ',text) #.
    # text = re.sub(u'\u2248',' aproximadamente-igual-a ',text) #.
    text = re.sub(u'\u266f','#',text) #.
    text = re.sub(u'\u2032','-',text) # Grados
    text = re.sub(u'\u2033','"',text) #
    text = re.sub(u'\u2219','*',text) #
    # text = re.sub(u'\u2261',' congruente ',text) #
    # text = re.sub(u'\uf0ce',' en ',text) #

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
