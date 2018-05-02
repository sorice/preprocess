# Preprocess Library

A python package for preprocessing text using some NLP techniques:

* normalization techniques (Eg. url recognition, etc)
* punctuation patterns recognition
* symbol filtering and substitution
* shallow NLP techniques (Eg. Part of Speech Tagging)
* deep NLP techniques (Eg. Name Entity Recognition, etc)

# Requirements

__Linux__

java X is needed, but you need to check your downloaded Stanford model requirements to get the correct version.

(__current version__ for this example is _stanford-xxx-2015-04-20_)

```
$ apt install openjdk-8-jre
$ pip install nltk nose numpy
```



# Installation

```
$ pip install preprocess
```

# Usage

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

# Configuration

For a correct function of preprocess package, the supported NLP models must be configured correctly. Use the following steps to get it right:

1. get the stanford _coreNLP_ software on Internet: [Stanford CoreNLP software](https://stanfordnlp.github.io/CoreNLP/download.html)
   1. pick the language of your preference in stanford models repository: [Stanford CoreNLP models](http://nlp.stanford.edu/software/). (**current version** filename is stanford-parser-full-2015-04-20.zip)
2. get [Stanford Name Entity parser](http://nlp.stanford.edu/software/stanford-ner-2015-04-20.zip)
3. get [Stanford POSTagger parser](http://nlp.stanford.edu/software/stanford-postagger-full-2015-04-20.zip)
4. unzip the all the parsers
5. extract _Lexical models_ inside /path/to/stanford/jars/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar
   1. (__note__: the _Name Entity parser_ contains its models in _classifier_ folder, & the _POSTagger parser_ contains a set of models in the _models_ folder)

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

