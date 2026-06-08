from flask import Blueprint

bp_clientes = Blueprint('bp_clientes', __name__, template_folder='templates', url_prefix="/clientes")

from app.clientes import routes

