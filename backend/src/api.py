from flask import Flask, jsonify, abort, request
from database.models import setup_db, Actors, Movies
import json

app = Flask(__name__)
setup_db(app)

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


if __name__ == '__main__':
    app.run()
