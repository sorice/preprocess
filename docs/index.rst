.. -*- mode: rst -*-
.. preprocess documentation master file, created by
    sphinx-quickstart on Tue Apr 7 21:31:28 2020

Preprocess: Wrangling Text
==========================

**preprocess** is a python library for natural language tasks. The
principal reason for its implementation it is to avoid the still
current dispersion in python ecosystem for the next list of NLP
sub-process: stopword removal, hyphenation, POS tagging, general text
normalization tasks, etc. At the same time, even though current trend
it is to convert everything to *Pandas DataFrame*, this project start
when that trend wasn't alive and *Sklearn library* needed Bunch objects
and some of my colleague were using Weka (java) and arff format. So the
comparison of performances was a nightmare. This library integrates
methods to accomplish this purpose from NLTK, Spacy and others. 

QuickStart
-----------

1. :doc: `foo`

Future Goals
-------------

  - **Implement/Reuse** the open source better methods (performance
    speaking).
  - Implement some **techniques mentioned in scientific papers**, but 
    not available in popular python open source libraries.
  - At the end to make the preprocess **independent from NLTK**, and 
    less complex.
  - If after testing some Spacy or any other author have less heavy and
    better performance models **to exclude stanfordParser models**, 
    very heavy and java dependent.
  - **Create a mechanism to find better combination of preprocessing
    techniques** for some NLP tasks, reusing the ideas of *Sklearn 
    Pipeline* and *GreadSearch* parameter tuning technique. If 
    possible to combine with *Sklearn library* in some independent 
    module.

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   tutorial/user_guide_summary
   tutorial/user/applications
   foo

.. toctree::
   :maxdepth: 2
   :caption: Developers Guide

   tutorial/dev_guide_summary.rst
   tutorial/dev/deep.rst
   tutorial/dev/shallow.rst
   tutorial/dev/ngrams.rst

Util module
-----------

Helpers functions of preprocessing library.

.. automodule:: preprocess.utils
   :members:
