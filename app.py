from flask import Flask, request, session, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    from user import User
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        db.session.add(User(username=request.form['username'], password=request.form['password']))
        db.session.commit()
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    from user import User
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        pass

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
