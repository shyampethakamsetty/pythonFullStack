import os

class Config:
    # MongoDB URI (replace with your own connection string if using MongoDB Atlas)
    MONGO_URI = "mongodb+srv://sivashyam121:8r7a4fZ95nwBHLH5@cluster0.lzdyu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    SECRET_KEY = os.urandom(24)
