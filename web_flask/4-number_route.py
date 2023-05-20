#!/usr/bin/python3
"""Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'


@app.route("/c/<string:text>", strict_slashes=False)
def c(text):
    """
    Display 'C ' followed by the value of the text variable
    Replaces underscore _ symbols with a space
    """
    if "_" in text:
        text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/")
@app.route("/python/<string:text>")
def python(text="is cool"):
    """
    Display 'Python ', followed by the value of the text variable
    Replaces underscore _ symbols with a space
    """
    if "_" in text:
        text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Display 'n is a number' only if n is an integer"""
    if isinstance(n, int):
        return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
