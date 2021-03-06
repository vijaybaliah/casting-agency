from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Column, String, Integer, ForeignKey,\
    DateTime

from src.utils.helpers import get_env_variable

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)


def setup_db(app, database_path):
    SQLALCHEMY_DATABASE_URI = get_env_variable('DATABASE_URL', database_path)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["DEBUG"] = True
    db.app = app
    db.init_app(app)
    Migrate(app, db)


movies = db.Table('movies_association',
                  Column('actor_id', Integer, ForeignKey('actors.id'),
                         primary_key=True),
                  Column('movie_id', Integer, ForeignKey('movies.id'),
                         primary_key=True))


class Actors(db.Model):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    movie = db.relationship('Movies',
                            secondary=movies,
                            backref=db.backref('actor', lazy=True))

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }


class Movies(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False, unique=True)
    release_date = Column(DateTime, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
        actors = list(map(Actors.format, self.actor))
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'actors': actors
        }

    def format(self):
        actors = list(map(Actors.format, self.actor))
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'actors': actors
        }
