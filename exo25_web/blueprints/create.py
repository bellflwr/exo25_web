from flask import Blueprint, redirect, render_template, url_for, request

from exo25_web.database import db
from exo25_web.database.db import Exoplanet

create = Blueprint("create", __name__)


@create.route("/")
def index():
    # create_exoplanet()
    id = 7
    return redirect(url_for("create.editor", id=id))


@create.route("/<int:id>", methods=["GET", "POST"])
def editor(id: int):
    if request.method == "POST":
        f = request.form

        cur = db.get_db().cursor()
        
        planet = Exoplanet(
            None, 
            f.get("name", type=str),
            f.get("planet-type", type=str),
            f.get("diameter", type=float),
            f.get("distance", type=float),
            f.get("planet-material", type=str),
            f.get("gas", type=bool, default=False),
            f.get("rings", type=int),
            f.get("colour", type=str),
            f.get("climate", type=float),
            f.get("star-type", type=str),
        )



        planet.write(cur)

        db.get_db().commit()

        return "", 201

    return render_template("create.html", id=id)
