.. -*- mode: rst -*-

Preprocessing and API
=====================

This is the ``preprocess`` API documentation. This section covers some 
advanced definitions of NLP techniques, also which of them are 
*preprocessing techniques* and the complete currently available set of 
preprocessing techniques.

NLP techniques
--------------

Techniques grouping in this library is based in the proposal contained 
in [Chong2013]_. This cathegorization divide preprocessing techniques in
3 groups: basic, shallow and deep. In this work ngrams are not included
in the mentioned groups, but ngrams [Shannon1948]_ is a way to represent
texts very used joined to some preprocessing techniques E.g. stopword
ngrams and syntactic ngrams. Due to the variety of ngram combinations
techniques and the length of some of the codes to implement it, this
technique is included in a separated module called ``grams``.

Only two extra modules are included in ``preprocess``: data and utils.
The data contains all the congifuration data, the books used in the
examples and some small text to show how alignment works, and so on.
The utils module contains some helper functions to reduce the complexity
of the preprocessing pipeline: convert from pdf to text, align
preprocessed text with the original, etc.

The main objective of this library is to obtain the original text in a
suitable form for later NLP tasks like: Text Similarity, Text
Classification, Automatic translation, Text Retrieval, etc.

Modules
-------

.. toctree::
   :maxdepth: 2

   basic/index.rst
   grams/index
   shallow/index
   deep/index
   utils/index

References
----------

.. [Shannon1948] C.E. Shannon, A mathematical theory of communications,
	The Bell Systems Tech. J. 27 (1948), 379-423.

.. [Chong2013] Chong M. M. Y. A Study on Plagiarism Detection and
	Plagiarism Direction Identification Using Natural Language Processing
	Techniques, University of Wolverhampton, 2013, PhD Thesis, 326 pags.
