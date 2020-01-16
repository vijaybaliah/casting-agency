from flask_script import Manager
from flask_migrate import MigrateCommand
from dotenv import load_dotenv

from src.app import create_app
from src.database.models import setup_db


database_path = "postgres://{}:{}@{}/{}".format(
    'postgres', 'password', 'localhost:5432', 'casting')

load_dotenv()
app = create_app()
setup_db(app, database_path)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
