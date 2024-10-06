from flask import Blueprint, render_template, redirect, url_for, request

from exo25_web.database import db

browse = Blueprint("browse", __name__)

@browse.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search = request.form['search']
        cur = db.get_db().cursor()
        c = cur.execute(f"SELECT COUNT(*) FROM Exoplanets WHERE NAME = '{search}'").fetchone()[0]
        if search == "" or c == 0:
            return redirect(url_for("browse.index"))

        return redirect(url_for("browse.searched", search=search))

    return render_template("browse.html")

@browse.route("/<string:search>", methods=["GET", "POST"])
def searched(search: str):
    cur = db.get_db().cursor()
    planet_type = cur.execute(f"SELECT type FROM Exoplanets WHERE NAME = '{search}'").fetchone()[0]
    planet_diameter = cur.execute(f"SELECT diameter FROM Exoplanets WHERE NAME = '{search}'").fetchone()[0]
    planet_distance = cur.execute(f"SELECT distance FROM Exoplanets WHERE NAME = '{search}'").fetchone()[0]
    planet_material = cur.execute(f"SELECT material FROM Exoplanets WHERE NAME = '{search}'").fetchone()[0]
    planet_colour = cur.execute(f"SELECT colour FROM Exoplanets WHERE NAME = '{search}'").fetchone()[0]
    planet_climate = cur.execute(f"SELECT climate FROM Exoplanets WHERE NAME = '{search}'").fetchone()[0]
    star_type = cur.execute(f"SELECT startype FROM Exoplanets WHERE NAME = '{search}'").fetchone()[0]
    if request.method == "POST":
        search = request.form['search']
        if search == "":
            return redirect(url_for("browse.index"))
        return redirect(url_for("browse.searched", search=search))
    return render_template("browse.html", search=search, planet_type=planet_type, planet_diameter=planet_diameter, planet_distance=planet_distance, planet_material=planet_material, planet_colour=planet_colour, planet_climate=planet_climate, star_type=star_type)