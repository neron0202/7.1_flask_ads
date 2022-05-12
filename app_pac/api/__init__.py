from flask import Blueprint

bp = Blueprint('api', __name__)

from app_pac.api import ads, users