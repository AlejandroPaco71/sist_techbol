from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.extensions import db, login_manager
from app.auth.models import User

#db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='templates')
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ventas.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # app.config['SECRET_KEY'] = 'tomas123'
    app.config.from_object("app.config.Config")
    
    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id)) 
    
    
    #1. Importacion del blueprint (Para cada modulo)
    from app.auth import auth_bp
    from app.core import bp_core

    # from app.core.routes import bp_core
    # from app.clientes.routes import bp_clientes
    # from app.productos.routes import bp_productos
    # from app.pedidos.routes import bp_pedidos

    #2. Registrar el blueprint (Para cada modulo)
    app.register_blueprint(bp_core)
    app.register_blueprint(auth_bp)
    # app.register_blueprint(bp_core, url_prefix='/')
    # app.register_blueprint(bp_clientes, url_prefix='/clientes')
    # app.register_blueprint(bp_productos, url_prefix='/productos')
    # app.register_blueprint(bp_pedidos, url_prefix='/pedidos')
    

    
    return app
    