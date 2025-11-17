from flask import Blueprint

bp: Blueprint = Blueprint("entry", __name__, url_prefix="/<uuid:register_id>/entries")

from app.entry import routes  # noqa: E402,F401
