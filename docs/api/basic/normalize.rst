.. currentmodule:: preprocess

.. _normalize-module:

Normalize Module
================

This module gather the must popular and basic techniques for text
preprocessing.

Replace URLs
------------

``replace_urls``

This function underscore all the punctuation marks that appear in a url
Eg. *www.google.com* is transformed into *www_google_com*

Replace Symbols
---------------

``replace_symbols``

This function was implemented to replace the Greek letters, and other
mathematical symbols, but its implementation was made for python2 and
utf8 code, due to the python2 deprecation this function must be
rewritten.

Replace Dot Sequence
--------------------

``replace_dot_sequence``

This function was created to replace the *three dots* punctuation sign.
Usually other sequences of dots appears in real text coming from pdf.
Eg. some entries in the content index are separated by long sequences
of dots, three dots at the end of a sentence could turn into four dots.

The algorithm implemented prioritize this sequence:
* dot [0 OR 1]\s [1 OR N]dot N[\s OR dot]
all the sequences detected are changed by white spaces. Without change
the length of the string.

This function is used also in aligning functions, in which is important
to keep the same quantity of chars.

Multipart Words
----------------

``multipart_word``

Considered as new words, frequently two or more words appear together
united by hyphens. Eg. common-sense, proprietary-software, etc. These
hyphenated words are considered a new single word, named 
*multipart-word*, and could be significant for some NLP problems.

The algorithm implemented here, take in consideration three different
marks as hyphens to be replaced by underscore sign:

* ``-`` or ``hyphen``: CD-ROM -> CD_ROM
* ``.`` or ``dot``: pandas.DataFrame -> pandas_DataFrame
* ``@`` or ``at``: example@gmail.com -> example_gmail_com
