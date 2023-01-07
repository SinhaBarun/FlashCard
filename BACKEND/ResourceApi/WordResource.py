import random
from time import perf_counter_ns
from tracemalloc import start
from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import jwt_required

from db import db
from Models.Word import Word
from Models.User import User

_parser = reqparse.RequestParser()

_parser.add_argument('word',
    type = str,
    required = True,
    help = "This Field cannot be empty !"
    )

_parser.add_argument('ans',
    type = str,
    required = True,
    help = "this field cannot be empty !"
    )  



class WordResource(Resource):

    def post(self):
        data = _parser.parse_args()
        
        inp_word = data['word'].strip().capitalize()
        inp_ans = data['ans'].strip()

        if Word.get_single_word(inp_word):
            return {'message' : 'word already exist'}, 401
        
        try :
            word = Word(inp_word, inp_ans)
            word.save_word_to_db()
        except:
            return {'message' : 'Error occured while adding word'}, 500

        return {'message' : 'word added successfully',
                'word' : inp_word,
                'ans' : inp_ans
                }, 201

class Checkword(Resource):
    
    @jwt_required()
    def post(self):

        data = _parser.parse_args()
        word = data['word'].strip().capitalize()
        ans = data ['ans'].strip()
        get_word = Word.get_single_word(word)

        if get_word and safe_str_cmp(get_word.ans, ans):

            db.session.commit()

            msg = {'message' : "correct"}
            return make_response(jsonify(msg), 200)
        
        msg = {'message' : "Incorrect"}
        return make_response(jsonify(msg), 401)

class GetWord(Resource):

    # parser = reqparse.RequestParser()
    # parser.add_argument('username', type=str, required = True)

    @jwt_required()
    def get(self,username):
    
        user = User.get_user(username)
        
        
        reviewed_deck = [i.id for i in user.reviewed_decks]
        reviewed_words = [[Word.get_word_by_id(i).word, Word.get_word_by_id(i).ans] for i in reviewed_deck]
        start = perf_counter_ns()
        all_words = [i.id for i in Word.get_all_word()]
        end = perf_counter_ns()
        print("time taken", end - start)
        not_reviewed_decks = [i for i in all_words if i not in reviewed_deck] 

        if len(not_reviewed_decks) > 0:  
            n = random.randint(2,5)
            res_word = Word.get_word_by_id(not_reviewed_decks[0]).word
            res_ans = Word.get_word_by_id(not_reviewed_decks[0]).ans
            options = [
                Word.get_word_by_id(not_reviewed_decks[n+1]).ans,
                Word.get_word_by_id(not_reviewed_decks[n]).ans,
                Word.get_word_by_id(not_reviewed_decks[n-1]).ans,
                Word.get_word_by_id(not_reviewed_decks[n+2]).ans
            ] 
            res = {
                "res_word" : res_word,
                "res_ans" : res_ans,
                "options" : options,
                "reviewedWords" : reviewed_words
                }

            return make_response(jsonify(res),200)
        else : 

            res = {
                "message" : "No more words"
            }

            return make_response(jsonify(res), 200)

class GetReviewedWords(Resource):

    @jwt_required()
    def get(self,username):
        user = User.get_user(username)

        reviewed_word_id = [i.id for i in user.reviewed_decks]
        reviewed_words = [[Word.get_word_by_id(i).word, Word.get_word_by_id(i).ans] for i in reviewed_word_id]

        if len(reviewed_word_id) > 0 :
            res = {
                "reviewedWords" : reviewed_words 
            }

            return make_response(jsonify(res), 200)







    
