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
    "load_freesoftware",
    "load_culturalibre",
    "freesoftware_pdfpath",
    ]

DATASETS = {
    "load_freesoftware": "FS_FSociety.txt",
    "load_culturalibre": "Cultura_Libre.txt",
    "freesoftware_pdfpath": "FS_FSociety.pdf",
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

def load_freesoftware():
    """Load the book Free Software Free Society.
    """
    return _load_dataset('load_freesoftware')

def load_culturalibre():
    """Load the book Cultura Libre.
    """
    return _load_dataset('load_culturalibre')

def freesoftware_pdfpath():
    path = os.path.join(os.path.dirname(__file__), 'books', DATASETS['freesoftware_pdfpath'])
    return path
