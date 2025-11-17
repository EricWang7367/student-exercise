"""
Entry Blueprint Package

This module creates the Flask blueprint for all routes that deal with
`Entry` objects, which always belong to a specific `Register`.

Key Concepts for Students:
1. Nested Blueprints:
   - In this app, `Entry` routes are "nested" under `Register` routes.
   - The parent blueprint (`register`) handles URLs starting with `/registers`.
   - This blueprint only handles the part after the register ID: `/<register_id>/entries`.

2. URL Parameters:
   - `<uuid:register_id>` in the URL ensures:
       * Only valid UUIDs are accepted for the register ID.
       * Flask automatically converts the URL part to a Python `UUID` object.
   - Each route in this blueprint will receive `register_id` as a function argument.

3. Endpoint Naming:
   - When this blueprint is nested under `register_bp`, Flask combines
     the names:
       parent_name.child_name.view_function_name
   - Example: `register.entry.index` for listing entries of a register.

4. Importing Routes:
   - The import statement at the bottom ensures the routes have access
     to this `bp` object.
   - It is placed after the blueprint is created to prevent circular imports.
"""

from flask import Blueprint

# Create the blueprint for Entry routes
#
# - "entry" is the internal name of the blueprint.
# - __name__ allows Flask to find templates and static files.
# - url_prefix defines the URL path that all routes in this blueprint
#   will start with, *relative to the parent blueprint*.
#
# Example full URLs after nesting under register_bp:
#   /registers/<register_id>/entries/         -> list entries
#   /registers/<register_id>/entries/new     -> create entry
#   /registers/<register_id>/entries/<entry_id> -> view/edit/delete entry
bp: Blueprint = Blueprint("entry", __name__, url_prefix="/<uuid:register_id>/entries")

# Import routes after blueprint creation
#
# This pattern avoids circular import errors because routes need
# access to the bp object.
# The "# noqa" comments disable linting warnings about import order
# (E402) or unused imports (F401).
from app.entry import routes  # noqa: E402,F401
