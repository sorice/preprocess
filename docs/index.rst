.. -*- mode: rst -*-
.. preprocess documentation master file, created by
    sphinx-quickstart on Tue Apr 7 21:31:28 2020

Preprocess: Wrangling Text
==========================

``preprocess`` is a python library for natural language tasks. The
principal reason for its implementation it is to avoid the still
current dispersion in python ecosystem for the next list of NLP
sub-process: stopword removal, hyphenation, POS tagging, general text
normalization tasks, etc. At the same time, even though current trend
it is to convert everything to *Pandas DataFrame*, this project start
when that trend wasn't alive and *Sklearn library* needed Bunch objects
and some of my colleague were using Weka (java) and arff format. So the
comparison of performances was a nightmare. This library integrates
methods to accomplish this purpose from NLTK, Spacy and others.

Recommendded Learning Path
---------------------------

1. :doc:`edu/quickstart`.
2. Bases of `Text Normalization <edu/text-normalization.ipynb>`_.
3. `Applying Preprocess <edu/applied_preprocessing.ipynb>`_.
4. ``preprocess`` and ``NLTK`` entangles :doc:`edu/entangled-nltk`.
5. Playfull Programming `Filtering Important Words with Luhn <edu/filtering-words-with-Luhn.ipynb>`_.

Contributing
------------

Interested in contributing to ``preprocess``? ``preprocess`` is a 
welcoming, inclusive project and we would love to have you.
We follow the `Python Software Foundation Code of Conduct 
<http://www.python.org/psf/codeofconduct/>`_.

No matter your level of technical skill, you can be helpful. We 
appreciate bug reports, user testing, feature requests, bug fixes, 
product enhancements, and documentation improvements.

Check out the :doc:`collab/contributing` guide!

If you've signed up to do user testing, head over to the 
:doc:`collab/evaluation`.

Thank you for your contributions!


Concepts & API
--------------

Preprocessing Techniques
~~~~~~~~~~~~~~~~~~~~~~~~

Are wrangling techniques that convert an original text object in some
modified text suitable for NLP tasks. Usuarlly are not complicated to
understand but its diversity and combined forms make difficult to
apply or to program because are distributed in many libraries or not
public available in open source, only mentioned in scientific papers.

Basic Techniques
~~~~~~~~~~~~~~~~

- :doc:`api/basic/normalize`: contains usually called normalization techniques
- :doc:`api/basic/punctuation`: set of regular expressions for punctuation sign treatment
- :doc:`api/basic/hypen`: changes some sign conventions that modify words, specially to identify collocations
- :doc:`api/basic/symbols`: substitution of rare chars that represents symbols, frecuently appears in math texts

.. toctree::
  :maxdepth: 2
  :caption: Table of Contents

  collab/about
  edu/quickstart
  edu/text-normalization
  api/index
  collab/contributing
  collab/code_of_conduct
  collab/changelog
  edu/applied_preprocessing
  edu/entangled-nltk
  edu/filtering-words-with-Luhn

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