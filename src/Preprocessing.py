import unittest
import pandas as pd
from nltk.corpus import stopwords


class Preprocessing:

    def __init__(
        self,
        path: str = 'assets/books.csv',
        cols: list = [
            'title',
            'description']):
        self.books = pd.read_csv(
            filepath_or_buffer=path,
            usecols=cols
        )
        self.corpus = self.books['title'] + ' ' + self.books['description']

    def normalize(self):
        """
        Normalizes the corpus by converting the text to lowercase, removing all
        digits, removing all symbols, removing all non-single whitespaces as
        well as leading and trailing whitespaces.
        """
        self.corpus = self.corpus.str.lower()
        self.corpus = self.corpus.str.replace(r'\d+', '', regex=True)
        self.corpus = self.corpus.str.replace(r'[^\w\s]+', '', regex=True)
        self.corpus = self.corpus.str.replace(
            r'\s{2,}', ' ', regex=True).str.strip()


class TestPreprocessing(unittest.TestCase):

    def setUp(self):
        self.preprocessing = Preprocessing()

    def test_init(self):
        self.assertIsInstance(self.preprocessing.corpus, pd.Series)

    def test_normalize(self):
        self.preprocessing.normalize()
        self.assertIsInstance(self.preprocessing.corpus, pd.Series)
        self.assertFalse(any(self.preprocessing.corpus.str.contains(r'\d')))
        self.assertFalse(any(self.preprocessing.corpus.str.contains('[^\w\s]+')))
        self.assertFalse(any(self.preprocessing.corpus.str.contains(r'\s{2,}')))


if __name__ == '__main__':
    unittest.main()
