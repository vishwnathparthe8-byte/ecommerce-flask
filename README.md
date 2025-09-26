<H1>📦E-commerce Flask App<H1>

<H5>A simple E-commerce web application built with Flask, SQLAlchemy, and SQLite.
This project demonstrates user authentication, role-based access (Admin, Seller, Customer), and basic product/order management.<H5>

<H1>🚀 Features<H1>
<H2>👤 User Roles<H2>
<H5>Admin: Manage everything (users, products, orders).<H5>
<H5>Seller: Add/delete their own products, view orders for their products.<H5>
<H5>Customer: Browse products, place orders, cancel their own orders.<H5>

<H2>🛍 Product Management<H2>
<H5>View all products.<H5>
<H5>Add new products (Seller only).<H5>
<H5>Delete products (Seller → only own, Admin → all).<H5>

<H2>📦 Order Management<H2>
<H5>Place orders (Customer only).<H5>
<H5>View orders:<H5>
<H5>Admin → all orders<H5>
<H5>Seller → orders for their products<H5>
<H5>Customer → their own orders<H5>
<H5>Cancel orders (Customer for own / Admin for all).<H5>

<H2>🔐 Authentication<H2>
<H5>Secure password hashing (werkzeug.security).<H5>
<H5>Session-based login with role-based permissions.<H5>

<H2>📂 Project Structure<H2>

<H5>ecommerce-flask/<H5>
<H5>│── app.py                # Main entry point (creates app)<H5>
<H5>│── models.py             # Database models<H5>
<H5>│── routes/
    │   ├── users.py          # User routes (login, register, dashboard)
    │   ├── products.py       # Product routes
    │   └── orders.py         # Order routes<H5>
<H5>│── templates/<H5>
<H5>│   ├── users/            # HTML files for users<H5>
<H5>│   ├── products/         # HTML files for products<H5>
<H5>│   └── orders/           # HTML files for orders<H5>
<H5>│── static/               # CSS, JS, images<H5>
<H5>│── init_admin.py         # Script to create default admin<H5>
<H5>│── requirements.txt      # Dependencies<H5>
<H5>│── README.md             # Project documentation<H5>

