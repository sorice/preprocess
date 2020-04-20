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

Using preprocess (Basic)
------------------------

.. code-block:: python

    import preprocess
    preprocess.basic.__all__

    ['lowercase',
     'replace_urls',
     'replace_symbols',
     'replace_dot_sequence',
     'multipart_words',
     'abbreviations',
     'expand_contractions',
     'replace_punctuation',
     'extraspace_for_endingpoints',
     'add_doc_ending_point',
     'del_tokens_len_one',
     'hyphenation']

Having a string as input all those functions are applicable.

.. Note:: Some examples are designed based on real text obtained from pdf to text transformers. 

.. code-block:: python

    string = "Free software is common in Europe... and UK it is not an exception"
    preprocess.lowercase(string)

    "free software is common in europe... and uk it is not an exception"

Replacing dot sequences. This function in particular, due to its uses in aligment, do not change the input string length in the output.

    * ``...`` it is not considered a sentece separator so it is whiten.
    * three dots sequences are priority or two dots followed by a white space

.. code-block:: python

    string = ". ... a.... b. .. . c.. .. d.. . e"
    preprocess.replace_dot_sequence(string)

    '    . a   . b     . c      d   . e'

Underscore sign are used as indestructible punctuation sign during preprocessing. The multi-part words are hyphenated words ([Read more about hyphen](https://en.wikipedia.org/wiki/Hyphen)) and are very important in compound-modifier constructions, this are morphological changes which modifies the meaning of another word.

.. code-block:: python

    string = "Hyphen multi-part words"
    preprocess.multipart_words(string)

    'Hyphen multi_part words

Another example of underscoring function in preprocess is ``hyphenation``, but its uses has been designed after having a list of tuples with collocations. Se more about ``collocations`` in `preprocess.grams.collocations <../_modules/preprocess/grams/collocations.html#Collocations>`_

.. code-block:: python

    collocations = [("natural", "language")]
    string = "In natural language processing multi-words are important"
    preprocess.hypenation(string, collocations)

    'In natural_language processing multi-words are important'

Combining Techniques
--------------------

This is a basic example of how to execute a designed order of basic preprocessing.

.. code-block:: python

    order = ['abbreviations', 'lowercase', 'replace_dot_sequence', 'multipart_words', 'replace_punctuation']
    string = "Free-software is common in Europe... and U.K. it is not an exception."
    preprocess.pipeline(string, flow=order)

    'free_software is common in europe and u_k_ is not an exception '

.. Note:: Not all the preprocess function in all modules can be concatenated.

Ngrams uses
-----------

.. code-block:: python

    string = 'free software is common in europe'
    preprocess.ngrams(string)                                                                                                                    

    ['free software ', 'software is ', 'is common ', 'common in ', 'in europe ']

.. code-block:: python

    preprocess.ngrams(string, n=3)

    ['free software is ',
     'software is common ',
     'is common in ',
     'common in europe ']

Using Shallow
-------------

.. code-block:: python

    string = 'free software is common in europe'
    preprocess.shallow.remove_stopwords(string)                                                                                                  

    ' free software common europe'

Deep example
-------------

.. code-block:: python

    string = 'free software is common in europe'
    preprocess.deep.syntdep(string)

    [('common', 'nsubj', 'software'),
     ('software', 'amod', 'free'),
     ('common', 'cop', 'is'),
     ('common', 'nmod', 'europe'),
     ('europe', 'case', 'in')]

Working with PDF
----------------

The variety of pdf generators made *"not standard"* pdf documents, so in the reverse process those resultant text come with rare chars, strange puntuation-signs sequences, page brakes, numbers inside the string sequences, line brakes which divide words syllables, etc.

``preprocess`` include *Creative Commons* books in PDF and text format to be preprocessed and to compare results with other libraries and platforms.

.. code-block:: python

    from preprocess.data import freesoftware_pdfpath
    pdf_path = freesoftware_pdfpath()
    text = preprocess.utils.io.pdftotxt(pdf_path)
    len(text)

    596767

Hopefully this examples gives you an idea of how to transform texts with preprocess library. The preprocessing stage is important to improve results as `Applying Preprocessing <applied-preprocessing.html>`_ tutorial shows. It is recommended that after this *quickstart* you read the `preprocess API <../api/index.html>`_ to learn complicated examples.

