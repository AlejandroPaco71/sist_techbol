from app.app import db
from datetime import datetime

class Pedido(db.Model):
    __tablename__ = "pedidos"
    
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    monto = db.Column(db.Float, nullable=False)
    
    # Llaves foráneas (relaciones muchos-a-uno)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    

    
    def __repr__(self):
        return f"Pedido #{self.id} - Fecha: {self.fecha} - Monto: {self.monto}"