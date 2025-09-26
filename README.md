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


# 📂 Project Structure

```text
ecommerce-flask/
│── app.py                # Main entry point (creates app)
│── models.py             # Database models
│── routes/
│   ├── users.py          # User routes (login, register, dashboard)
│   ├── products.py       # Product routes
│   └── orders.py         # Order routes
│── templates/
│   ├── users/            # HTML files for users
│   ├── products/         # HTML files for products
│   └── orders/           # HTML files for orders
│── static/               # CSS, JS, images
│── init_admin.py         # Script to create default admin
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
```


<H2>Clone the repo<H2>

<H5>git clone https://github.com/yourusername/ecommerce-flask.git
cd ecommerce-flask<H5>


<H2>Create virtual environment<H2>

<H5>python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows<H5>


<H2>Install dependencies<H2>

<H5>pip install -r requirements.txt<H5>


<H2>Initialize the database<H2>

<H5>python init_admin.py<H5>


<H2>This will create the tables and add a default admin:<H2>

<H5>Username: admin
Password: admin123<H5>


<H2>Run the app<H2>

<H5>flask run<H5>


<H5>App will run at: http://127.0.0.1:5000<H5>
