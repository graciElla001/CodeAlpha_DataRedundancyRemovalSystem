from flask import Flask, render_template, request
from database import create_database

app = Flask(__name__)

create_database()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_record():

    full_name = request.form["full_name"]
    email = request.form["email"]
    phone = request.form["phone"]

    print("Full Name:", full_name)
    print("Email:", email)
    print("Phone:", phone)

    return f"""
    Record received successfully!

    <br><br>

    Name: {full_name}

    <br>

    Email: {email}

    <br>

    Phone: {phone}
    """

if __name__ == "__main__":
    app.run(debug=True)