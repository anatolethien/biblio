from flask import Flask
import pandas as pd

df = pd.read_csv('assets/authors.csv')

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/authors/<int:id>")
def author(id):
    return df.iloc(id)


if __name__ == "__main__" :
    app.run(debug=True, host='0.0.0.0')
