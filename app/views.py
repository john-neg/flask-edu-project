from app import app
from app.forms import *
from werkzeug.utils import redirect
from flask import render_template, request, url_for, session


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = Intro()
    if form.validate_on_submit():
        session['room'] = request.form.get('room')
        width = request.form.get('width')
        height = request.form.get('height')
        return redirect(url_for('quest', width=width, height=height, room=room))
    return render_template('index.html', form=form)


@app.route('/quest/<int:width>x<int:height>', methods=['GET', 'POST'])
def quest(width, height):
    r = Rooms(session['room'], width+2, height+2)
    form = Quest()
    message = "Hello"
    return render_template('start.html', rooms=r.rooms, form=form, message=message)
