from flask import Blueprint, flash, redirect, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from app import db
from app.models import Staff

bp = Blueprint("auth", __name__)


def safe_next_url():
    # Only follow same-site paths, so ?next= can't bounce users to another site
    target = request.args.get("next", "")
    if target.startswith("/") and not target.startswith("//"):
        return target
    return "/"


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        staff = db.session.scalar(db.select(Staff).filter_by(username=username))

        if staff and staff.check_password(password):
            login_user(staff)
            return redirect(safe_next_url())

        flash("Invalid username or password.", "danger")

    # Placeholder until the login template is built
    return "Login page goes here."


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been signed out.", "info")
    return redirect(url_for("auth.login"))
