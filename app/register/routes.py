from typing import Union

from flask import flash, redirect, render_template, url_for
from werkzeug import Response

from app import db
from app.models import Register
from app.register import bp
from app.register.forms import RegisterForm


@bp.route("/", methods=["GET"])
def index() -> str:
    registers = db.session.execute(db.select(Register)).scalars().all()
    return render_template("register/list.html", registers=registers)


@bp.route("/new", methods=["GET", "POST"])
def create() -> Union[str, Response]:
    form = RegisterForm()

    if form.validate_on_submit():
        new_register = Register(name=form.name.data)
        db.session.add(new_register)
        db.session.commit()
        flash("TEMP HELLO WORLD")
        return redirect(url_for("register.index"))

    return render_template("register/create.html", form=form)
