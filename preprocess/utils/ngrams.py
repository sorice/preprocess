#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Util functions based on ngrams elaboration.

Created on Fry Nov 10 2017
Modified by analysis on
Finish on
.. version: 0.1
.. release: 0.1-RC1
.. author: Abel Meneses abad
"""

from collections import defaultdict
from nltk.tree import Tree
from collections import deque
from nltk.util import skipgrams as nltk_skipgrams
from .decorators import Appender

def get_dict_from_list(dicc,lista, nivel,head_nodes):
    pendents = []

    if nivel == 1:
        root_node = lista[0].label()
        head_nodes[1]['ROOT'] = root_node                  #Head node of level 1 or ROOT node
        root_childs = list(lista[0])
        dicc[root_node] +=len(root_childs)            #if it is the first level add root-node to dicc (step-A)

        for element in root_childs:

            if isinstance(element,str):
                dicc[element]+=1                      #if actual node is a single-node add to dicc (step-B)

            if isinstance(element, Tree):
                node = element.label()
                dicc[node] +=1                        #if actual node is subtree add node to dicc (step-B) & then process.
                pendents.append(element)
                subtree = list(element)
                for i in range(len(subtree)):
                    subelement = element.label()
                    head_nodes[nivel+1][subelement] = root_node

    if nivel > 1:
        for subtree in lista:
            node = subtree.label()
            subtree_list = list(subtree)

            #Add actual-tree length to parents of past level head nodes
            if node in head_nodes[nivel].keys():          # if actual-node is child of a previous head-node
                child = node
                for level in range(nivel,1,-1):           # for every previous parent head node
                    parent = head_nodes[level][child]

                    dicc[parent] += len(subtree_list)     # add the length of actual-tree
                    child = parent

            # Check if there is not a new subtree inside the actual-tree
            for i in range(len(subtree_list)):
                subelement = subtree_list[i]

                if isinstance(subelement, Tree):
                    head_nodes[nivel+1][subelement.label()] = node #next level root nodes with childs (list elements)
                    pendents.append(subelement) # Add to pendents the element list for future sub-level processing

            dicc[node] += len(subtree_list)

            #Increment dicc in actual-node if elements are whatever (step-B)
            for element in subtree_list:
                if isinstance(element, str):
                    dicc[element] += 1
                else:
                    dicc[element.label()]+=1
    nivel += 1

    if len(pendents) > 0:
        get_dict_from_list(dicc,pendents, nivel, head_nodes)

    return dicc, head_nodes

def get_j_from_list(j,bi_grams):
    for i,tupla in enumerate(bi_grams):
        if j == tupla[1]:
            return tupla[0]

def sngrams(st, text,n=2):

    SYNT = [parse.tree() for parse in st.raw_parse(text)]
    SYNT1 = [list(parse.triples()) for parse in st.raw_parse(text)]

    #Generate syntactic bigram
    sbigram = []
    for triplet in SYNT1[0]:
        sbigram.append((triplet[0][0],triplet[2][0]))
    if n==2:
        return sbigram

    else:
        #Preprocessing the syntactic tree
        D = defaultdict(int)
        nivel = 1
        head_nodes=defaultdict(dict)
        sn_grams = []
        D, head_nodes = get_dict_from_list(D, SYNT, nivel,head_nodes)
        ROOT = head_nodes[1]['ROOT']
        list2 = list(sorted(zip(D.values(),D.keys())))
        list2.reverse()

        if len(head_nodes)+1 < n:
            print('There is not any possible sn-gram, n have to be lower than', len(head_nodes)+2)
        else:
            pendent_words = list2.copy()
            while (len(pendent_words) > 1):
                j = pendent_words.pop()[1]                        #From foot nodes to ROOT

                count = 0
                gram = defaultdict(list)

                while(len(gram[0]) < n):
                    gram[0].append(j)
                    x = get_j_from_list(j, sbigram)

                    if x== ROOT and len(gram[0]) < n:
                        gram[0].append(x)
                        break

                    j = x

                #Exception for repeated words in different levels
                #first: detect the same word in the last position of more than a bigram
                if len(gram[0]) > 1:
                    for i,_gram in enumerate(sbigram):
                        if _gram[1] == gram[0][0]:
                            count +=1

                #second: detect the bigram used in the last loop and delete it.
                if count > 1:
                    for i,_gram in enumerate(sbigram):
                        if _gram[1] == gram[0][0] and _gram[0] == gram[0][1]:
                            sbigram.pop(i)

                if len(gram[0]) == n:
                    sn_grams.append(gram[0])

                if count > 1:
                    pendent_words.append((1,gram[0][0]))

        return sn_grams

#TODO: optimization of this script making experimentation inside the Notebook of my NLP course "Synt..."

# Set of util functions for n-gram generation
def _make_ngrams(l, n):
    """Auxiliar ngrams generation func."""
    rez = [l[i:(-n + i + 1)] for i in range(n - 1)]
    rez.append(l[n - 1:])
    return zip(*rez)

def _ngram_split(text,n):
    ngram = ''
    gram_count = 0
    for i,word in enumerate(text.split(),1):
        if gram_count-n == -1 and i > n:
            ngram = ngram[ngram.find(' ')+1:]
        ngram += word+' '; gram_count+=1
        if gram_count == n:
            gram_count -= 1
            yield ngram

def _ngrams(text,n):
    ngrams = []
    ngrams.__iadd__(_ngram_split(text,n))
    return ngrams

def _chargrams(s,n):
    """Generate character n-grams."""
    return [s[i:i+n] for i in range(len(s)-n+1)]

def ngrams(text,n=2,gram_type='tokens',multioutput='raw_value'):
    """Generate the list of n-grams.

     Parameters
    ----------
    text: string to parse, generally a sentence.

    gram_type: Select the type of grams.
               string in ['chars', 'tokens']

    multioutput: Format type of the output.
                 string in ['raw_value', 'tuple_list']
                 * raw value - list of n-grams in string format. Eg: 'a b c'
                 * tuple list - list of n-grams in tuple format.
                 Eg: ('a','b','c')
    """
    if len(text.split()) >= n:
        if multioutput == 'raw_value':
            if gram_type == 'char':
                return _chargrams(text,n)
            else:
                return _ngrams(text,n)
        elif multioutput == 'tuple_list':
            if gram_type == 'char':
                return deque(_make_ngrams(text,n))
            else:
                return deque(_make_ngrams(text.split(),n))
    else:
        raise Exception("Not possible, n must be longer than total words.")

@Appender(nltk_skipgrams.__doc__)
def skipgrams(text,n,k, gram_type='tokens'):
    if gram_type == 'tokens':
        return nltk_skipgrams(text.split(),n,k)
    else:
        return nltk_skipgrams(text,n,k)