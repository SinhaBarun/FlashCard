from flask_restful import Resource
from flask import jsonify, make_response

from Models.User import User
from Models.Word import Word
from db import db

class ScoreboardResource(Resource):

    def get(self,username):
        
        user = User.get_user(username)

        correct = user.score.correct
        incorrect = user.score.incorrect

        res = {"correct" : correct,
                "incorrect" : incorrect}
        
        return make_response(jsonify(res), 200)
    
class UpdateScore(Resource):

    def post(self,username,word,n):

        user = User.get_user(username)
        get_word = Word.get_single_word(word)
        user.reviewed_decks.append(get_word)

        if n :
            user.score.correct = user.score.correct + 1
            db.session.commit()

            res = {"correct" : user.score.correct,
                    "incorrect" : user.score.incorrect}
            
            return make_response(jsonify(res), 200)

        else :
            user.score.incorrect = user.score.incorrect + 1
            db.session.commit()

            res = {"correct" : user.score.correct,
                    "incorrect" : user.score.incorrect}
            
            return make_response(jsonify(res), 200)
        
