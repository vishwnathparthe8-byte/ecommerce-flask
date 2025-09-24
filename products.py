from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import db, Products
from datetime import datetime

products_bp = Blueprint("products", __name__, url_prefix="/products")

# -------- View Products -------- #
@products_bp.route("/")
def view_products():
    products = Products.query.all()
    return render_template("products/products.html", products=products)

# -------- Add Product (Seller) -------- #
@products_bp.route("/add", methods=["POST"])
def add_product():
    if "user_id" not in session or session.get("role") != "Seller":
        flash("Please login as Seller to add product", "warning")
        return redirect(url_for("users.login"))

    name = request.form["name"]
    price = float(request.form["price"])
    stock = int(request.form["stock"])

    new_product = Products(
        Name=name,
        Price=price,
        Stock=stock,
        SellerID=session["user_id"]
    )
    db.session.add(new_product)
    db.session.commit()
    flash(f"Product '{name}' added successfully!", "success")
    return redirect(url_for("products.view_products"))

# -------- Delete Product (Seller/Admin) -------- #
@products_bp.route("/delete/<int:product_id>")
def delete_product(product_id):
    if "user_id" not in session:
        flash("Please login first!", "warning")
        return redirect(url_for("users.login"))

    product = Products.query.get_or_404(product_id)

    if session.get("role") not in ["Seller", "Admin"]:
        flash("You are not authorized to delete product", "danger")
        return redirect(url_for("products.view_products"))

    # Only the seller who added it or Admin can delete
    if session.get("role") == "Seller" and product.SellerID != session["user_id"]:
        flash("You can only delete your own products!", "danger")
        return redirect(url_for("products.view_products"))

    db.session.delete(product)
    db.session.commit()
    flash(f"Product '{product.Name}' deleted successfully!", "success")
    return redirect(url_for("products.view_products"))