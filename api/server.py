from flask import Flask
import pandas as pd

df_authors = pd.read_csv('assets/authors.csv')
df_authors = df_authors[~df_authors["author_name"].isna()]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/author/<int:author_id>")
def author_name(author_id):
    return df_authors.loc[author_id]["author_name"]


if __name__ == "__main__" :
    app.run(debug=True, host='0.0.0.0')
