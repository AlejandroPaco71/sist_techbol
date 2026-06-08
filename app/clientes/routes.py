
from flask import request, render_template, redirect, url_for, flash
from flask_login import login_required
# Referencia a la base de datos
from app.extensions import db
# Modelos con los que interactura el modulo
from app.clientes.models import Cliente
from app.clientes import bp_clientes


#bp_clientes = Blueprint('bp_clientes', __name__, template_folder='templates')

@bp_clientes.route("/")
@login_required
def index():
    clientes = Cliente.query.all()
    return render_template('clientes/index.html', clientes=clientes)

@bp_clientes.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'GET':
        return render_template('clientes/create.html')
    elif request.method == 'POST':
        nombre = request.form.get('nombre')
        telefono = request.form.get('telefono')
        cliente = Cliente(nombre=nombre, telefono=telefono)
        db.session.add(cliente)
        db.session.commit()
        flash('Cliente registrado exitosamente', 'success')
        return redirect(url_for('bp_clientes.index'))

@bp_clientes.route("/edit/<int:id>", methods=['GET', 'POST'])
@login_required
def edit(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        cliente = Cliente.query.get(id)
        cliente.nombre = nombre
        cliente.telefono = telefono
        db.session.commit()
        flash('Cliente actualizado exitosamente', 'success')
        return redirect(url_for('bp_clientes.index'))
    
    cliente = Cliente.query.get(id)
    return render_template("clientes/edit.html", cliente=cliente)

@bp_clientes.route("/delete/<int:id>")
@login_required
def delete(id):
    cliente = Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    flash('Cliente eliminado exitosamente', 'success')
    return redirect(url_for("bp_clientes.index"))
        
    

    
 
