from flask import render_template

from app.register import bp
from app.register.forms import RegisterForm

from app.models import Register
from app import db


@bp.route("/", methods=["GET"])
def index() -> str:
    return render_template("register/list.html")


@bp.route("/new", methods=["GET", "POST"])
def create() -> str:
    form = RegisterForm()

    if form.validate_on_submit():
        new_register = Register(name=form.name.data)
        db.session.add(new_register)
        db.session.commit()

    return render_template("register/create.html", form=form)
