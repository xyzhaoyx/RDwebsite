from flask import (
    Blueprint, render_template, url_for
)

bp = Blueprint('index', __name__)

@bp.route('/')
def hello():
    return render_template('index.html')