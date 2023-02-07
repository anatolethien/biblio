#!/usr/bin/env env/Scripts/python

import pandas as pd
import numpy as np

print('Broom!')

df_books = pd.read_csv(
    filepath_or_buffer='assets/dataset.csv',
    usecols=[
        'authors',
        'bestsellers-rank',
        'categories',
        'description',
        'dimension-x',
        'dimension-y',
        'dimension-z',
        'format',
        'id',
        'image-url',
        'isbn10',
        'isbn13',
        'lang',
        'publication-date',
        'rating-avg',
        'rating-count',
        'title',
        'weight'
    ]
)

df_books = df_books.dropna()
df_books = df_books.loc[df_books['lang'] == 'en']
df_books['bestsellers-rank'] = df_books['bestsellers-rank'].astype(np.int32)
df_books['format'] = df_books['format'].astype(np.int32)
df_books = df_books.loc[df_books['format'].isin([1,2,9,16,22])]
df_books['publication-date'] = pd.to_datetime(df_books['publication-date']).dt.date
df_books['rating-count'] = df_books['rating-count'].astype(np.int32)

print(df_books.info(memory_usage='deep'))

df_books.sample(5000).to_csv('assets/books.csv', index=False)
# df_books.to_csv('assets/books.csv', index=False),
