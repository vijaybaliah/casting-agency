from flask import Flask
from src.database.models import setup_db

app = Flask(__name__)
setup_db(app)

if __name__ == '__main__':
    app.run(debug=True)
