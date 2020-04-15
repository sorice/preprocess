.. -*- mode: rst -*-

Quick Start
============

If preprocess is new for you, this guide will help you to run your first
examples:

:mod:`preprocess` use some external library models, before _v0.5_ depends
on NLTK and StanfordParser, which in turns depends on java. Java 
dependences must be `installed by hand <https://github.com/nltk/nltk/wiki/Installing-Third-Party-Software>`_
and the models must be collocated in the right place before starting the 
below installation.

NLP pretrained models are usually heavy, so :mod:`preprocess` do not 
include on it.

Config the enviroment
-----------------------

1. Pretrained model downloading
	- download `StanfordParser Syntactic Parser models <https://nlp.stanford.edu/software/lex-parser.html#Download>`_
	- download `StanfordParser POS Tagger models <https://nlp.stanford.edu/software/tagger.html#Download>`_
	- download `StanfordParser NER models <https://nlp.stanford.edu/software/CRF-NER.html#Download>`_
2. Extract models in /opt/stanford/

.. NOTE:: By default *preprocess/data/cfg/stanford.cfg* is configured on the direction */opt/stanford*.

Installation
------------

:mod:`preprocess` is a Python 3 package and works well with 3.4 or later.

.. code-block:: bash

    $ pip install preprocess
    

