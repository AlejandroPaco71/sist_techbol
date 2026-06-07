from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from app.extensions import db, bcrypt
from app.auth import auth_bp
from app.auth.models import User

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        user = User.query.filter_by(username=username).first()
        if user:
            flash("El nombre de usuario ya existe","danger")
            return redirect(url_for("auth.register"))
        
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        
        user = User(username=username, password=hashed_password)
        
        db.session.add(user)
        db.session.commit()
        flash("Usuario registrado corectamente","success")
        return redirect(url_for("auth.login"))
    #Qitamos el auth/
    return render_template("register.html")

@auth_bp.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash("Usuario logeado","success")
            return redirect(url_for("bp_core.dashboard"))
        
        flash("Usaurio o contrasena incorecta","danger")

    #quitamos el auth/
    return render_template("login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("bp_core.index"))