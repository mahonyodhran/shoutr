from flask import (
    Blueprint, render_template
)
from werkzeug.exceptions import abort
from shoutr.db import get_db

bp = Blueprint('profile', __name__, url_prefix='/profile')

@bp.route('/<int:id>/', methods=('GET', 'POST'))
def get_user(id):
    user = get_db().execute(
        'SELECT id, username'
        ' FROM user'
        ' WHERE id = ?',
        (id,)
    ).fetchone()

    if user is None:
        abort(404, f"User {id} doesn't exist.")

    return render_template('profile/view-profile.html', user=user)