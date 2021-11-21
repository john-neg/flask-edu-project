from app import app
from app.func import *
from app.forms import *
from werkzeug.utils import redirect
from flask import render_template, request, url_for


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = Intro()
    if form.validate_on_submit():
        room = request.form.get('room')
        return redirect(url_for('quest', room=room))
    return render_template('index.html', form=form)


@app.route('/quest', methods=['GET', 'POST'])
def quest():
    form = Quest()
    message = room
    return render_template('start.html', room=room, form=form, message=message)
