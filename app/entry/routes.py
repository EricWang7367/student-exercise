"""
Blueprint: Entry management (list, create, view, edit, delete)

This module defines the route handlers (also called "view functions")
for working with `Entry` records in the application. It follows a
typical CRUD pattern:

- index():   List all entries in a specific register
- create():  Create a new entry in a specific register
- view():    Display a single entry by ID in a specific register
- edit():    Update an existing entry in a specific register
- delete():  Delete an existing entry in a specific register
"""

from uuid import UUID

from app.entry import bp


@bp.route("/", methods=["GET"])
def index(register_id: UUID) -> str:
    pass
