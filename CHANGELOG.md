#### Version 0.3 'Packaging' (current)

* type checking and remove support for Py2[OK, 30%]
* add tox.ini, requirements.txt, .travis.yml, LICENSE, MANIFEST, .pypirc 
* doc v0.3 [OK 50%]
	- changing doc to API style of yellowbrick[OK]
	- include data for examples[OK]
	- include datasets rst
* test v0.3[OK, 20%]
* separate aligning and helpers in utils.aling.py [OK]
* doc ngrams.py + Basic docstring of sn_gram [OK]
* separated pack for ngrams, because sngrams is to long [OK]
* embedding notebook examples to the sphinx doc [OK]
* translate to English the notebooks involved.[OK,66%]
* include the test data from NLP course for Text Normalization Jupyter ntb[OK]
	- review the paths to those datas in all the involved notebooks[OK]
    - include a summary description of the books and their copyright in docs/api/data/ <- run ipyn
* Included a playfull and advanced example using Luhn law to filter important words[OK]
	- translate to English[OK]
* define if the hypenation functions must be in normalization [OK]
* Write the Quickstart [OK]
* feat: delete digit words[OK]
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
