"""HTTP routes for the monitoring demo UI (Phase 0 placeholders)."""

from flask import Blueprint, render_template

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    return render_template("home.html")


@bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@bp.route("/servers/<hostname>")
def server_detail(hostname: str):
    # hostname is escaped by Jinja when rendered — do not mark it safe
    return render_template("server_detail.html", hostname=hostname)


@bp.route("/servers")
def manage_servers():
    return render_template("manage_servers.html")
