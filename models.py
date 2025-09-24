from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# ---------------- Users ---------------- #
class Users(db.Model):
    __tablename__ = "Users"
    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Username = db.Column(db.String(50), unique=True, nullable=False)
    Password = db.Column(db.String(200), nullable=False)
    Email = db.Column(db.String(100), nullable=True)
    Role = db.Column(db.String(20), nullable=False)  # Admin, Seller, Customer

    # Relationships
    products = db.relationship('Products', backref='seller', lazy=True)
    orders = db.relationship('Orders', backref='user', lazy=True)


# ---------------- Products ---------------- #
class Products(db.Model):
    __tablename__ = "Products"
    ProductID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Price = db.Column(db.Float, nullable=False)
    Stock = db.Column(db.Integer, nullable=False)
    SellerID = db.Column(db.Integer, db.ForeignKey('Users.UserID'), nullable=False)

    # Relationship to orders
    orders = db.relationship('Orders', backref='product', lazy=True)


# ---------------- Orders ---------------- #
class Orders(db.Model):
    __tablename__ = "Orders"
    OrderID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'), nullable=False)
    ProductID = db.Column(db.Integer, db.ForeignKey('Products.ProductID'), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    OrderDate = db.Column(db.DateTime, default=datetime.utcnow)  # default to current datetime