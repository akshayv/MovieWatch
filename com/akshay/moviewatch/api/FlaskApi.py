import json
from simplejson import JSONEncoder
from com.akshay.moviewatch.business.dao.Dao import engine, Base
from com.akshay.moviewatch.business import Api
from com.akshay.moviewatch.business.utils import Mapper

__author__ = 'akshay'

from flask import Flask, request


class ObjectEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


app = Flask(__name__)


@app.route("/get/imdb")
def getIMDBSuggestions():
    session_id = request.args.get('session_id')
    user_id = request.args.get('user_id')
    if not Api.authenticate(user_id, session_id):
        raise Exception("Authentication failed")
    title = request.args.get('title')
    movies = Api.getIMDBSuggestionsForTitle(title)
    string = json.dumps([json.dumps(p, cls=ObjectEncoder) for p in movies])
    return string


@app.route("/get/registerMovie")
def registerMovie():
    session_id = request.args.get('session_id')
    user_id = request.args.get('user_id')
    if not Api.authenticate(user_id, session_id):
        raise Exception("Authentication failed")
    movie_id = request.args.get('movie_id')
    Api.registerMovie(movie_id, user_id)
    return json.dumps(json.dumps({'message': 'Done'}, cls=ObjectEncoder))


@app.route("/get/saveMovie")
def saveMovie():
    session_id = request.args.get('session_id')
    user_id = request.args.get('user_id')
    if not Api.authenticate(user_id, session_id):
        raise Exception("Authentication failed")
    movie_title = request.args.get('movie_title')
    movie_year = request.args.get('movie_year')
    movie_imdb_id = request.args.get('movie_imdb_id')
    Api.saveMovie(movie_title, movie_year, movie_imdb_id)
    return json.dumps(json.dumps({'sessionId': session_id}, cls=ObjectEncoder))


@app.route("/get/findAllForUser")
def getRegisteredMovies():
    session_id = request.args.get('session_id')
    user_id = request.args.get('user_id')
    if not Api.authenticate(user_id, session_id):
        raise Exception("Authentication failed")
    movies = Mapper.mapMovies(Api.getRegisteredMovies(user_id))
    return json.dumps([json.dumps(p, cls=ObjectEncoder) for p in movies])


@app.route("/get/registerUser")
def createUser():
    user_name = request.args.get('user_name')
    emailId = request.args.get('user_emailId')
    password = request.args.get('user_password')
    session_id = Api.createUser(user_name, password, emailId)
    print session_id
    if not session_id:
        raise Exception("Sorry, could not create user. User is already registered")
    return json.dumps(json.dumps({'sessionId': session_id}, cls=ObjectEncoder))



@app.route("/get/findForUser")
def getNonArchivedMoviesForUser():
    session_id = request.args.get('session_id')
    user_id = request.args.get('user_id')
    if not Api.authenticate(user_id, session_id):
        raise Exception("Authentication failed")
    movies = Mapper.mapMovies(Api.getNonArchivedMoviesForUser(user_id))
    return json.dumps([json.dumps(p, cls=ObjectEncoder) for p in movies])


@app.route("/get/archive")
def archiveMovieForUser():
    session_id = request.args.get('session_id')
    user_id = request.args.get('user_id')
    if not Api.authenticate(user_id, session_id):
        raise Exception("Authentication failed")
    movie_id = request.args.get('movie_id')
    Api.archiveMovieForUser(movie_id, user_id)
    return json.dumps(json.dumps({'message': 'Done'}, cls=ObjectEncoder))


@app.route("/login")
def login():
    userEmail = request.args.get('emailId')
    password = request.args.get('password')
    session_id = Api.login(userEmail, password)
    if not session_id:
        raise Exception("Authentication failed")
    return json.dumps(json.dumps({'sessionId': session_id}, cls=ObjectEncoder))


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run()