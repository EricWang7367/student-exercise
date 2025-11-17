"""
Register Blueprint Package

This module creates the Flask blueprint for all routes that deal with
`Register` objects. A blueprint in Flask acts like a modular "section" of
the application: it groups related routes, templates, and static files
together.

By placing the blueprint creation in this file and importing the route
definitions at the bottom, we ensure that:

1. The blueprint exists before routes try to attach themselves to it.
2. We avoid circular import problems (common in Flask apps).
3. The `register` package can be imported cleanly elsewhere in the app.

Other modules (such as `app.register.routes`) will use this `bp` object
to add URL routes that belong to the "register" part of the application.
"""

from flask import Blueprint

from app.entry import bp as entry_bp

# Create a blueprint named "register".
#
# - The first argument ("register") is the internal name of the blueprint.
# - `__name__` helps Flask locate related templates and static files.
# - `url_prefix="/registers"` means every route attached to this blueprint
#   will begin with /registers in its URL.
#
#   For example:
#     @bp.route("/")
#   becomes:
#     /registers/
#
bp: Blueprint = Blueprint("register", __name__, url_prefix="/registers")

# Nest the Entry blueprint under the Register blueprint
bp.register_blueprint(entry_bp)

# Import routes AFTER the blueprint is created.
#
# This pattern prevents circular imports because the routes module expects
# `bp` to already exist when it is imported.
#
# The "# noqa" comments disable certain formatting/linting warnings about
# import order (E402) or unused imports (F401).
from app.register import routes  # noqa: E402,F401
