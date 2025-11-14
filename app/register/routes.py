"""
Blueprint: Register management (list, create, view, edit, delete)

This module defines the route handlers (also called "view functions")
for working with `Register` records in the application. It follows a
typical CRUD pattern:

- index():   List all registers
- create():  Create a new register
- view():    Display a single register by ID
- edit():    Update an existing register
- delete():  Delete an existing register
"""

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
    """
    List all Register records.

    HTTP Method
    ----------
    - GET: Show the list of registers to the user

    Returns
    -------
    str
        The rendered HTML of the list page (Jinja template).
    """
    # `db.select(Register)` constructs a SQL SELECT query for the `Register` table.
    # `.scalars()` converts the result rows into model instances.
    # `.all()` loads all results into a Python list.
    registers = db.session.execute(db.select(Register)).scalars().all()

    # Render a Jinja template and inject the list of registers into it.
    return render_template("register/list.html", registers=registers)


@bp.route("/new", methods=["GET", "POST"])
def create() -> Union[str, Response]:
    """
    Create a new Register.

    HTTP Methods
    ------------
    - GET:  Show the blank form to the user.
    - POST: Validate and process the submitted form data.

    Returns
    -------
    Union[str, Response]
        - On GET or validation failure: Rendered HTML form page (str).
        - On successful creation: A redirect response back to the index page.
    """
    form = RegisterForm()

    # On POST + valid form data, persist a new Register record.
    if form.validate_on_submit():
        # Create a new Register instance from form data.
        register = Register(name=form.name.data)

        # Stage the new record for insert.
        db.session.add(register)
        # Commit actually writes to the database.
        db.session.commit()

        # Add a one-time success message to show in the next rendered page.
        flash("Successfully created register", "success")

        # Redirect to avoid form resubmission if user refreshes the page.
        return redirect(url_for("register.index"))

    # Either initial GET or POST with validation errors -> render the form.
    return render_template("register/create.html", form=form)


@bp.route("/<uuid:id>", methods=["GET"])
def view(id: UUID) -> str:
    """
    View a single Register by its UUID.

    Parameters
    ----------
    id : UUID
        The unique identifier of the Register to display.

    Returns
    -------
    str
        The rendered HTML of the detail page.
    """
    # Fetch the register or return a 404 response if it doesn't exist.
    register = db.get_or_404(Register, id)

    # Render the detail page for this specific register.
    return render_template("register/view.html", register=register)


@bp.route("/<uuid:id>/edit", methods=["GET", "POST"])
def edit(id: UUID) -> Union[str, Response]:
    """
    Edit an existing Register.

    HTTP Methods
    ------------
    - GET:  Pre-fill the form with existing register data for user to edit.
    - POST: Validate and update the register if the form data is valid.

    Parameters
    ----------
    id : UUID
        The unique identifier of the Register to edit.

    Returns
    -------
    Union[str, Response]
        - On GET or invalid POST: The rendered edit form (str).
        - On success: A redirect response back to the index page.
    """
    # Retrieve the register to edit or 404 if it doesn't exist.
    register: Register = db.get_or_404(Register, id)
    form = RegisterForm()

    if request.method == "GET":
        # Pre-populate the form fields so the user sees the current values.
        form.name.data = register.name
    elif form.validate_on_submit():
        # Copy validated form data into the model instance.
        register.name = form.name.data

        # Persist the changes to the database.
        db.session.commit()

        flash("Successfully edited register", "success")
        return redirect(url_for("register.index"))

    # Either initial GET or POST with validation errors -> render the form.
    return render_template("register/edit.html", register=register, form=form)


@bp.route("/<uuid:id>/delete", methods=["GET", "POST"])
def delete(id: UUID) -> Union[str, Response]:
    """
    Delete an existing Register.

    HTTP Methods
    ------------
    - GET:  Show a confirmation page (to prevent accidental deletions).
    - POST: Validate the confirmation and perform the deletion.

    Parameters
    ----------
    id : UUID
        The unique identifier of the Register to delete.

    Returns
    -------
    Union[str, Response]
        - On GET or invalid POST: Rendered confirmation page (str).
        - On success: A redirect response back to the index page.
    """
    # Load the target register or show a 404 if not found.
    register = db.get_or_404(Register, id)

    form = RegisterDeleteForm()

    if form.validate_on_submit():
        # Mark the object for deletion and commit to persist the change.
        db.session.delete(register)
        db.session.commit()

        flash("Successfully deleted register", "success")
        return redirect(url_for("register.index"))

    # Either initial GET or POST with validation errors -> render the form.
    return render_template("register/delete.html", register=register, form=form)