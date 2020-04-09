#### Versión 0.7 'Spanish support'

- Implementaciones y pruebas para idioma español.


#### Version 0.6 'Applying Deep Learning'

* EN-SRL, with multioutput for textsim
	* review how to install practnlptools for python3, 64bit
* Syntactic Neural Dependency Parsing
	* TensorFlow, sklearn y Spacy

#### Versión 0.5 'Spycy support'

- Add spacy y los modelos model instead of Stanford or FreeLing models
- test all deep techniques(stanford, spacy, nltk) using nltk-trainer package.
  - Pick the best tech as DEFAULT
* If the test result shows it is possible abandon nltk/standfordNLP and only use spacy and sklearn

#### Version 0.4.x 'Optimize'

Objective:

* test de performance usando pytest-benchmark (poner en la doc todos los tests results del v0.3)
	* Optimization of sngrams
* repeat performance test
* Pipeline version similar to sklearn
- add negation substitution
- add synonym replacement
- add spelling correction
* New version of collocations without nltk

#### Version 0.3.3

* Introduce OOP in all possible funcs in pack 'utils'
* introduce binary text writing in all functions
* preprocess('some_txt') -> return 'preprocessed_txt'
* preprocess.config must acept a dict to stablish the preprocess techniques active by default

#### Version 0.3.1

* Review the regular expressions for symbols.
* punctuation needs to be tested with human labeled data (books)
* for organization, readability and testing purpose make a subpack preprocess.normalization
* Review the mechanism of LANGUAGE in shallow.__init__ it is not being used

#### Version 0.3 'Packaging' (current)

* type checking and remove support for Py2
* add tox.ini, requirements.txt, .travis.yml, LICENSE, MANIFEST, .pypirc 
* doc v0.3 [OK 50%]
* test v0.3
* Finish decorator Appender to link docstring to doc
* separate aligning and helpers in utils.aling.py
* define if the hypenation functions must be in normalization
* doc ngrams.py + Basic docstring of sn_gram [OK]
* separated pack for ngrams, because sngrams is to long [OK]
* embedding notebook examples to the sphinx doc[OK]
* translate to English the notebooks involved

### Version 0.2.x 'Testing in Reality'</u>

- str input restriction management with only one decorator (if: isinstance(input,str) do, else: raise error)[NO, replaced by type checking en release 0.3] 
- Revisar los init y comprobar que no se cargan variables y funciones que no deben. 
- Poner privadas todas las variables y funciones que deben estarlo.
- Put the normalization funcs in shallow module[NO]
- Set punctuation in shallow module
- add collocations with nltk
- made some changes to regular expressions in normalize.py after PSTS experiments
- add first version of pdftotext
- test configurations for documentation with Sphinx
- ES support for Regular Expressions y los text normalization methods.
- Revisar sí las funciones viejas donde se especificaba la codificación han sido cambiadas a Py3.

### changelog 1.0 'preproc-tech'

- first version of pipeline
- lemmatization, stemming
- ngrams added, also stowords_ngrams, contextual_ngrams, and syntactic_ngrams (as sngrams)
- Notebook of POS
- Syntactic Dependency Parsing con Stanford
- Syntactic Tree Parsing con Stanford
- multioutputs for every tagger func
- NER con Stanford
- POS con Stanford[OK]
