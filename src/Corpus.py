import unittest
import pandas as pd


class Corpus:

    def __init__(self, path='assets/books.csv', cols=['title', 'description']):
        self.books = pd.read_csv(
            filepath_or_buffer=path,
            usecols=cols
        ).astype(str)
        self.corpus = self.books.title + ' ' + self.books.description

    def normalize(self):
        return self.corpus.lower()


class TestCorpus(unittest.TestCase):

    def test_setup(self):
        self.corpus = Corpus()

    def test_init(self):
        self.assertIsInstance(self.corpus.books, pd.DataFrame)
        self.assertIsInstance(self.corpus.corpus, pd.Series)
        self.assertEqual(len(self.corpus.books), len(self.corpus.corpus))

    def test_corpus_values(self):
        for index, row in self.corpus.books.iterrows():
            title = row['title']
            description = row['description']
            combined = title + ' ' + description
            self.assertEqual(self.corpus.corpus[index], combined)


if __name__ == '__main__':
    unittest.main()
