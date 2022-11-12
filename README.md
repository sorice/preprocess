# _Preprocess_ Library

Preprocess is a python package for preprocessing text using some NLP techniques:

* normalization techniques (Eg. url recognition, etc)
* punctuation patterns recognition
* symbol filtering and substitution
* shallow NLP techniques (Eg. Part of Speech Tagging)
* deep NLP techniques (Eg. Name Entity Recognition, etc)

The python ecosystem for text preprocessing is large and difficult to configure and use. When I started to use preprocessing for some more complex NLP task, the process to configure and generate standalone apps with non heavy dependencies was impossible using _nltk_ as a baseline. At the same time every normalization step taken from a different approach/library have a different input type and arguments. For that reason I decided to wrapped all those functions in a standard and unified library named preprocess, which works as follow:

```python
from preprocess import func
func('text')
'text_result'
```

This package integrates some text normalization techniques from some python packages likes: _nltk_, _normalizr_. Also contains many ideas extracted from other normalization or text preprocessing packages.

Some regular expressions used on shallow parsing are based on observations made from frequent errors in txt obtained from pdf conversion.

Additionally some functions intend to keep the original length of the text after normalization. E.gs. _'state-of-the-art'_ by _'state\_of\_the\_art'_; _'doing... some'_ by _'doing    some'_ (there are 4 whitespaces between _doing_ and _some_).  The objective was to wrangling the data (not munging it), not in all cases this objective was get it, some [alignment examples](https://github.com/sorice/2017paraphrasebsent/02.2-Jaccard-Align-Preproc-to-Original-Sent.ipynb) can be read.

# Requirements

__Linux__

java X is needed, but you need to check your downloaded Stanford model requirements to get the correct version.

(__current version__ for this example are _stanford-xxx-2015-04-20_ models)

```
$ apt install openjdk-8-jre pandoc
$ pip install nltk nose numpy
```

# Installation

```
$ pip install preprocess
```

# Generating the doc

Read carefully the section #doc in requirements.txt
This documentation render some notebooks to sphinx docs, so a not common
set of python libraries is used, and pandoc package is needed at OS 
level.

```
apt install pandoc
pip3 install 
```

# Basic Usage

```python
>>> import preprocess
>>> preprocess.lowercase('Stanford parser was created by Stanford University')
'stanford parser was created by stanford university'
```

Basic usage includes the following functions:

* lowercase, replace_urls, abbreviations, expand_contractions, ngrams
* replace_symbols: based on recognition of unicode & utf8 representations of Greek symbols, etc. 
* replace_punctuation: based on punctuation regular expressions
* multipart_words: or hyphenated expressions.
* some non-classical text manipulation operations such those made to easy parse the texts obtained from PDF:
  * extraspace_for_endingpoints: add an extra whitespace before the ending point of a sentence.
  * add_doc_ending_point: check if the last sentence of a doc ends with a dot, if not add it.
  * del_tokens_len_one: a primariy way to make stopword removal

Advanced usage includes the following functions:

* pos, ner, syntdp, sngrams, remove_stopword, contextual_ngrams, stopword_ngrams

# Advanced Usage 

### Configuration

For a correct function of preprocess package, the supported NLP models must be configured correctly. Use the following steps to get it right:

1. get the stanford _coreNLP_ software on Internet: [Stanford CoreNLP software](https://stanfordnlp.github.io/CoreNLP/download.html)
   1. pick the language of your preference in stanford models repository: [Stanford CoreNLP models](http://nlp.stanford.edu/software/). (**current tested version** filename is stanford-parser-full-2015-04-20.zip)

2. get [Stanford Name Entity parser](http://nlp.stanford.edu/software/stanford-ner-2015-04-20.zip)

3. get [Stanford POSTagger parser](http://nlp.stanford.edu/software/stanford-postagger-full-2015-04-20.zip)

4. unzip the all the parsers in your /path/to/stanford/jars/

5. extract _Lexical models_ inside /path/to/stanford/jars/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar

   __note__: the _Name Entity parser_ contains its models in _classifier_ folder, & the _POSTagger parser_ contains a set of models in the _models_ folder)

```
$ cd /path/to/stanford/jars/
$ ls -l
stanford-ner-2015-04-20
stanford-parser-full-2015-04-20
stanford-postagger-2015-04-20
```

```
$ cd stanford-parser-full-2015-04-20
$ ls -l
bin
conf
data
models <- your extracted models
...
```

### Usage

```python
>>> import preprocess
>>> preprocess.pos('What is the airspeed of an unladen swallow ?')
[('What', 'WP'),
 ('is', 'VBZ'),
 ('the', 'DT'),
 ('airspeed', 'NN'),
 ('of', 'IN'),
 ('an', 'DT'),
 ('unladen', 'JJ'),
 ('swallow', 'VB'),
 ('?', '.')]
```

# Future

The future changes of this library are based in the initial objectives:

1. A __pure python library__: at this version the Stanford models dependency, developed in java,  made this milestone impossible.

    - The future: replace with spacy, or pntl or any other self deep learning tagging implementation with a free and professional collection of texts.

2. __Optimization__ to get better times in processing big collections of data: many functions are in pure python:

    - The future: implement pure python funcs in cython or rust.

3. __Standard Input__: many libraries, ideas or codes reused in this library have different ways to get the inputs (numerical vectors, strings, set of words, etc), the objective is to pass a simple string or a well known _ObjectType_ like _TfIdfModel_.

    - The future: check if the input is a string distance and with a decorator change all kind of object type to string.

4. __Low-weight__: to have the less possible dependencies for academical or commercial use deployment, and the least possible complexity.

    - The future: avoid the nltk dependency or any other, reusing the necessary code and fixing them to integrate them on _preprocess architecture_.

5. __Integration__: add every preprocessing technique mentioned in the papers of SEMEVAL or CLEF to solve _Reused Text Detection_ or _Semantic Text Similiarity_, and other fundamental papers in this area.

    - __Citation__: add a complete set of cites about all techniques, and link them with its correspondent function on the library.

