<H1>📦E-commerce Flask App<H1>

<H5>A simple E-commerce web application built with Flask, SQLAlchemy, and SQLite.
This project demonstrates user authentication, role-based access (Admin, Seller, Customer), and basic product/order management.<H5>

<H1>🚀 Features<H1>

👤 User Roles

Admin: Manage everything (users, products, orders).

Seller: Add/delete their own products, view orders for their products.

Customer: Browse products, place orders, cancel their own orders.

🛍 Product Management

View all products.

Add new products (Seller only).

Delete products (Seller → only own, Admin → all).

📦 Order Management

Place orders (Customer only).

View orders:

Admin → all orders

Seller → orders for their products

Customer → their own orders

Cancel orders (Customer for own / Admin for all).

🔐 Authentication

Secure password hashing (werkzeug.security).

Session-based login with role-based permissions.
