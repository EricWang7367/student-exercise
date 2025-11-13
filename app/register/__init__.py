from flask import Blueprint

bp: Blueprint = Blueprint("register", __name__, url_prefix="/registers")

from app.register import routes  # noqa: E402,F401
