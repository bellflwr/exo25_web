from flask import Blueprint, render_template

learn = Blueprint("learn", __name__)

@learn.route("/")
def index():
    return render_template("learn.html")