from flask import render_template
from application import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/league_on_arch")
def league_on_arch():
    return render_template("league_on_arch.html")


@app.route("/js_test")
def js_test():
    return render_template("js_test.html")


##################################################
@app.route("/401")
def unauthorized_i():
    return render_template('errors/401.html'), 401


@app.errorhandler(401)
def unauthorized(e):
    return render_template('errors/401.html'), 401


##################################################
@app.route("/403")
def forbidden_i():
    return render_template('errors/403.html'), 403


@app.errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html'), 403


##################################################
@app.route("/404")
def not_found_i():
    return render_template('errors/404.html'), 404


@app.errorhandler(404)
def not_found(e):
    return render_template('errors/404.html'), 404


##################################################
@app.route("/405")
def method_not_allowed_i():
    return render_template('errors/405.html'), 405


@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('errors/405.html'), 405


##################################################
@app.route("/500")
def internal_server_error_i():
    return render_template('errors/500.html'), 500


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500


##################################################
@app.route("/502")
def bad_gateway_i():
    return render_template('errors/502.html'), 502


@app.errorhandler(502)
def bad_gateway(e):
    return render_template('errors/502.html'), 502
