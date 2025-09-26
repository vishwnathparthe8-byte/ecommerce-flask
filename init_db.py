from app import create_app
from models import db, Users
from werkzeug.security import generate_password_hash

app = create_app()
app.app_context().push()

db.create_all()

# Create default admin
if not Users.query.filter_by(Username='admin').first():
    admin = Users(
        Username='admin',
        Password=generate_password_hash('admin123'),
        Email='admin@example.com',
        Role='Admin'
    )
    db.session.add(admin)
    db.session.commit()
    print("Created default admin -> username: admin password: admin123")
else:
    print("Admin already exists")