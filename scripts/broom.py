#!/usr/bin/env env/Scripts/python

import pandas as pd

print('Broom!')

df_authors = pd.read_csv('assets/authors.csv')
df_categories = pd.read_csv('assets/categories.csv')
df_dataset = pd.read_csv('assets/dataset.csv')

def author_magic_parser(row):
    author_info = []
    list = eval(row)
    for author_id in list:
        if author_id in df_authors.index:
            author_info.append((author_id, ))

    return author_info

df_dataset = df_dataset[df_dataset["bestsellers-rank"].notna()]


