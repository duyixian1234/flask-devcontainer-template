"""Define the flask app"""
from flask import Flask

app = Flask(__name__)


@app.get("/")
@app.get("/<name>")
def greet(name: str | None = None):
    """Greet with optional name"""
    return f"Hello, {name or 'World'}."
