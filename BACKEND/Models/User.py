from db import db
from .ReviewedDecks import decks


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(20))

    score = db.relationship('Scoreboard', uselist=False, backref='user')

    reviewed_decks = db.relationship('Word', 
                    secondary=decks, 
                    lazy='subquery',
                    backref=db.backref('users', lazy=True))

    def __init__(self, username, password):
        
        self.username = username
        self.password = password

    def save_user_to_db(self):
        db.session.add(self)
        db.session.commit()     
                      
    
    @classmethod
    def get_user(cls,username):
        return cls.query.filter_by(username=username).first()
        
        
class Scoreboard(db.Model):
    __tablename__ = "scoreboard"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    correct = db.Column(db.Integer)
    incorrect  = db.Column(db.Integer)

    def __init__(self,user_id,correct=0,incorrect=0):
        self.user_id = user_id
        self.correct = correct
        self.incorrect = incorrect
    
    def save_score_to_db(self):
        db.session.add(self)
        db.session.commit()



    