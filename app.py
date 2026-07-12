from flask import Flask
from database import create_database

app = Flask(__name__)

create_database()


@app.route("/")
def home():
    return "Welcome to the CodeAlpha Data Redundancy Removal System!"


if __name__ == "__main__":
    app.run(debug=True)