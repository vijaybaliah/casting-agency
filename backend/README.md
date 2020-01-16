# Casting Agency Backend

## Motivation

In the media industry, we need to find out which actor is currently available for booking the movies here is where the casting agency comes into the picture. It exposes API with restricted access to members so that the members can utilize the information to book the same.

## Getting Started

### Installing Dependencies

#### Python 3.6.10

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

##### Database Migration

First create the database
```
createdb casting -U postgres
psql casting < casting.psql
```
or you can run the migration scripts as follows
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

##### Running the server

Navigate to `/backend` and run `python manage.py runserver`

##### Supported api

###### Get actors
```
GET /actors
```
gives the list os actors
- permission required `get:actors`

###### Add actors
```
POST /actors
```
adds a new actor

request body
```
{
	"name": "vijay",
	"age": 68,
	"gender": "male"
}
```
- permission required `post:actors`

###### Update actors
```
PATCH /actors
```
updates the actors

request body
```
{
	"id": 1,
	"name": "vijay",
	"age": 30,
	"gender": "male"
}
```
- permission required `patch:actors`

###### Delete actors
```
DELETE /actors
```
deletes the actors

request body
```
{
	"id": 1
}
```
- permission required `delete:actors`

###### Get movies
```
GET /movies
```
gives the list os movies
- permission required `get:movies`

###### Add movies
```
POST /movies
```
adds a new actor

request body
```
{
	"title": "movie_title",
	"release_date": "01/02/2019",
	"actor_id": 1
}
```
- permission required `post:movies`

###### Update movies
```
PATCH /movies
```
updates the movies

request body
```
{
	"id": 1,
	"title": "new movie title from update",
	"release_date": "02/01/2019",
	"actor_id": "1"
}
```
- permission required `patch:movies`

###### Delete movies
```
DELETE /movies
```
deletes the movies

request body
```
{
	"id": 1
}
```
- permission required `delete:movies`


##### Heroku Domain

The project has been hosted in `https://vijay-casting-agency.herokuapp.com` and has the above mentioned routes for example `https://vijay-casting-agency.herokuapp.com/actors` etc

##### Testing

```
dropdb casting_test -U postgres
createdb casting_test -U postgres
psql casting_test < casting.psql
python test_app.py
```

##### Error Codes

Currently it supports 401, 404 and 422 error codes