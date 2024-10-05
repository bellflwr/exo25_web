from flask import Blueprint, render_template, redirect, url_for, request

browse = Blueprint("browse", __name__)

@browse.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search = request.form['search']
        return redirect(url_for("browse.searched", search=search))

    return render_template("browse.html")

@browse.route("/<string:search>", methods=["GET", "POST"])
def searched(search: str):
    if request.method == "POST":
        search = request.form['search']
        return redirect(url_for("browse.searched", search=search))
    return render_template("browse.html", search=search)