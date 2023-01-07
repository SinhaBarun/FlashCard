from db import db

decks = db.Table('decks',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('word_id', db.Integer, db.ForeignKey('word.id'), primary_key=True)
)

