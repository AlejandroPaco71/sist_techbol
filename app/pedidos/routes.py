from flask import request, render_template, redirect, url_for, Blueprint, flash
from datetime import datetime
from app.app import db
from app.pedidos.models import Pedido
from app.clientes.models import Cliente
from app.productos.models import Producto

bp_pedidos = Blueprint('bp_pedidos', __name__, template_folder='templates')

@bp_pedidos.route("/")
def index():
    pedidos = Pedido.query.all()
    return render_template('pedidos/index.html', pedidos=pedidos)

@bp_pedidos.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        clientes = Cliente.query.all()
        productos = Producto.query.all()
        return render_template('pedidos/create.html', clientes=clientes, productos=productos)
    elif request.method == 'POST':
        cliente_id = int(request.form.get('cliente_id'))
        producto_id = int(request.form.get('producto_id'))
        monto = float(request.form.get('monto'))
        fecha_str = request.form['fecha']
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
        pedido = Pedido(cliente_id=cliente_id, producto_id=producto_id, monto=monto, fecha=fecha)
        db.session.add(pedido)
        db.session.commit()
        flash('Pedido registrado exitosamente', 'success')
        return redirect(url_for('bp_pedidos.index'))

@bp_pedidos.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        cliente_id = int(request.form['cliente_id'])
        producto_id = int(request.form['producto_id'])
        monto = float(request.form['monto'])
        pedido = Pedido.query.get(id)
        pedido.cliente_id = cliente_id
        pedido.producto_id = producto_id
        pedido.monto = monto
        db.session.commit()
        flash('Pedido actualizado exitosamente', 'success')
        return redirect(url_for('bp_pedidos.index'))
    
    pedido = Pedido.query.get(id)
    clientes = Cliente.query.all()
    productos = Producto.query.all()
    return render_template("pedidos/edit.html", pedido=pedido, clientes=clientes, productos=productos)

@bp_pedidos.route("/delete/<int:id>")
def delete(id):
    pedido = Pedido.query.get(id)
    db.session.delete(pedido)
    db.session.commit()
    flash('Pedido eliminado exitosamente', 'success')
    return redirect(url_for("bp_pedidos.index"))