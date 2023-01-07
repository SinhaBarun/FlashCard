from db import db
from cache import cache

class Word(db.Model):
    __tablename__ = 'word'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    ans = db.Column(db.String(100), nullable=False)

    def __init__(self, word, ans):
        self.word = word
        self.ans = ans
    

    @classmethod
    @cache.cached(timeout=50)
    def get_all_word(cls):
        return cls.query.all()

    @classmethod
    def get_single_word(cls, word):
        return cls.query.filter_by(word=word).first()

    @classmethod
    def get_word_by_id(cls, _id):
        return cls.query.filter_by(id =_id).first()

    def save_word_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    
    
    
    