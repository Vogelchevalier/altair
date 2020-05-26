from flask import render_template
from application import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/text")
def text():
    return render_template("text.html")


@app.errorhandler(403)
def not_found(e):
    return render_template('errors/403.html'), 403


@app.errorhandler(404)
def forbidden(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500