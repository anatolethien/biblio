from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user
from .models import Book

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/book/<int:id>')
def book(id: int):
    book = Book.query.get(id)
    if book:
        return render_template('book.html', book=book.to_dict())
    else:
        return redirect('/error')

@main.route('/error')
def error():
    return render_template('error.html')
