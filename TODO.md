#### Versión 2.x 'Spanish support'

- Implementaciones y pruebas para idioma español.
- Aún está sin revisar la parte de las expresiones regulares y los text normalization methods. Solo el textMode_Functions necesitó ser reelaborado.
- Revisar sí las funciones viejas donde se especificaba la codificación han sido cambiadas a Py3.

#### Version 2.0 'Neural Network Intro'

* SRL, with multioutput for textsim
* review how to install practnlptools for python3, 64bit
* Syntactic Neural Dependency Parsing
* TensorFlow, Tehano, y otros deep learning

#### Version 1.3.x 'Optimize'

* Optimization of sngrams
* test de performance usando pytest-benchmark
* repeat performance test

#### Versión 1.2 'Spycy support'

- Add spacy y los modelos model instead of Stanford or FreeLing models
- test all deep techniques(stanford, spacy, nltk) using nltk-trainer package.
  - Pick the best tech as DEFAULT


### <u>Actual open development issues</u>

- str input restriction management with only one decorator (if: isinstance(input,str) do, else: raise error) 
- Revisar los init y comprobar que no se cargan variables y funciones que no deben. Poner privadas todas las variables y funciones que deben estarlo.
- Put the normalization funcs in shallow module
- Set punctuation in shallow module
- add negation substitution
- add synonym replacement
- add spelling correction


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