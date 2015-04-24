from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models.auth import Permission


@main.app_context_processor
def inject_permisssions():
    return dict(Permission=Permission)
