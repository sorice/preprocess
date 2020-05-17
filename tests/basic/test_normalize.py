import os
import sys
import unittest
from unittest import TestCase
from unittest.mock import patch
import preprocess
from preprocess.basic.normalize import *
from preprocess.basic.abbreviation import *
from preprocess.data import test_text_path
from .data import *

class TestNormalize(unittest.TestCase):
    """Testing class for normalization techniques.
    """

    def setUp(self):
        self.dataPath = test_text_path()

    def test_replace_urls(self):
        """Test replacing urls punctuation signs by underscore.
        """
        #Init data
        text = URL
        #Applying the function to test
        result = replace_urls(text)
        self.assertEqual(tURL,result,"Transformed URL must be underscored.")

    def test_replace_dot_sequence(self):
        """Test for replacing dots sequences with white spaces.
        """
        #Init data
        text = DOT_SEQUENCE
        #Applying the function to test
        result = replace_dot_sequence(text)
        self.assertEqual(rDOT_SEQUENCE,result,"Dot sequences must be replaced by white spaces.")
        
    def test_multipart_words(self):
        """Test for replacing hyphens with underscore in multi-part-words.
        """
        #Init data
        text = MULTIPART_WORDS
        #Applying the function to test
        result = multipart_words(text)
        self.assertEqual(rMWORDS,result,"Transformed URL must be underscored.")

    def test_expand_abbrevs(self):
        """Test expand abbreviations on English language, the classical
        abbreviations.
        """
        #Init data
        text = ABBR
        #Applying the function to test
        result = expand_abbrevs(text, lang='en')
        self.assertEqual(eABBR,result,"Classic abbreviations must be expanded")

    def test_normalize_abbrev(self):
        """Test for normalizing abbreviations with underscore sign.
        """
        #Init data
        text = ACRONYM
        #Applying the function to test
        result = normalize_abbrevs(text)
        self.assertEqual(rACRONYM,result,"Abbreviations must be underscored")

    def test_expand_contractions(self):
        """Test the expansion of contractions
        """
        #Init data
        text = CONTRACTIONS
        #Applying the function to test
        result = expand_contractions(text)
        self.assertEqual(eCONTRACTIONS,result,"Abbreviations must be underscored")