from flask import Flask
import pandas as pd

df_authors = pd.read_csv('assets/authors.csv')
df_dataset = pd.read_csv('assets/dataset.csv')
df_authors = df_authors[~df_authors["author_name"].isna()]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/author/<int:author_id>")
def author_name(author_id):
    return df_authors.loc[author_id]["author_name"]


@app.route("/book/<int:book_id>")
def book_name(book_id):
    return df_dataset.iloc[book_id]["title"]


@app.route("/book/<int:book_id>/height")
def book_height(book_id):
    height = df_dataset.iloc[book_id]["dimension-z"]
    return f"{height}mm"


@app.route("/book/<int:book_id>/width")
def book_width(book_id):
    width = df_dataset.iloc[book_id]["dimension-x"]
    return f"{width}mm"


@app.route("/book/<int:book_id>/length")
def book_length(book_id):
    length = df_dataset.iloc[book_id]["dimension-y"]
    return f"{length}mm" 

@app.route("/book/<int:book_id>/author")
def book_author():
    

    if __name__ == "__main__" :
        app.run(debug=True, host='0.0.0.0')
