from flask_pymongo import PyMongo
from flask import Flask

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/my_database?retryWrites=true&w=majority"
mongo = PyMongo(app)

print(mongo.db)  # Should print the MongoDB database object
