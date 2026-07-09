from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.models import User
from app.extensions import db


auth_bp = Blueprint("auth", __name__)

# ---------------- Home ---------------- #

@auth_bp.route("/")
def home():
    return "<h2>Backend is Working Successfully!</h2><br><a href='/register'>Register</a>"

# ---------------- Register ---------------- #

@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        full_name = request.form.get("full_name")

        email = request.form.get("email")

        password = request.form.get("password")

        # Check duplicate email
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:

            flash("Email already registered!")

            return redirect(url_for("auth.register"))

        hashed_password = generate_password_hash(password)

        user = User(
            full_name=full_name,
            email=email,
            password=hashed_password
        )

        db.session.add(user)

        db.session.commit()

        flash("Registration Successful!")

        return redirect(url_for("auth.login"))

    return render_template("register.html")

# ---------------- Login ---------------- #

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            login_user(user)

            flash("Login Successful!")

            return redirect(url_for("dashboard.dashboard"))

        flash("Invalid Email or Password")

        return redirect(url_for("auth.login"))

    return render_template("login.html")

# ---------------- Dashboard ---------------- #



@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    flash("Logged out successfully!")

    return redirect(url_for("auth.login"))