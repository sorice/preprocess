Preprocess-Documentation
=========================

**preprocess** is a preprocessing language for natural language tasks
usually implements methods of normalization. This library collects
methods to accomplish this purpose from NLTK, spacy and others.

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   tutorial/user_guide_summary.rst
   tutorial/user/applications.rst

.. toctree::
   :maxdepth: 2
   :caption: Developers Guide

   tutorial/dev_guide_summary.rst
   tutorial/dev/deep.rst

.. toctree::
	:caption: Others
	:maxdepth: 1

    glossary
    about

Util module
-----------

Helpers functions of preprocessing library.

.. automodule:: preprocess.utils
   :members:


Testing some codes (delete later)
-------------------------------------

.. math::

    y_k = \frac{x_0}{\sqrt{N}}+ \frac{1}{\sqrt{N}} \sum_{n=1}^{N-1} x_n \cos (\frac{\pi n(2k+1)}{2N}) \qquad 0 \leq k < N.

.. math::

   \frac{c_{TF} + c_{FT}}{c_{TT} + c_{FT} + c_{TF}}

where :math:`c_{ij}` is the number of occurrences of
:math:`\mathtt{u[k]} = i` and :math:`\mathtt{v[k]} = j` for
:math:`k < n`.

.. math::

   \frac{\sum |u_i-v_i|}{\sum |u_i+v_i|}

sublevel 4 of markdown
^^^^^^^^^^^^^^^^^^^^^^

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
