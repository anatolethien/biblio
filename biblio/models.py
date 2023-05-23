import json
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))

class Book(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    authors = db.Column(db.String(255))
    bestsellers_rank = db.Column(db.Integer())
    categories = db.Column(db.String(255))
    description = db.Column(db.String(255))
    length = db.Column(db.Float()) # dimension-x
    height = db.Column(db.Float()) # dimension-y
    width = db.Column(db.Float()) # dimension-z
    format = db.Column(db.Integer())
    image_url = db.Column(db.String(255))
    isbn10 = db.Column(db.String(255))
    isbn13 = db.Column(db.Integer())
    lang = db.Column(db.String(255))
    publication_date = db.Column(db.Date())
    rating_avg = db.Column(db.Float())
    rating_count = db.Column(db.Integer())
    title = db.Column(db.String(255))
    weight = db.Column(db.Float())

    def to_dict(self):
        with open('recommandations.json', 'r') as file:
            recommandations = json.load(file)
        return {
            'id': self.id,
            'description': self.description,
            'length': self.length,
            'height': self.height,
            'width': self.width,
            'image_url': self.image_url,
            'lang': self.lang,
            'rating_avg': self.rating_avg,
            'rating_count': self.rating_count,
            'title': self.title,
            'weight': self.weight,
            'recommandations': recommandations[str(self.id)]
        }

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.String(255))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
