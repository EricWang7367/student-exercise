from flask import render_template, redirect, url_for, flash
from app.register import bp
from app.register.forms import RegisterForm

from app.models import Register
from app import db


@bp.route("/", methods=["GET"])
def index() -> str:
    registers = db.session.execute(db.select(Register)).scalars().all()
    return render_template("register/list.html", registers=registers)


@bp.route("/new", methods=["GET", "POST"])
def create() -> str:
    form = RegisterForm()

    if form.validate_on_submit():
        new_register = Register(name=form.name.data)
        db.session.add(new_register)
        db.session.commit()
        flash("TEMP HELLO WORLD")
        return redirect(url_for("register.index"))

    return render_template("register/create.html", form=form)
