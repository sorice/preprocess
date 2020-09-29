# preprocess.data.loaders
# Dataset loading utilities and primary API to the datasets module.
#
# Author:   Abel Meneses-Abad
# Created: Thu Apr 12 7:23:25 2020 -0400
#
# Copyright (C) 2020 BSD 3-Clause License
# For license information, see LICENSE.txt
#
# ID: loaders.py [] abelma1980@gmail.com $

"""
Dataset loading utilities and primary API to the datasets module.
"""

##########################################################################
## Imports
##########################################################################
import os

__all__ = [
    "load_freeculture",
    "load_culturalibre",
    "freeculture_pdfpath",
    "tnlp1_path",
    "tnlp1h_path",
    "test_text_path",
    "test_texth_path",
    ]

DATASETS = {
    "load_freeculture": "Free_Culture.txt",
    "load_culturalibre": "Cultura_Libre.txt",
    "freeculture_pdfpath": "Free_Culture.pdf",
    "tnlp1_path": "srctnlp1.txt",
    "tnlp1h_path": "srctnlp1_human.txt",
    "test_text_path": "test_text.txt",
    "test_texth_path": "test_text_human.txt",
    }

##########################################################################
## Specific loading utilities
##########################################################################

def _load_dataset(name, data_home=None, return_dataset=False):
    """
    Load a dataset by name and return specified format.
    """
    title = DATASETS[name]
    txt = os.path.join(os.path.dirname(__file__), 'books', title)
    with open(txt) as doc:
        data = doc.read()
    if return_dataset:
        return data
    return data

def load_freeculture():
    """Load the book Free Culture.
    """
    return _load_dataset('load_freeculture')

def load_culturalibre():
    """Load the book Cultura Libre.
    """
    return _load_dataset('load_culturalibre')

def freeculture_pdfpath():
    path = os.path.join(os.path.dirname(__file__), 'books', DATASETS['freeculture_pdfpath'])
    return path

def tnlp1_path():
    path = os.path.join(os.path.dirname(__file__), 'short', DATASETS['tnlp1_path'])
    return path

def tnlp1h_path():
    path = os.path.join(os.path.dirname(__file__), 'short', DATASETS['tnlp1h_path'])
    return path

def test_text_path():
    path = os.path.join(os.path.dirname(__file__), 'short', DATASETS['test_text_path'])
    return path

def test_texth_path():
    path = os.path.join(os.path.dirname(__file__), 'short', DATASETS['test_texth_path'])
    return path