import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "hey whats up hello"
