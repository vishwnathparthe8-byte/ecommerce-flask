from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import db, Users
from werkzeug.security import generate_password_hash, check_password_hash

# Define blueprint only once
users_bp = Blueprint("users", __name__, url_prefix="/users")

# -------- Register -------- #
@users_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])
        email = request.form["email"]
        role = request.form["role"]

        if Users.query.filter_by(Username=username).first():
            flash("Username already exists!", "danger")
            return redirect(url_for("users.register"))

        new_user = Users(Username=username, Password=password, Email=email, Role=role)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful. Please login.", "success")
        return redirect(url_for("users.login"))

    return render_template("users/register.html")

# -------- Login -------- #
@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = Users.query.filter_by(Username=username).first()
        if user and check_password_hash(user.Password, password):
            session["user_id"] = user.UserID
            session["username"] = user.Username
            session["role"] = user.Role
            flash("Login successful!", "success")
            return redirect(url_for("users.dashboard"))
        else:
            flash("Invalid credentials!", "danger")

    return render_template("users/login.html")

# -------- Dashboard -------- #
@users_bp.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Please login first!", "warning")
        return redirect(url_for("users.login"))
    return render_template("users/dashboard.html", role=session.get("role"))

# -------- View All Users (Admin only) -------- #
@users_bp.route("/all")
def view_users():
    if "user_id" not in session or session.get("role") != "Admin":
        flash("Only Admin can view users!", "danger")
        return redirect(url_for("users.dashboard"))

    users = Users.query.all()
    return render_template("users/users_list.html", users=users)


# -------- Delete User (Admin only) -------- #
@users_bp.route("/delete/<int:user_id>")
def delete_user(user_id):
    if "user_id" not in session or session.get("role") != "Admin":
        flash("Only Admin can delete users!", "danger")
        return redirect(url_for("users.dashboard"))

    user = Users.query.get_or_404(user_id)

    # Prevent deleting self
    if user.UserID == session["user_id"]:
        flash("You cannot delete yourself!", "warning")
        return redirect(url_for("users.view_users"))

    db.session.delete(user)
    db.session.commit()
    flash(f"User {user.Username} deleted successfully!", "success")
    return redirect(url_for("users.view_users"))


# -------- Logout -------- #
@users_bp.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully!", "success")
    return redirect(url_for("users.login"))