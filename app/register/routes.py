from typing import Union
from uuid import UUID

from flask import flash, redirect, render_template, request, url_for
from werkzeug import Response

from app import db
from app.models import Register
from app.register import bp
from app.register.forms import RegisterDeleteForm, RegisterForm


@bp.route("/", methods=["GET"])
def index() -> str:
    registers = db.session.execute(db.select(Register)).scalars().all()
    return render_template("register/list.html", registers=registers)


@bp.route("/new", methods=["GET", "POST"])
def create() -> Union[str, Response]:
    form = RegisterForm()

    if form.validate_on_submit():
        register = Register(name=form.name.data)
        db.session.add(register)
        db.session.commit()
        flash("Successfully created register", "success")
        return redirect(url_for("register.index"))

    return render_template("register/create.html", form=form)


@bp.route("/<uuid:id>", methods=["GET"])
def view(id: UUID) -> str:
    register = db.get_or_404(Register, id)
    return render_template("register/view.html", register=register)


@bp.route("/<uuid:id>/edit", methods=["GET", "POST"])
def edit(id: UUID) -> Union[str, Response]:
    register: Register = db.get_or_404(Register, id)
    form = RegisterForm()

    if request.method == "GET":
        form.name.data = register.name
    elif form.validate_on_submit():
        register.name = form.name.data
        db.session.commit()
        flash("Successfully edited register", "success")
        return redirect(url_for("register.index"))

    return render_template("register/edit.html", register=register, form=form)


@bp.route("/<uuid:id>/delete", methods=["GET", "POST"])
def delete(id: UUID) -> Union[str, Response]:
    register = db.get_or_404(Register, id)
    form = RegisterDeleteForm()

    if form.validate_on_submit():
        db.session.delete(register)
        db.session.commit()
        flash("Successfully deleted register", "success")
        return redirect(url_for("register.index"))

    return render_template("/register/delete.html", register=register, form=form)
