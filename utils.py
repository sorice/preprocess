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