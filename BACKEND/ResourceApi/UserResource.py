from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, jwt_required, get_jwt

from Models.User import User
from Models.User import Scoreboard

_parser = reqparse.RequestParser()
    
_parser.add_argument('username',
    type=str,
    required=True,
    help="username cannot be empty !"
)

_parser.add_argument('password',
    type=str,
    required=True,
    help="this field cannot be empty!"
)

class UserResource(Resource):

    def post(self):
        
        data = _parser.parse_args()                

        if User.get_user(data['username']) :
            
            msg = {'message' : "user already exist"}
            return make_response(jsonify(msg), 409)

        try :
            
            username = data['username']
            password = data['password']
            
            user = User(username, password)
            user.save_user_to_db()

            score = Scoreboard(user.id)
            score.save_score_to_db()      
            
            msg = {'message' : 'User added successfully',
                    'user_id' : user.id,
                }
            return make_response(jsonify(msg), 201)

        except :
            
            msg = {'message' : 'An error occured while adding user'}
            return make_response(jsonify(msg), 500)

                
class UserLogin(Resource):

    @classmethod
    def post(cls):
        
        data = _parser.parse_args()

        user = User.get_user(data['username'])

        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.id)
            
            res = {
                "access_token" : access_token ,
                "username" : user.username
                }

            return make_response(jsonify(res), 200)

        msg = {"message" : "invalid credentials"}

        return make_response(jsonify(msg), 401)

class UserLogout(Resource):

    @jwt_required()
    def post(self):
        from app import ACCESS_EXPIRES, jwt_redis_blocklist
        jti = get_jwt()['jti']
        jwt_redis_blocklist.set(jti, "", ex=ACCESS_EXPIRES)
        
        res = {
            "message" : "user Logout successfully"
        }

        return make_response(jsonify(res), 200)
    


