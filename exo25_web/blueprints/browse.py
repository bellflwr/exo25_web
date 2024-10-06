from flask import Blueprint, render_template, redirect, url_for, request

from exo25_web.database import db

browse = Blueprint("browse", __name__)

temp = {
    "O": "40 000k",
    "B": "20 000k",
    "A": "8 500k",
    "F": "6 500k",
    "G": "5 700k",
    "K": "4 500k",
    "M": "3 200k"
}

radius = { # Measured in suns
    "O": "10",
    "B": "5",
    "A": "1.7",
    "F": "1.3",
    "G": "1.0",
    "K": "0.8",
    "M": "0.3"
}

mass = { # Measured in suns
    "O": "50",
    "B": "10",
    "A": "2.0",
    "F": "1.5",
    "G": "1.0",
    "K": "0.7",
    "M": "0.2"
}

luminosity = { # Measured in suns
    "O": "100 000",
    "B": "1000",
    "A": "20",
    "F": "4",
    "G": "1.0",
    "K": "0.2",
    "M": "0.01"
}

lifetime = { # Measured in million years
    "O": "10",
    "B": "100",
    "A": "1000",
    "F": "3000",
    "G": "10 000",
    "K": "50 000",
    "M": "200 000"
}

abundance = {
    "O": "0.00001%",
    "B": "0.1%",
    "A": "0.7%",
    "F": "2%",
    "G": "3.5%",
    "K": "8%",
    "M": "80%"
}

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
