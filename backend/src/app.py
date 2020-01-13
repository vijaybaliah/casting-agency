from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
import json

from src.database.models import Actors, Movies
from src.utils.constants import STATUS_UNPROCESSABLE, STATUS_NOT_FOUND,\
    INTERNAL_SERVER_ERROR
from src.auth import AuthError, requires_auth


def get_request_data(request):
    return json.loads(request.data.decode('utf-8'))


def create_app():
    app = Flask(__name__)
    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(payload):
        actors = list(map(Actors.format, Actors.query.all()))
        result = {
            "success": True,
            "actors": actors
        }
        return jsonify(result)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actors(payload):
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

    @app.route('/actors', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actors(payload):
        if request.data:
            request_data = get_request_data(request)
            actor = Actors.query.get(request_data['id'])
            if actor:
                actor.name = request_data['name']
                actor.age = request_data['age']
                actor.gender = request_data['gender']
                Actors.update(actor)
                actors = list(map(Actors.format, [actor]))
                result = {
                    "success": True,
                    "actors": actors
                }
                return jsonify(result)
            else:
                abort(STATUS_NOT_FOUND)
        else:
            abort(STATUS_UNPROCESSABLE)

    @app.route('/actors', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(payload):
        if request.data:
            request_data = get_request_data(request)
            actor = Actors.query.get(request_data['id'])
            if actor:
                Actors.delete(actor)
                actors = list(map(Actors.format, [actor]))
                result = {
                    "success": True,
                    "actors": actors
                }
                return jsonify(result)
            else:
                abort(STATUS_NOT_FOUND)
        else:
            abort(STATUS_UNPROCESSABLE)

    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(payload):
        movies = list(map(Movies.format, Movies.query.all()))
        result = {
            "success": True,
            "movies": movies
        }
        return jsonify(result)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movies(payload):
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

    @app.route('/movies', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movies(payload):
        if request.data:
            request_data = get_request_data(request)
            movie = Movies.query.get(request_data['id'])
            if movie:
                movie.title = request_data['title']
                movie.release_date = request_data['release_date']
                actor_id = request_data['actor_id']
                actor = Actors.query.get(actor_id)
                movie.actor = [actor]
                updated_movie = Movies.update(movie)
                result = {
                    "success": True,
                    "movies": updated_movie
                }
                return jsonify(result)
            else:
                abort(STATUS_NOT_FOUND)
        else:
            abort(STATUS_UNPROCESSABLE)

    @app.route('/movies', methods=['delete'])
    @requires_auth('delete:movies')
    def delete_movies(payload):
        if request.data:
            request_data = get_request_data(request)
            movie = Movies.query.get(request_data['id'])
            if movie:
                Movies.delete(movie)
                movies = list(map(Movies.format, [movie]))
                result = {
                    "success": True,
                    "movies": movies
                }
                return jsonify(result)
            else:
                abort(STATUS_NOT_FOUND)
        else:
            abort(STATUS_UNPROCESSABLE)

    @app.errorhandler(INTERNAL_SERVER_ERROR)
    def internal_server(error):
        return jsonify({
            "success": False,
            "error": INTERNAL_SERVER_ERROR,
            "message": "internal server error"
        }), INTERNAL_SERVER_ERROR

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
    
    @app.errorhandler(AuthError)
    def auth_error(e):
        return jsonify(e.error), e.status_code

    with app.app_context():
        db = SQLAlchemy()
        db.init_app(app)
        db.create_all()

    return app
