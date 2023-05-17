import unittest
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Preprocessing:
    """
    Text preprocessing.

    Parameters
    ----------
    path : str, default 'assets/books.csv'
        File path of the CSV table used as sample data.
    """

    def __init__(self, path: str = 'assets/books.csv'):
        self.books = pd.read_csv(
            filepath_or_buffer=path,
            usecols=['title', 'description']
        )
        self.corpus = self.books['title'] + ' ' + self.books['description']

    def normalize(self):
        """
        Normalizes the corpus by converting the text to lowercase, removing all
        digits, removing all symbols, removing all non-single whitespaces as
        well as leading and trailing whitespaces.

        Returns
        -------
        None
        """
        self.corpus = self.corpus.str.lower()
        self.corpus = self.corpus.str.replace(r'\d+', '', regex=True)
        self.corpus = self.corpus.str.replace(r'[^\w\s]+', '', regex=True)
        self.corpus = self.corpus.str.replace(
            r'\s{2,}', ' ', regex=True).str.strip()
    
    def tokenize(self):
        """
        Tokenizes the corpus by removing english stopwords and .

        Returns
        -------
        None
        """
        stop_words = set(stopwords.words('english'))
        self.corpus = self.corpus.apply(
            lambda ser: [word for word in word_tokenize(ser) if word not in stop_words]
        )


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


if __name__ == '__main__':
    unittest.main()