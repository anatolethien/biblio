import unittest
import pandas as pd

from biblio.preprocessing import Preprocessing

class TestPreprocessing(unittest.TestCase):

    def setUp(self):
        self.preprocessing = Preprocessing()

    def test_init(self):
        self.assertIsInstance(self.preprocessing.corpus, pd.Series)

    def test_normalize(self):
        self.preprocessing.normalize()
        self.assertIsInstance(self.preprocessing.corpus, pd.Series)
        self.assertGreater(any(self.preprocessing.corpus.str.len()), 0)
        self.assertFalse(any(self.preprocessing.corpus.str.contains(r'\d')))
        self.assertFalse(any(self.preprocessing.corpus.str.contains(r'[^\w\s]+')))
        self.assertFalse(any(self.preprocessing.corpus.str.contains(r'\s{2,}')))
    
    def test_tokenize(self):
        self.preprocessing.normalize()
        self.preprocessing.tokenize()
