from app import app
from app.forms import *
from werkzeug.utils import redirect
from flask import render_template, request, url_for, session
from flask_session import sessions

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = Intro()
    if form.validate_on_submit():
        session['room'] = request.form["room"]
        width = request.form.get("width")
        height = request.form.get("height")
        return redirect(url_for("quest", width=width, height=height))
    return render_template("index.html", form=form)


@app.route("/quest/<int:width>x<int:height>", methods=["GET", "POST"])
def quest(width, height):
    if request.method == "POST":
        message = "Move"
        form = Quest()
        place = session['place']
        return render_template(
            "start.html",
            position=place.position,
            rooms=place.rooms,
            current_room=place.get_name(),
            form=form,
            message=message,
        )
    else:
        place = Rooms(int(session.pop('room')), width + 2, height + 2)
        form = Quest()
        message = "Hello"
        return render_template(
            "start.html",
            position=place.position,
            rooms=place.rooms,
            current_room=place.get_name(),
            form=form,
            message=message,
        )
