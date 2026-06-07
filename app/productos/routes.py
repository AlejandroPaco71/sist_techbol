from flask import request, render_template, redirect, url_for, Blueprint, flash
from app.app import db
from app.productos.models import Producto

bp_productos = Blueprint('bp_productos', __name__, template_folder='templates')

@bp_productos.route("/")
def index():
    productos = Producto.query.all()
    return render_template('productos/index.html', productos=productos)

@bp_productos.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('productos/create.html')
    elif request.method == 'POST':
        nombre = request.form.get('nombre')
        precio = float(request.form.get('precio'))
        stock = int(request.form.get('stock'))
        producto = Producto(nombre=nombre, precio=precio, stock=stock)
        db.session.add(producto)
        db.session.commit()
        flash('Producto registrado exitosamente', 'success')
        return redirect(url_for('bp_productos.index'))

@bp_productos.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        stock = int(request.form['stock'])
        producto = Producto.query.get(id)
        producto.nombre = nombre
        producto.precio = precio
        producto.stock = stock
        db.session.commit()
        flash('Producto actualizado exitosamente', 'success')
        return redirect(url_for('bp_productos.index'))
    
    producto = Producto.query.get(id)
    return render_template("productos/edit.html", producto=producto)

@bp_productos.route("/delete/<int:id>")
def delete(id):
    producto = Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    flash('Producto eliminado exitosamente', 'success')
    return redirect(url_for("bp_productos.index"))