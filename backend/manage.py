from flask import Flask
from flask_script import Manager
from flask_migrate import MigrateCommand

from src.database.models import setup_db

app = Flask(__name__)
setup_db(app)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
