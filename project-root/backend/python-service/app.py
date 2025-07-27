from flask import Flask

app = Flask(__name__)

@app.route("/ml/echo/<word>")
def echo(word):
    return {"echo": word}

if __name__ == "__main__":
    app.run(port=5000)