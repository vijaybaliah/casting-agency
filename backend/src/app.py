from flask import jsonify, abort, request
from src.database.models import Actors, Movies
import json


STATUS_CODE_SUCCESS = 200
STATUS_NOT_FOUND = 404
STATUS_UNPROCESSABLE = 422


def get_request_data(request):
    return json.loads(request.data.decode('utf-8'))


@app.route('/actors')
def get_actors():
    actors = list(map(Actors.format, Actors.query.all()))
    result = {
        "success": True,
        "actors": actors
    }
    return jsonify(result)


@app.route('/actors', methods=['POST'])
def add_actors():
    if request.data:
        request_data = get_request_data(request)
        new_actor = Actors(name=request_data['name'],
                           age=request_data['age'],
                           gender=request_data['gender'])
        Actors.insert(new_actor)
        actors = list(map(Actors.format, [new_actor]))
        result = {
            "success": True,
            "actors": actors
        }
        return jsonify(result)
    else:
        abort(STATUS_UNPROCESSABLE)


@app.route('/movies')
def get_movies():
    movies = list(map(Movies.format, Movies.query.all()))
    result = {
        "success": True,
        "movies": movies
    }
    return jsonify(result)


@app.route('/movies', methods=['POST'])
def add_movies():
    if request.data:
        request_data = get_request_data(request)
        new_movie = Movies(title=request_data['title'],
                           release_date=request_data['release_date'])
        actor = Actors.query.get(request_data['actor_id'])
        new_movie.actor.append(actor)
        Movies.insert(new_movie)
        movies = list(map(Movies.format, [new_movie]))
        result = {
            "success": True,
            "movies": movies
        }
        return jsonify(result)
    else:
        abort(STATUS_UNPROCESSABLE)


@app.errorhandler(STATUS_UNPROCESSABLE)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": STATUS_UNPROCESSABLE,
        "message": "unprocessable"
    }), STATUS_UNPROCESSABLE


@app.errorhandler(STATUS_NOT_FOUND)
def not_found(error):
    return jsonify({
        "success": False,
        "error": STATUS_NOT_FOUND,
        "message": "resource not found"
    }), STATUS_NOT_FOUND
