.. currentmodule:: preprocess

.. _basic-module:

Basic Module
============

Module for basic preprocessing techniques: lowercase, urls replacement
symbols replacement, multipart words underscoring, etc.

Some extra techniques very useful the testing of ``preprocess`` library in
real scenarios are included in this module as functions: ``replace_point_secuence``,
``add_doc_end_point``.

Quick Example
-------------

The original text (first six lines):

.. code-block:: bash

    For other (optional) flags of <opencv_createsamples>, see the official... documentation
    at http://Docs.opencv.org/doc/user_guide/ug_traincascade.html.
    [ 99 ]
    www.it-ebooks.info.
    Generating Haar Cascades for Custom 8.4 Targets

.. code-block:: python

    from preprocess.basic import replace_urls, multipart_words
    from preprocess.data import test_text_path

    path = test_text_path()

    with open(path) as doc:
        text = doc.read()

    resultant_text = replace_urls(multipart_words(text))
    print("\n".join(resultant_text.split('\n')[:10]))

The output must look like this:

.. code-block:: bash

    For other (optional) flags of <opencv_createsamples>, see the official... documentation
    at http___Docs_opencv_org_doc_user_guide_ug_traincascade_html.
    [ 99 ]
    www_it_ebooks_info.
    Generating Haar Cascades for Custom 8_4 Targets

Detailed Docs
-------------

1. :doc:`normalize`: normalization functions.

API Reference
-------------

.. automodule:: preprocess.basic
   :members:

.. toctree::
   :maxdepth: 2

   normalize
