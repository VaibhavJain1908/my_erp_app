from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///erp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(255), nullable=False)
    party_name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    style_number = db.Column(db.Float, nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=True)
    supplier = db.relationship('Supplier', back_populates='inventory')

class ProductStage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
    stage = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    product = db.relationship('Inventory', backref='stages')

    def __init__(self, product_id, stage, quantity):
        self.product_id = product_id
        self.stage = stage
        self.quantity = quantity

class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    sale_date = db.Column(db.DateTime, nullable=False)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(255), nullable=False)
    position = db.Column(db.String(255), nullable=False)
    salary = db.Column(db.Float, nullable=False)

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(255), nullable=False)
    contact_info = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    inventory = db.relationship('Inventory', back_populates='supplier')

class SupportTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), default='Open')

with app.app_context():
    db.create_all()
