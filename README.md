Mini E-Commerce Flask Project
Project Overview
simple e-commerce web application built using Flask and Flask-SQLAlchemy. It allows users to register, login, browse products, place orders, and view order history. Admins can manage all orders and users.

Setup Instructions
Clone this repository:
git clone <your-github-repo-link>
Create a virtual environment:
python -m venv venv
Activate the virtual environment:
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt
Run the application:
python app.py
Open http://127.0.0.1:5000 in your browser.
Database Schema
Table	Columns	Relationships
Users	UserID, Username, Password, Email, Role	One-to-Many: Products (seller), Orders (customer)
Products	ProductID, Name, Price, Stock, SellerID	One-to-Many: Orders (product)
Orders	OrderID, UserID, ProductID, Quantity, OrderDate, Status	Many-to-One: User, Product
Features
User registration and login
Product listing with stock management
Place orders with quantity validation
View order history
Cancel orders (for Admin and Customer)
Role-based access control (Admin, Customer, Seller)
Features by Role
Admin: View all orders, cancel any order, manage users
Customer: Browse products, place order, view and cancel own orders
Seller: Manage own products (view, add, update)
Future Improvements
Integrate payment gateway (e.g., Stripe, PayPal)
Add product search and filter functionality
Improve UI with Bootstrap or Tailwind CSS
Email notifications for order placement/cancellation
Admin dashboard with analytics
User profile update options
File Structure

Raj_Mart/
│
├── app.py                  # Main Flask app
├── models.py               # SQLAlchemy database models
├── requirements.txt        # Python dependencies
├── README.html             # This README file
│
├── static/                 # Static files
│   ├── css/
│      └── style.css
│   
│       
│
├── templates/              # HTML templates
│   ├── base.html
│   ├── users/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── dashboard.html
│   ├── products/
│   │   └── products_list.html
│   └── orders/
│       └── orders_list.html
│
├── routes/                 # Blueprint routes
│   ├── users.py
│   ├── products.py
│   └── orders.py
│
└── instance/               # Optional: SQLite DB
    └── vegas-mart
    
GitHub Repository
