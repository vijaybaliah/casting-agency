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

Before running the test create a `.env` file in `./backend` folder with the following details.

```
ENVIRONMENT=development
CASTING_ASSISTANT_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6VTVOelZEUXpNNFJEZzNOalJHTjBKRU5rVTNRVFJDT0RJeU9UYzFORUU1T0RFek1FWkdSUSJ9.eyJpc3MiOiJodHRwczovL3ZpamF5ZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWRkNTdjNzM3ODk0YWYwZWZlMGE0ZjY3IiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTU3OTE4ODQ0NCwiZXhwIjoxNTc5MTk1NjQ0LCJhenAiOiJic2Y4aTA3amVuSDhWbTBqNEtPQ3djSkxnckFnMkFUbyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.pD5LgCG7QdsEf-_RK89E6r0W5w_kpMf4Rb2TorTi7VYIyKpgJSunYQpC48ieEYjTlZbyByZbQSUrYL0FAjFGtibi21kNaUNYvtWkqKGKHtYfkEJT9bDBKRP7vFf-hohA1llaqQHQqOabVI7Vqrz4gqsxHe-siRv8xmD_qi5KHD5O0MW6y51im7F2rst72-oBO7xt59fciFDMVnAbGAhSzYPe_mRZWnkL9cQs9VmWMxvUlL1px9Bl5MR9lzp9wHgD9Q1osqL0S1tbQ4a4NDqCs9WzYoZ9xeApOjTPdbpgwQzG3BxYYwDbfXzeDjIBswXPN9x-JBk-Wsxnz4meb96HKA
CASTING_DIRECTOR_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6VTVOelZEUXpNNFJEZzNOalJHTjBKRU5rVTNRVFJDT0RJeU9UYzFORUU1T0RFek1FWkdSUSJ9.eyJpc3MiOiJodHRwczovL3ZpamF5ZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWRmMDQ1ZTBjNzZiNDMwZTlhZGRlMGM4IiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTU3OTE4ODUxNSwiZXhwIjoxNTc5MTk1NzE1LCJhenAiOiJic2Y4aTA3amVuSDhWbTBqNEtPQ3djSkxnckFnMkFUbyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.PMYRvyOh7Rekzu5IyxvFZHAn4jj8oZVDsQTxnp9c9aLv0jHXi0oylnw8dbmo3glW65F4YR7iNXJCr6QPc-Z2m5-vObxdpEbMEfLlKeHL-y6AsGUPFvCn2ppX6g0hrqrBWxoenqxlngXdnjh1SrhfnH06VMbG7i8i1mZB8It6wiDEbdlu2kkwVkZMWiAH3qqO66YxBCdJPKmPLGmKJ3WeN67JgnM1kdoW2_P1wcHqVnPyp6lpN8DheKquAEyisQ1K_4UyZ1XIYTBNZSCioPH01rPySK5q16w7EhofL__UiTaVnsrgU2G25_zuOOX1z9mkDJV9G60W0U94VxLNgz0q9Q
EXECUTIVE_PRODUCER=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6VTVOelZEUXpNNFJEZzNOalJHTjBKRU5rVTNRVFJDT0RJeU9UYzFORUU1T0RFek1FWkdSUSJ9.eyJpc3MiOiJodHRwczovL3ZpamF5ZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWUxZGQ4NzI3YWFjNTkwZDEyNTQxMTBkIiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTU3OTE4ODYyMywiZXhwIjoxNTc5MTk1ODIzLCJhenAiOiJic2Y4aTA3amVuSDhWbTBqNEtPQ3djSkxnckFnMkFUbyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.llbF0rSSsx-UKOHk8451o7LdtoN7Ck0tV07MssrlcHSDskRj1oqHmX36ikJx4PEBk4XQYvAUcEGq1L1clSRo6vebcaMdzuWCRSnpKzQhGMl3D0Ioc4VadQ37ONyDEnQdGN6z8G3Qs-0aE-5cRo6bwW7VAwJYYSivN0JzrxTUhzgY1GcpAhvNQrtNCvxisASGIHvTT2VHuyC3ySLk8hrHxeWnUAgAvv9aQZ7-tLQ_IhCSqDRw5FhKmPH5IA5g3pcf8S8SDuCLRwZprDTFuAx6x5rVoJdIwLVIE-FoCqptyvfB9B-dxaVPhdZbF07kh5KQ-547yCKM8AzdTkMeSErxmA
```

```
dropdb casting_test -U postgres
createdb casting_test -U postgres
psql casting_test < casting.psql
python test_app.py
```

##### Error Codes

Currently it supports 401, 404 and 422 error codes