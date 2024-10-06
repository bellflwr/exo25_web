from flask import Blueprint, redirect, render_template, url_for, request

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

        return "", 201

    return render_template("create.html", id=id)
