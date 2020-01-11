from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from src.app import app
from src.database.models import db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
# from flask import Flask
# from src.database.models import setup_db

# app = Flask(__name__)
# setup_db(app)

# if __name__ == '__main__':
#  app.run(debug=True)
