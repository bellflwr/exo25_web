from flask import Blueprint, render_template, redirect, url_for, request

from exo25_web.database import db

browse = Blueprint("browse", __name__)


@browse.route("/")
def index():
    search = request.args.get("search", default="", type=str)

    if search == "":
        return render_template("search.html")

    cur = db.get_db().cursor()
    planet = db.Exoplanet.from_name(cur, search)

    if planet is None:
        return redirect(url_for("browse.index"))

    return redirect(url_for("browse.page", id=planet.id))


@browse.route("/<int:id>", methods=["GET"])
def page(id: int):
    cur = db.get_db().cursor()

    planet = db.Exoplanet.from_id(cur, id)

    if planet is None:
        # TODO handle this
        raise Exception()

    return render_template("planet.html", planet=planet)
