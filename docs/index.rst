Documentation for the Code
**************************

.. toctree::
   :maxdepth: 2

useful #1 -- auto members
=========================

This is something I want to say that is not in the docstring.

.. automodule:: utils
   :members:

useful #2 -- auto members
=========================

This is something I want to say that is not in the docstring.

.. automodule:: deep
   :members:



Part III - Math formula example
-------------------------------------

.. math::

    y_k = \frac{x_0}{\sqrt{N}}+ \frac{1}{\sqrt{N}} \sum_{n=1}^{N-1} x_n \cos (\frac{\pi n(2k+1)}{2N}) \qquad 0 \leq k < N.
    
.. topic:: References:

    * C.D. Manning, P. Raghavan and H. Schütze (2008). Introduction to
      Information Retrieval. Cambridge University Press.
      http://nlp.stanford.edu/IR-book/html/htmledition/the-vector-space-model-for-scoring-1.html
      
.. math::

   \frac{c_{TF} + c_{FT}}{c_{TT} + c_{FT} + c_{TF}}

where :math:`c_{ij}` is the number of occurrences of
:math:`\mathtt{u[k]} = i` and :math:`\mathtt{v[k]} = j` for
:math:`k < n`.

.. math:: 

   \frac{\sum |u_i-v_i|}{\sum |u_i+v_i|}

Part IV - Inheriting docstring from external function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As you can see de :func:`interval_distance` inside :py:mod:`textsim` package does'n have any docstring, the result of sphinx-build is dynamically constructed from :func:`nltk.metrics.interval_distance` and other texts.

.. automodule:: shallow
   :members:

:See also:

    Read more in the **Sklearn User Guide** :mod:`metrics`.
    
:returns: D : array
        If sum_over_features is False shape is
        (n_samples_X * n_samples_Y, n_features) and D contains the
        componentwise L1 pairwise-distances (ie. absolute difference),
        else shape is (n_samples_X, n_samples_Y) and D contains
        the pairwise L1 distances.
        
.. note::

        **Y_norm_squared** and **X_norm_squared** are pre-computed dot-products of
        vectors in Y, and X respectively (E.g., ``(Y**2).sum(axis=1)``)

.. toctree::
    :maxdepth: 2
    :hidden:

    shallow
    deep
    tutorial/index
    user_guide
    glossary