from flask import Flask, render_template, request, redirect, url_for
import os
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://sivashyam121:8r7a4fZ95nwBHLH5@cluster0.mongodb.net/my_database?retryWrites=true&w=majority"
app.secret_key = os.urandom(24)

mongo = PyMongo(app)

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password)

        # Insert user into 'users' collection
        mongo.db.users.insert_one({
            "username": username,
            "password": hashed_password
        })

        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Find the user in the 'users' collection
        user = mongo.db.users.find_one({"username": username})

        if user and check_password_hash(user["password"], password):  # Verify hashed password
            return redirect(url_for("account"))
        else:
            return "Invalid username or password."

    return render_template("login.html")

@app.route("/account")
def account():
    return render_template("account.html")

if __name__ == "__main__":
    app.run(debug=True)
