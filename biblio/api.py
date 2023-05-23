from flask import Blueprint, jsonify, render_template
from flask_login import login_required, current_user
from .models import Book

api = Blueprint('api', __name__)

@api.route('/book/<int:id>')
def book(id: int):
    book = Book.query.get(id)
    if book:
        return jsonify(book.to_dict()), 200
    else:
        return jsonify({'error': 'Not Found'}), 404
