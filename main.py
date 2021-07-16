# from flask import Flask
# from markupsafe import escape

# app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, endermare !</p>"


# @app.route("/<name>")
# def destroy_world(name):
#     nomb = ''.join(reversed(name))
#     return f"<p>{nomb} !eramredne, olleH</p>"

from app import app

if __name__ == "__main__":
    app.run()

