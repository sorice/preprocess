Versión 2.x
- Implementaciones y pruebas para idioma español.
- Aún está sin revisar la parte de las expresiones regulares y los text normalization methods. Solo el textMode_Functions necesitó ser reelaborado.
- Revisar sí las funciones viejas donde se especificaba la codificación han sido cambiadas a Py3.

Version 2.0

* SRL, with multioutput for textsim
* review how to install practnlptools for python3, 64bit
* Syntactic Neural Dependency Parsing
* TensorFlow, Tehano, y otros deep learning

Versión 1.x

- Revisar los init y comprobar que no se cargan variables y funciones que no deben. Poner privadas todas las variables y funciones que deben estarlo.
- Put the normalization funcs in shallow module
- Set punctuation in shallow module
- Add spacy y los modelos model instead of Stanford or FreeLing models
- test all deep techniques using nltk-trainer package.
- test de performance usando pytest-benchmark
- Optimization of sngrams
- repeat performance test


Versión 1.0

- Notebook of POS[OK]
- Syntactic Dependency Parsing con Stanford[OK]
- Syntactic Tree Parsing con Stanford[OK]
- multioutputs for every tagger func[OK]
- NER con Stanford[OK]
- POS con Stanford[OK]
