from flask import render_template

from app.register import bp
from app.register.forms import RegisterForm


@bp.route("/", methods=["GET"])
def index() -> str:
    return render_template("register/list.html")


@bp.route("/new", methods=["GET", "POST"])
def create() -> str:
    form = RegisterForm()
    return render_template("register/create.html", form=form)
