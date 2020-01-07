from flask import Flask
from database.models import setup_db

app = Flask(__name__)
setup_db(app)
