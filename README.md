# Preprocess Library

A python package for preprocessing text using some NLP techniques:

* normalization techniques (Eg. url recognition, etc)
* punctuation patterns recognition
* symbol filtering and substitution
* shallow NLP techniques (Eg. Part of Speech Tagging)
* deep NLP techniques (Eg. Name Entity Recognition, etc)

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

For a correct function of preprocess package, the supported NLP models must be configured correctly

```
cd 
```

