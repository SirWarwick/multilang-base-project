from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongo:27017/")
db = client.test_database

@app.route("/ml/echo/<word>")
def echo(word):
    db.logs.insert_one({"word": word})
    return {"echo": word}

if __name__ == "__main__":
    app.run(port=5000)
