import os
import sys
import unittest
from unittest import TestCase
from unittest.mock import patch
import preprocess
from preprocess.basic.normalize import *
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

        #Deactivating track changes
        self.assertEqual(tURL,result,"Transforme URL must be underscored.")
 
