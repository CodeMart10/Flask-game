from flask import (Blueprint, flash, render_template, redirect, url_for, request, session)
from . import character

bp = Blueprint('engine', __name__)

@bp.route('/', methods=('GET', 'POST'))
def user():
    if request.method == 'POST':
        username = request.form['username']
        error = None

        if not username:
            error = 'Username is required.'

        return render_template('rooms/index.html', username=username)

        flash(error)

    return render_template('name/username.html')

@bp.route('/engine/<character>')
def char(character, name):
    if character == 'Tank':
        return render_template('rooms/rooms.html', character=character, name=name)
    if character == 'Knight':
        return render_template('rooms/rooms.html', character=character)
    if character == 'Assassin':
        return render_template('rooms/rooms.html', character=character)
