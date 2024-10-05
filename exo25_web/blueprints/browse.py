from flask import Blueprint, render_template, redirect, url_for, request

browse = Blueprint("browse", __name__)

@browse.route("/")
def index():
    search = "test"
    return redirect(url_for("browse.search", search=search))

@browse.route("/<string:search>", methods=["GET", "POST"])
def search(search: str):
    return render_template("browse.html")