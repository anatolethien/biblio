from flask import Flask, render_template, request, redirect, session
from flask_security import Security, SQLAlchemyUserDatastore, \
    login_required, login_user, logout_user, current_user

from database import db_session, init_db
from models import User, Role

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SECRET_KEY'] = 'secr3t'

user_datastore = SQLAlchemyUserDatastore(db_session, User, Role)
security = Security(app, user_datastore)


@app.before_first_request
def create_user():
    init_db()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    match request.method:
        case 'GET':
            return render_template('register.html')
        case 'POST':
            username = request.form['username']
            password = request.form['password']
            user_datastore.create_user(username=username, password=password)
            db_session.commit()
            return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    match request.method:
        case 'GET':
            return render_template('login.html')
        case 'POST':
            username = request.form['username']
            password = request.form['password']
            user = user_datastore.get_user(username)
            if user and user_datastore.verify_password(password, user):
                login_user(user)
                return redirect('/')
            else:
                return redirect('/error')
            pass


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', current_user=current_user)


@app.route('/error')
def error():
    return render_template('error.html')