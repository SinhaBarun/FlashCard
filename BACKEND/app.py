from functools import cache
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta
import redis
from celery.schedules import crontab

from ResourceApi.UserResource import UserResource, UserLogin,UserLogout
from ResourceApi.WordResource import Word
from ResourceApi.WordResource import WordResource, Checkword, GetWord, GetReviewedWords
from ResourceApi.Scoreboard import ScoreboardResource, UpdateScore
from workers.celery_worker import make_celery



app = Flask(__name__)

api = Api(app)
jwt = JWTManager(app)

cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

ACCESS_EXPIRES = timedelta(hours=1)

app.secret_key = 'secretKey'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
cache_config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "RedisCache",  # Flask-Caching related configs
    "CACHE_REDIS_HOST" : "localhost",
    "CACHE_REDIS_PORT" : 6379,
    
} 

jwt_redis_blocklist = redis.StrictRedis(
    host="localhost", port=6379, db=0, decode_responses=True
)

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/1',
    
)

celery_app = make_celery(app)


@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token_in_redis = jwt_redis_blocklist.get(jti)
    return token_in_redis is not None


@app.before_first_request
def create_table():
    db.create_all()



api.add_resource(UserResource, '/user')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout') 
api.add_resource(GetWord, '/getword/<string:username>')
api.add_resource(ScoreboardResource, '/getscore/<string:username>')
api.add_resource(UpdateScore, '/updatescore/<string:username>/<string:word>/<int:n>')
api.add_resource(GetReviewedWords, '/getReviewedWords/<string:username>')




if __name__ == "__main__" :
    from db import db 
    from cache import cache

    db.init_app(app)
    cache.init_app(app, config=cache_config)

    app.run(debug=True)