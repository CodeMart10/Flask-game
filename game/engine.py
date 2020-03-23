from flask import (Blueprint, render_template)

bp = Blueprint('engine', __name__)

@bp.route('/')
def engine():
    return render_template('index.html')
