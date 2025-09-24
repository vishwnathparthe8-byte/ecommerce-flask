from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import db, Orders, Products
from datetime import datetime

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")

# -------- Place Order (Customer only) -------- #
@orders_bp.route("/place/<int:product_id>", methods=["GET", "POST"])
def place_order(product_id):
    if "user_id" not in session or session.get("role") != "Customer":
        flash("Please login as Customer to place order", "warning")
        return redirect(url_for("users.login"))

    product = Products.query.get_or_404(product_id)

    if request.method == "POST":
        quantity = int(request.form["quantity"])
        if quantity > product.Stock:
            flash("Not enough stock!", "danger")
            return redirect(url_for("orders.place_order", product_id=product_id))

        # Deduct stock
        product.Stock -= quantity

        # Create order
        new_order = Orders(
            UserID=session["user_id"],
            ProductID=product.ProductID,
            Quantity=quantity,
            OrderDate=datetime.utcnow()
        )
        db.session.add(new_order)
        db.session.commit()
        flash("Order placed successfully!", "success")
        return redirect(url_for("users.dashboard"))

    return render_template("orders/place_order.html", product=product)

# -------- View Orders -------- #
@orders_bp.route("/all")
def view_orders():
    if "user_id" not in session:
        flash("Please login first!", "warning")
        return redirect(url_for("users.login"))

    role = session.get("role")

    if role == "Admin":
        # Admin can see all orders
        orders = Orders.query.all()
    elif role == "Seller":
        # Seller can see orders for their products only
        orders = Orders.query.join(Products).filter(Products.SellerID==session["user_id"]).all()
    else:
        # Customer sees only their own orders
        orders = Orders.query.filter_by(UserID=session["user_id"]).all()

    return render_template("orders/orders_list.html", orders=orders, role=role)
@orders_bp.route("/cancel/<int:order_id>")
def cancel_order(order_id):
    if "user_id" not in session:
        flash("Please login first!", "warning")
        return redirect(url_for("users.login"))

    order = Orders.query.get_or_404(order_id)

    role = session.get("role")

    # Only the customer who placed it or Admin can cancel
    if role == "Customer" and order.UserID != session["user_id"]:
        flash("You can only cancel your own orders!", "danger")
        return redirect(url_for("orders.view_orders"))

    # Restore stock when cancelled
    product = Products.query.get(order.ProductID)
    if product:
        product.Stock += order.Quantity

    db.session.delete(order)
    db.session.commit()
    flash("Order cancelled successfully!", "success")
    return redirect(url_for("orders.view_orders"))
