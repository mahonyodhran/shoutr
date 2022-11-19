from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from shoutr.auth import login_required
from shoutr.db import get_db

bp = Blueprint("shout", __name__)


@bp.route("/")
@login_required
def index():
    db = get_db()
    shouts = db.execute(
        "SELECT p.id, shout, created, author_id, username"
        " FROM shout p JOIN user u ON p.author_id = u.id"
        " ORDER BY created DESC"
    ).fetchall()
    return render_template("shout/index.html", shouts=shouts)


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        shout = request.form["shout"]
        error = None

        if not shout:
            error = "Shout is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO shout (shout, author_id)" " VALUES (?, ?)",
                (shout, g.user["id"]),
            )
            db.commit()
            return redirect(url_for("shout.index"))

    return render_template("shout/create.html")


def get_shout(id, check_author=True):
    shout = (
        get_db()
        .execute(
            "SELECT p.id, shout, created, author_id, username"
            " FROM shout p JOIN user u ON p.author_id = u.id"
            " WHERE p.id = ?",
            (id,),
        )
        .fetchone()
    )

    if shout is None:
        abort(404, f"Shout id {id} doesn't exist.")

    if check_author and shout["author_id"] != g.user["id"]:
        abort(403)

    return shout


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    shout = get_shout(id)

    if request.method == "POST":
        shout_request = request.form["shout"]
        error = None

        if not shout_request:
            error = "Shout is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE shout SET shout = ?" " WHERE id = ?", (shout_request, id)
            )
            db.commit()
            return redirect(url_for("shout.index"))

    return render_template("shout/update.html", shout=shout)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    get_shout(id)
    db = get_db()
    db.execute("DELETE FROM shout WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("shout.index"))
