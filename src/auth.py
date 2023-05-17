from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'hello'

@app.route('/login')
def login():
    return 'login'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    match request.method:
        case 'GET':
            return render_template('signup.html')
        case 'POST':
            if User.query.filter_by(username=request.form['username']).first():
                db.session.add(User(
                    username=request.form['username'],
                    password=request.form['password']
                ))
                db.session.commit()
                return redirect(url_for('/'))
            else:
                return 'Username already in use.'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
