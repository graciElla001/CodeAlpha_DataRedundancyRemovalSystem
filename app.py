from flask import Flask, render_template, request

from database import (
    create_database,
    add_user,
    user_exists,
    get_all_users,
    get_records
)

from duplicate_checker import check_name_similarity

app = Flask(__name__)

# Create the database (if it doesn't already exist)
create_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add_record():

    # Get data from the form and normalize it
    full_name = request.form["full_name"].strip()
    email = request.form["email"].strip().lower()
    phone = request.form["phone"].strip()

    # Check for exact duplicate email
    if user_exists(email):
        return render_template("duplicate.html")

    # Check for similar names
    existing_users = get_all_users()

    is_similar, matched_name, similarity = check_name_similarity(
        full_name,
        existing_users
    )

    # Warn if a similar name is found
    if is_similar:
        return render_template(
            "warning.html",
            matched_name=matched_name,
            similarity=f"{similarity:.0f}",
            full_name=full_name,
            email=email,
            phone=phone
        )

    # Save as a unique record
    add_user(full_name, email, phone, "Unique")

    return render_template("success.html")


@app.route("/save_anyway", methods=["POST"])
def save_anyway():

    full_name = request.form["full_name"]
    email = request.form["email"]
    phone = request.form["phone"]

    add_user(
        full_name,
        email,
        phone,
        "False Positive"
    )

    return render_template("success.html")

@app.route("/records")
def records():

    records = get_records()

    return render_template(
        "records.html",
        records=records
    )


if __name__ == "__main__":
    app.run(debug=True)