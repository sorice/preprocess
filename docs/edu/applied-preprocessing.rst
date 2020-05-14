.. _applications:

Applying Preprocess for Real
================================

This tutorial intends to show ``preprocess`` in a real context. After a 
quickstart in the library, and the bases of text normalization with 
python, the next obvious step is to apply preprocessing techniques in a 
real NLP problem

The selected problem is "Semantic Text Similarity".

Semantic Text Similarity
------------------------

SEMEVAl is an International Workshop on Semantic Evaluation, currently
part of Lexical and Computational Semantic and Semantic Evaluation
scientific conference. The objective of this workshop is to measure
the degree of semantic equivalence between two texts. The data is
composed by sentence pairs, coming from previously existing paraphrase
datasets [Agirre2012]. This event is divided in tasks, the task of 
interest is [Semantic Text Similarity](http://alt.qcri.org/semeval2012/task17/)

Usually in the gold standard the semantic equivalence is measured with
a float number between [0-5].

Dataset
-------

The data used for this example is a small part of SemEval 2012 Shared
[Task 6 Dataset](https://www.cs.york.ac.uk/semeval-2012/task6/index.php%3Fid=data.html), the en-en subset.

The subset is from MSR-Paraphrase, Microsoft Research Paraphrase Corpus
http://research.microsoft.com/en-us/downloads/607d14d9-20cd-47e3-85bc-a2f65cd28042/
750 pairs of sentences.

Machine Learning model
----------------------

[Some kind of Logistic Regression for binary classification.]

[Features, use textsim.calc_all](make a brief description here, and link with github.com/sorice/textsim)

Trainin Process
---------------

Train without preprocess

Train with preprocess

Cross Validation
----------------

[Show differences between scores obtained with/without preprocess]

Recommendations
---------------

* usually we must reduce dimensionality, for better interpretabillity
  of the model, less complexity, reduce the training time, avoid 
  overfitting and gain capacity of generalization 

* Feature selection process is not objective of this tutorial, but it
  is recommended that comparing the list of must important features,
  could show how preprocess is relevant for improving results, due to
  the straight relation between preprocess and selected features. 

Legal Note
----------

STS 2012 Dataset is under this licenses:
* http://research.microsoft.com/en-us/downloads/607d14d9-20cd-47e3-85bc-a2f65cd28042/
* http://research.microsoft.com/en-us/downloads/38cf15fd-b8df-477e-a4e4-a4680caa75af/

Preprocess Lib Application
------------------------------

``preprocess`` library has been used successfully as part of the
following projects:

- [Text Preprocessing Chapter of MyNLP Course Py3 version](file:///media/abelm/Almacen/Doctorado/Notas_de_la_Investigacion/03_Mi_Curso_Postgrado_Natural_Language_Process/02_Pre-Procesamiento_py3/)
- [Text Preprocessing Chapter of MyNLP Course Py2 version](file:///media/abelm/Almacen/Doctorado/Notas_de_la_Investigacion/03_Mi_Curso_Postgrado_Natural_Language_Process/02_Pre-Procesamiento)
- [Llanes-corpus similarity experiment active](file:///media/abelm/Almacen/Doctorado/01_Codigos/2016-02_Llanes_simCalcFlow/)
- [Next text-reuse experiment active](file:///media/abelm/Almacen/Doctorado/01_Codigos/2015-11-30_Llanes_similarity_Example_8_test_15/)
- [repository of my Text-Reuse algorithm](file:///media/abelm/Almacen/Doctorado/00_plag_algh/)

Older uses
----------

Older versions of this module. Be careful! Many of this URLs are the ancient versions with different software architectures.

- [QtNLP-Linguist module](https://github.com/sorice/QtNLP-Linguist)