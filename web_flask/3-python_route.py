#!/usr/bin/python3
"""
Starts Flask web app
Routes:
    /: display "Hello HBNB!"
    /hbnb: display "HBNB"
    /c/<text>: display "C <text>"
    /python/(<text>): display “Python <text>”
        The default value of text is “is cool”
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_route():
    """prints Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints HBNB"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """Prints C followed by <text> content"""
    text = text.replace("_", " ")
    return "C %s" % text


@app.route("/python/")
@app.route("/python/<text>")
def python(text="is cool"):
    """
    Display 'Python ', followed by the value of the text variable
    Replaces underscore _ symbols with a space
    """
    if "_" in text:
        text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
