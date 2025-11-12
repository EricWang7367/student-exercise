from flask import render_template
from app.register import bp


@bp.route("/", methods=["GET"])
def index() -> str:
    return render_template("list_registers.html")


@bp.route("/new", methods=["GET", "POST"])
def create() -> str:
    return render_template("create_register.html")
