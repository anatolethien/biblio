from flask import Flask, request, session, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    match request.method:
        case 'GET':
            return render_template('register.html')
        case 'POST':
            db.session.add(User(username=request.form['username'], password=request.form['password']))
            db.session.commit()
            return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    match request.method:
        case 'GET':
            return render_template('login.html')
        case 'POST':
            pass

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)