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
  - Pick the best tech as DEFAULT -> Default and Supported are only python packages 
  -> a close deprecation of StanfordDependencyParser made this objective to move to v0.3.1
  
* If the test result shows it is possible abandon nltk/standfordNLP and only use spacy and sklearn
* implement a method to include regular expression passed by the user (like spacy)
* implement self function of nltk.measures to pass to grams.CollocationList
* Implement new machine learning abbreviation_recognition based in notes inside basic/abbreviation.py
	-> put abbreviation_expan in basic/abbreviation.py
	-> put acronym_normalization in basic/abbreviation.py

#### Version 0.4.x 'Optimize'

Objective:

* test de performance usando pytest-benchmark (poner en la doc todos los tests results del v0.3)
	- Optimization of sngrams
	- Add those tests to the preprocess doc
* repeat performance test
* Pipeline version similar to sklearn
- add negation substitution
- add synonym replacement
- add spelling correction
* New version of collocations without nltk
* Completly in OOP if that has sense after 0.3.3
* Add main section Advanced Examples (include POS.ipynb)

#### Version 0.3.3

* Introduce OOP in all possible funcs in pack 'utils'
* introduce binary text writing in all functions
* preprocess('some_txt') -> return 'preprocessed_txt'
	-> with the default techniques selection
* preprocess.config must acept a dict to stablish the preprocess techniques active by default
* build __all__ for deep, shallow, basic
* build __pendent__ for deep, shallow, basic
* create preprocess.config 
	- hyphenation can't be used in pipelines because of collocations parameter so if None
		collocations = preprocess.config.collocations a default value
* replace_symbols is made for encoding utf8 this regular expressions must change to default encoding of python3

#### Version 0.3.1

* Review the regular expressions for symbols.
* punctuation needs to be tested with human labeled data (books)
* for organization, readability and testing purpose make a subpack preprocess.normalization
* Review the mechanism of LANGUAGE in shallow.__init__ it is not being used
* add shallow.sentence_segmentation
* add shallow.number_replacement
* increment dataset loading docstring
* prepare the semantic text similarity in applied_preprocessing.rst
* introduce abbreviation list from freeling as a cfg data.[NO]
	-> introduced in 0.3.0 as a free abb dict from Wikipedia
	-> 
* [High Priority] an NLTK warning during testing about deprecation of StanfordDependencyParser
	-> the warning recommend to use CoreNLPDependencyParser but this class needs to run a java server
	this is not util for preprocess objectives (simplicity, and later not java dependencies)
	-> so: preprocess.deep must be changed to spacy
* delete this function extraspace_for_endingpoints or change RE, if it is to much for replace_punctuation

#### Version 0.3 'Packaging' (current)

* type checking and remove support for Py2[OK, 30%]
* add tox.ini, requirements.txt, .travis.yml, LICENSE, MANIFEST, .pypirc 
* doc v0.3 [OK 50%]
	- changing doc to API style of yellowbrick[OK]
	- include data for examples[OK]
	- include datasets rst
* test v0.3[OK, 1%]
* separate aligning and helpers in utils.aling.py [OK]
* doc ngrams.py + Basic docstring of sn_gram [OK]
* separated pack for ngrams, because sngrams is to long [OK]
* embedding notebook examples to the sphinx doc [OK]
* translate to English the notebooks involved.
* include the test data from NLP course for Text Normalization Jupyter ntb[OK]
	- revisar los paths a esas datas en el notebook 
* Included a playfull and advanced example using Luhn law to filter important words[OK]
	- translate to English
* define if the hypenation functions must be in normalization [OK]
* Write the Quickstart [OK]
* Finish @Appender to link docstrings to .py with close to 200 LOC

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
