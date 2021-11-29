from app import app
from app.models import Rooms
from app.forms import *
from werkzeug.utils import redirect
from flask import render_template, request, url_for


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = Intro()
    if request.method == 'GET':
        form.width.data = 7
        form.height.data = 7
    if form.validate_on_submit():
        width = request.form.get("width")
        height = request.form.get("height")
        return redirect(url_for("quest", width=width, height=height))
    return render_template("index.html", form=form)


@app.route("/quest/<int:width>x<int:height>", methods=["GET", "POST"])
def quest(width, height):
    form = Quest()
    if request.method == 'GET':
        form.steps.data = 1
    if form.validate_on_submit():
        place = Rooms()
        direction = request.form.get("direction")
        steps = request.form.get("steps")
        for i in range(int(steps)):
            place.change_position(direction)
        return render_template(
            "start.html",
            position=place.position,
            rooms=place.rooms,
            current_room=place.get_name(),
            form=form,
            message=place.message,
        )
    else:
        place = Rooms(width + 2, height + 2)
        return render_template(
            "start.html",
            position=place.position,
            rooms=place.rooms,
            current_room=place.get_name(),
            form=form,
            message=place.message,
        )
