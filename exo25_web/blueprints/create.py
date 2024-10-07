from flask import Blueprint, redirect, render_template, url_for, request

from exo25_web.database import db
from exo25_web.database.db import Exoplanet

create = Blueprint("create", __name__)


@create.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        f = request.form

        cur = db.get_db().cursor()
        
        planet = Exoplanet(
            None, 
            f.get("name", type=str),
            f.get("diameter", type=float),
            f.get("distance", type=float),
            False,
            f.get("height-multiplier", type=float),
            0,
            f.get("freq", type=float),
            f.get("amp", type=float),
            f.get("scale", type=float),
            f.get("colour", type=str),
            f.get("star-type", type=str),
        )



        id = planet.write(cur)

        db.get_db().commit()

        return redirect(url_for("browse.page", id=id))

    return render_template("create.html")
