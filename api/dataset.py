import pandas as pd
import csv

df = pd.read_csv("biblio/assets/dataset.csv")
dc = df.columns
books = df[['title','description','categories','authors','dimension-x','dimension-y','dimension-z','format','rating-avg','rating-count','id','weight','lang']]
lang = books['lang'].value_counts()
lang.to_csv('lang.csv')
print(lang)

