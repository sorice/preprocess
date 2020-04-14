#!/usr/bin/env python 3.6

import preprocess
A = open('data/FS_FSociety.txt').read()
B = preprocess.normalize(A).lower()
C = preprocess.remove_stopwords(B)
from preprocess import CollocationList
coll2 = CollocationList(C)
coll2.find_collocations()
collocations = coll2.head(40)
D = preprocess.utils.hypenation(C,collocations)
coll3 = CollocationList(D)
coll3.find_collocations()
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r"\s+", gaps=True)
tokens = tokenizer.tokenize(D)
print ("Total inicial de palabras: ", len(B.split()))
print ("Total sin stopwords: ", len(C.split()))
print ("Total after collocations hypen: ", len(D.split()))
tokens_unique=set([])
tokens_unique = set(tokens)
print ("Palabras únicas:", len(tokens_unique))
#Inicializar un diccionario para guardar el # de apariciones de cada palabra.
dict = {}
for word in tokens_unique:
    dict[word]=0
#Diccionario con word = # apariciones.
for token in tokens:
    dict[token]+=1
#Operar con una tupla puede ser mejor. Lista([#apariciones,word])
tupla = []
for word in dict:
    tupla.append([dict[word],word])
tupla=sorted(tupla)
print("Las palabras más utilizadas son:")
for i in range(1,10):
    print (tupla[-i][1],":",tupla[-i][0])

print(coll2.head(20))
print(coll3.head(20))