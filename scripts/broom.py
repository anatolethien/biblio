#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
import sqlite3

def books_broom():
    origin_path = 'downloads/dataset.csv'
    match sys.argv[1] if len(sys.argv) > 1 else 'csv':
        case 'csv':
            destination_path = 'assets/books.csv'
        case 'sql':
            destination_path = 'instance/database.sqlite'
    print(f'Reading the books dataset from {origin_path}...')
    df_books = pd.read_csv(
        filepath_or_buffer=origin_path,
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
    ).sample(10000)
    print('Treating data...')
    df_books = df_books.dropna()
    correct_langs = ['en']
    df_books = df_books.loc[df_books['lang'].isin(correct_langs)]
    df_books['bestsellers-rank'] = df_books['bestsellers-rank'].astype(np.int32)
    df_books['format'] = df_books['format'].astype(np.int32)
    correct_formats = [1,2,9,16,22]
    df_books = df_books.loc[df_books['format'].isin(correct_formats)]
    df_books['publication-date'] = pd.to_datetime(df_books['publication-date']).dt.date
    df_books['rating-count'] = df_books['rating-count'].astype(np.int32)
    df_books = df_books.dropna()
    print(f'Writing the books dataset to {destination_path}...')
    match sys.argv[1] if len(sys.argv) > 1 else 'csv':
        case 'csv':
            df_books.to_csv(
                path_or_buf=destination_path,
                index=False
            )
        case 'sql':
            df_books.set_index('id', inplace=True)
            con = sqlite3.connect(destination_path)
            df_books.to_sql(
                name='book',
                con=con,
                index=True
            )
            con.close()

def authors_broom():
    origin_path = 'downloads/authors.csv'
    destination_path = 'assets/authors.csv'
    print(f'Reading the authors dataset from {origin_path}...')
    df_authors = pd.read_csv(
        filepath_or_buffer=origin_path
    )
    print('Treating data...')
    df_authors = df_authors.rename(
        {
            'author_id': 'id',
            'author_name': 'name'
        }
    )
    print(f'Writing the books dataset to {destination_path}...')
    df_authors.to_csv(
        path_or_buf=destination_path,
        index=False
    )

def categories_broom():
    origin_path = 'downloads/categories.csv'
    destination_path = 'assets/categories.csv'
    print(f'Reading the categories dataset from {origin_path}...')
    df_categories = pd.read_csv(
        filepath_or_buffer=origin_path
    )
    print('Treating data...')
    df_categories = df_categories.rename(
        {
            'category_id': 'id',
            'category_name': 'name'
        }
    )
    print(f'Writing the categories dataset to {destination_path}...')
    df_categories.to_csv(
        path_or_buf=destination_path,
        index=False
    )

def formats_broom():
    origin_path = 'downloads/formats.csv'
    destination_path = 'assets/formats.csv'
    print(f'Reading the formats dataset from {origin_path}...')
    df_formats = pd.read_csv(
        filepath_or_buffer=origin_path
    )
    print('Treating data...')
    df_formats.rename(
        columns={
            'format_id': 'id',
            'format_name': 'name'
        },
        inplace=True
    )
    df_formats = df_formats.sort_values(
        by='id',
        ascending=True
    )
    print(f'Writing the formats dataset to {destination_path}...')
    df_formats.to_csv(
        path_or_buf=destination_path,
        index=False
    )

if __name__ == '__main__' :
    print('Broom!')
    books_broom()
    authors_broom()
    categories_broom()
    formats_broom()
    print('Done!')
