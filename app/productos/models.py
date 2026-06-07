    
from app.app import db

class Producto(db.Model):
    __tablename__ = "productos"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    
    # Relación: un Producto puede estar en muchos Pedidos
    pedidos = db.relationship('Pedido', backref='producto', lazy=True, cascade="all, delete-orphan")

    
    def __repr__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio} - Stock: {self.stock}"
    

    