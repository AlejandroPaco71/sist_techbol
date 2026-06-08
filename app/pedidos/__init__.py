from flask import Blueprint

bp_pedidos = Blueprint('bp_pedidos', __name__, template_folder='templates', url_prefix="/pedidos")

from app.pedidos import routes