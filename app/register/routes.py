
from flask import (
    render_template
)

from app.register import bp


@bp.route("/registers", methods=["GET"])
def index() -> str:
    """Render the index page."""
    return render_template("list_register.html")
