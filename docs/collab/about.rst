.. -*- mode: rst -*-

About
=====

``preprocess`` is a python3 package for text preprocessing. Is based on
NLTK, Stanford NLP models, and other less popular NLP python libraries.

``preprocess`` was a personal project of the author started in 2014 to 
facilitate his PhD experiments. Currently is just a library to simplify
his work and a developing project to optimize his investigation and work
text experiment pipelines.

Who is preprocess for?
-----------------------

  - data scientists, who want to test with python the impact of different preprocessing techniques in NLP tasks.
  - students, to start doing text preprocessing the easy way.

License
-------

``preprocess`` is an open source project and its 
`licence <https://github.com/sorice/blob/master/LICENSE>`_ is the 
BSD 3-Clause License. Please read the `original license text 
<https://opensource.org/licenses/BSD-3-Clause>`_ to know the
copyright posibilities.

Why text-preproc?
-----------------

In 2011 when I started to play with texts and python, NLP was the must 
popular library in python ecosystem. Stanford models were very well known
and I was starting on python programming.

My modern language is Spanish, and NLTK still have lot of no capabilities
for this language. The Belgium software _Pattern_ was very versitile for
languages like Spanish, but unfortunately the version for python3 never
was developed, my hunch is because the fast grows of python community made
more profitable the use of open source libraries abailable on github or 
other python organizations.

Another important reason for the developing of this library was my personal 
need to develop my own skills in python, and at the very end this was a way 
to return to the community something useful for early learners as a new
resource to push them to the same stages I went through.

Vectorization is a huge technique to improve big text datasets analysis, but for 
small collections and scholl projects the conversion of "a beatifull text"
to the sequence [1, 56, 12], which means the frecuency of every word in a 
certain dictionary, it is not so obvious. So one of my final purpouse was 
to maintain the input as a literal string human readable, to allow the 
practitioner to compare visually the similarities between two strings. I
was working from the beginning in text similarity problems so was a good 
reason from my point of view.

Even version 0.3 does not support spacy models or objects, because was one 
of my last discoveries. Spacy is very optimized with Cython, and has support
for Spanish, so I consider this will be the last goal to reach inside 
text-preproc compatibilities.

My intentions are to let the library very well documented for future students,
and to let everything very organized to be extended with new techniques or to
optimize current functions. Even today, I don't know if OOP philosophy could 
be better, but in case I (or someone else) answer that question I will do 
what is right.

Move forward and faster than me folk, this is for you.

Author
------

Abel Meneses-Abad
