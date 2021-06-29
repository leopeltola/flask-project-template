from flask import current_app, render_template

from app.main import bp


@bp.route("/")
def index():
    return render_template("main/index.html")

@bp.route("/about")
def about():
    return render_template("main/about.html")
