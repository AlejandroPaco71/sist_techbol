    
from flask import render_template
from flask_login import login_required
from app.core import bp_core

@bp_core.route("/")
def index():
    return render_template('index.html')

@bp_core.route("/dashboard")
@login_required
def dashboard():
    #Quite a ambos el core/ por que no tengo esa carpeta dentro de templates
    return render_template("dashboard.html")