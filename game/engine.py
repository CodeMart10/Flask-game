from flask import (Blueprint, flash, render_template, redirect, url_for, request, session)

bp = Blueprint('engine', __name__)

@bp.route('/', methods=('GET', 'POST'))
def user():
    if request.method == 'POST':
        username = request.form['username']
        error = None

        if not username:
            error = 'Username is required.'

        return render_template('index.html', username=username)

        flash(error)

    return render_template('username.html')
