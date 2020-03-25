from flask import (Blueprint, render_template, redirect, url_for, request, session)

bp = Blueprint('engine', __name__)

@bp.route('/', methods=('GET', 'POST'))
def user():
    if request.method == 'POST':
        username = request.form['username']
        error = None

        if not username:
            error = 'Username is required.'

        if error is None:
            session.clear()
            session['username'] = username
            return render_template('index.html', username=username)

        flash(error)

    return render_template('username.html')
