from dash import Dash, dash_table
import pandas as pd

def ckoi(obj):
    print(type(obj))


categories = pd.read_csv('assets/categories.csv')
authors = pd.read_csv('assets/authors.csv')
dataset = pd.read_csv('assets/dataset.csv')

app = Dash(__name__)
# app.layout = dash_table.DataTable(authors.to_dict('records'), [{'id': i, 'name': i} for i in authors.columns])
app.layout = dash_table.DataTable(categories.to_dict('records'), [{'id': i, 'name': i} for i in categories.columns])
# app.layout = dash_table.DataTable(dataset.to_dict('records'), [{'id': i, 'name': i} for i in dataset.columns])

if __name__ == '__main__':
    app.run_server(debug=True)