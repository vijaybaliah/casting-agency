import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from src.app import create_app
from src.database.models import setup_db


class CastingTestCase(unittest.TestCase):
    """This class represents the casting test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_test"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'vijay', 'password', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.code_success = 200
        self.code_not_found = 404
        self.code_unprocessable = 422
        self.code_unauthorised = 401

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def format_response(self, response):
        return json.loads(response.data)
    """
    TODO
    Write at least one test for each test for successful operation and for
    expected errors.
    """

    def test_get_actors(self):
        res = self.client().get('/actors', headers={
            'Authorization': 'Bearer {}'.format(
                os.getenv('CASTING_ASSISTANT_TOKEN'))
        })
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_success)
        self.assertTrue(data['actors'])

    def test_get_actors_unauthorised(self):
        res = self.client().get('/actors')
        self.assertEqual(res.status_code, self.code_unauthorised)

    def test_get_movies(self):
        res = self.client().get('/movies', headers={
            'Authorization': 'Bearer {}'.format(
                os.getenv('CASTING_ASSISTANT_TOKEN'))
        })
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_success)
        self.assertTrue(data['movies'])

    def test_get_movies_unauthorised(self):
        res = self.client().get('/movies')
        self.assertEqual(res.status_code, self.code_unauthorised)

    def test_post_actors(self):
        mock_data = {
            "name": "vijay",
            "age": 30,
            "gender": "male"
        }
        res = self.client().post('/actors', json=mock_data, headers={
            'Authorization': 'Bearer {}'.format(
                os.getenv('CASTING_DIRECTOR_TOKEN'))
        })
        self.client().post('/actors', json=mock_data, headers={
            'Authorization': 'Bearer {}'.format(
                os.getenv('CASTING_DIRECTOR_TOKEN'))
        })
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_success)
        self.assertTrue(data['actors'])

    def test_post_actors_unauthorised(self):
        res = self.client().post('/actors')
        self.assertEqual(res.status_code, self.code_unauthorised)

    def test_post_actors_error(self):
        res = self.client().post('/actors', headers={
            'Authorization': 'Bearer {}'.format(
                os.getenv('CASTING_DIRECTOR_TOKEN'))
        })
        self.assertEqual(res.status_code, self.code_unprocessable)

    def test_patch_actors(self):
        mock_data = {
            "id": 2,
            "name": "vijay",
            "age": 30,
            "gender": "male"
        }
        res = self.client().patch('/actors', json=mock_data, headers={
            'Authorization': 'Bearer {}'.format(
                os.getenv('CASTING_DIRECTOR_TOKEN'))
        })
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_success)
        self.assertTrue(data['actors'])

    def test_patch_actors_unauthorised(self):
        res = self.client().patch('/actors')
        self.assertEqual(res.status_code, self.code_unauthorised)

    def test_patch_actors_error(self):
        res = self.client().patch('/actors', headers={
            'Authorization': 'Bearer {}'.format(
                os.getenv('CASTING_DIRECTOR_TOKEN'))
        })
        self.assertEqual(res.status_code, self.code_unprocessable)

    def test_delete_actors(self):
        mock_data = {
            "id": 1,
            "name": "vijay",
            "age": 30,
            "gender": "male"
        }
        res = self.client().delete('/actors', json=mock_data, headers={
            'Authorization': 'Bearer {}'.format(
                os.getenv('CASTING_DIRECTOR_TOKEN'))
        })
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_success)
        self.assertTrue(data['actors'])

    def test_delete_actors_unauthorised(self):
        res = self.client().delete('/actors')
        self.assertEqual(res.status_code, self.code_unauthorised)

    def test_delete_actors_error(self):
        res = self.client().delete('/actors', headers={
            'Authorization': 'Bearer {}'.format(
                os.getenv('CASTING_DIRECTOR_TOKEN'))
        })
        self.assertEqual(res.status_code, self.code_unprocessable)

    def test_post_movies(self):
        mock_data = {
            "title": "movie_title_test112313",
            "release_date": "01/02/2019",
            "actor_id": 2
        }
        res = self.client().post('/movies', json=mock_data, headers={
            'Authorization': 'Bearer {}'.format(
                os.getenv('EXECUTIVE_PRODUCER'))
        })
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_success)
        self.assertTrue(data['movies'])

    def test_post_movies_unauthorised(self):
        res = self.client().post('/movies')
        self.assertEqual(res.status_code, self.code_unauthorised)

    def test_post_movies_error(self):
        res = self.client().post('/movies', headers={
            'Authorization': 'Bearer {}'.format(
                os.getenv('EXECUTIVE_PRODUCER'))
        })
        self.assertEqual(res.status_code, self.code_unprocessable)

    def test_patch_movies(self):
        mock_data = {
            "id": 4,
            "title": "new movie title from update",
            "release_date": "02/01/2019",
            "actor_id": 2
        }
        res = self.client().patch('/movies', json=mock_data, headers={
            'Authorization': 'Bearer {}'.format(
                os.getenv('CASTING_DIRECTOR_TOKEN'))
        })
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_success)
        self.assertTrue(data['movies'])

    def test_patch_movies_unauthorised(self):
        res = self.client().patch('/movies')
        self.assertEqual(res.status_code, self.code_unauthorised)

    def test_patch_movies_error(self):
        res = self.client().patch('/movies', headers={
            'Authorization': 'Bearer {}'.format(
                os.getenv('CASTING_DIRECTOR_TOKEN'))
        })
        self.assertEqual(res.status_code, self.code_unprocessable)

    def test_delete_movies(self):
        mock_data = {
            "id": 2
        }
        res = self.client().delete('/movies', json=mock_data, headers={
            'Authorization': 'Bearer {}'.format(
                os.getenv('EXECUTIVE_PRODUCER'))
        })
        data = self.format_response(res)
        self.assertEqual(res.status_code, self.code_success)
        self.assertTrue(data['movies'])

    def test_delete_movies_unauthorised(self):
        res = self.client().delete('/movies')
        self.assertEqual(res.status_code, self.code_unauthorised)

    def test_delete_movies_error(self):
        res = self.client().delete('/movies', headers={
            'Authorization': 'Bearer {}'.format(
                os.getenv('EXECUTIVE_PRODUCER'))
        })
        self.assertEqual(res.status_code, self.code_unprocessable)


# Make the tests conveniently executable
if __name__ == "__main__":
    load_dotenv()
    unittest.main()
