
from flask import Blueprint

bp_productos = Blueprint('bp_productos', __name__, template_folder='templates', url_prefix="/productos")

from app.productos import routes