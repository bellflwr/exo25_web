from flask import Blueprint, render_template, redirect, url_for, request

from exo25_web.database import db

browse = Blueprint("browse", __name__)


@browse.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search = request.form["search"]
        cur = db.get_db().cursor()
        c = cur.execute(
            f"SELECT COUNT(*) FROM Exoplanets WHERE NAME = '{search}'"
        ).fetchone()[0]
        if search == "" or c == 0:
            return redirect(url_for("browse.index"))

        return redirect(url_for("browse.searched", search=search))

    return render_template("browse.html")


@browse.route("/<string:search>", methods=["GET", "POST"])
def searched(search: str):
    cur = db.get_db().cursor()

    planet = db.Exoplanet.from_name(cur, search)

    if request.method == "POST":
        search = request.form["search"]
        if search == "":
            return redirect(url_for("browse.index"))
        return redirect(url_for("browse.searched", search=search))
    return render_template(
        "browse.html",
        search=search,
        planet_type=planet.planet_type,
        planet_diameter=planet.diameter,
        planet_distance=planet.distance,
        planet_material=planet.material,
        planet_colour=planet.colour,
        planet_climate=planet.climate,
        star_type=planet.star_type,
    )
