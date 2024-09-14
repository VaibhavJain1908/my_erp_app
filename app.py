from flask import Flask, render_template, request, redirect, url_for
from models import app, db, Inventory, Sales, Employee, Supplier, SupportTicket
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inventory')
def inventory():
    items = Inventory.query.all()
    return render_template('inventory.html', items=items)

@app.route('/inventory/add', methods=['POST'])
def add_inventory():
    item_name = request.form.get('itemName')
    quantity = request.form.get('itemQuantity')
    price = request.form.get('itemPrice')
    supplier_id = request.form.get('supplierId')  # Assuming supplier_id is optional
    
    if item_name and quantity and price:
        quantity = int(quantity)
        price = float(price)
        new_item = Inventory(item_name=item_name, quantity=quantity, price=price, supplier_id=supplier_id)
        db.session.add(new_item)
        try:
            db.session.commit()
            return redirect(url_for('inventory'))
        except Exception as e:
            db.session.rollback()
            return str(e)
    else:
        return "All fields are required."

@app.route('/sales')
def sales():
    records = Sales.query.all()
    return render_template('sales.html', records=records)

@app.route('/sales/add', methods=['POST'])
def add_sales():
    item_name = request.form.get('productName')
    quantity = request.form.get('saleQuantity')
    total_price = request.form.get('salePrice')
    sale_date = request.form.get('saleDate')  # Ensure format is correct
    
    if item_name and quantity and total_price and sale_date:
        quantity = int(quantity)
        total_price = float(total_price)
        sale_date = datetime.strptime(sale_date, '%Y-%m-%d')  # Adjust format as needed
        new_sale = Sales(item_name=item_name, quantity=quantity, total_price=total_price, sale_date=sale_date)
        db.session.add(new_sale)
        try:
            db.session.commit()
            return redirect(url_for('sales'))
        except Exception as e:
            db.session.rollback()
            return str(e)
    else:
        return "All fields are required."

@app.route('/employees')
def employees():
    records = Employee.query.all()
    return render_template('employees.html', records=records)

@app.route('/employees/add', methods=['POST'])
def add_employee():
    employee_name = request.form.get('employeeName')
    position = request.form.get('employeePosition')
    salary = request.form.get('employeeSalary')
    
    if employee_name and position and salary:
        salary = float(salary)
        new_employee = Employee(employee_name=employee_name, position=position, salary=salary)
        db.session.add(new_employee)
        try:
            db.session.commit()
            return redirect(url_for('employees'))
        except Exception as e:
            db.session.rollback()
            return str(e)
    else:
        return "All fields are required."

@app.route('/suppliers')
def suppliers():
    records = Supplier.query.all()
    return render_template('suppliers.html', records=records)

@app.route('/suppliers/add', methods=['POST'])
def add_supplier():
    supplier_name = request.form.get('supplierName')
    contact_info = request.form.get('supplierContact')
    address = request.form.get('supplierAddress')
    
    if supplier_name and contact_info and address:
        new_supplier = Supplier(supplier_name=supplier_name, contact_info=contact_info, address=address)
        db.session.add(new_supplier)
        try:
            db.session.commit()
            return redirect(url_for('suppliers'))
        except Exception as e:
            db.session.rollback()
            return str(e)
    else:
        return "All fields are required."

@app.route('/support')
def support():
    tickets = SupportTicket.query.all()
    return render_template('support.html', tickets=tickets)

@app.route('/support/add', methods=['POST'])
def add_support_ticket():
    title = request.form.get('ticketTitle')
    description = request.form.get('ticketDescription')
    priority = request.form.get('ticketPriority')
    
    if title and description and priority:
        new_ticket = SupportTicket(title=title, description=description, priority=priority)
        db.session.add(new_ticket)
        try:
            db.session.commit()
            return redirect(url_for('support'))
        except Exception as e:
            db.session.rollback()
            return str(e)
    else:
        return "All fields are required."
    
@app.route('/inventory/delete/<int:id>', methods=['POST'])
def delete_inventory(id):
    item = Inventory.query.get(id)
    if item:
        db.session.delete(item)
        try:
            db.session.commit()
            return redirect(url_for('inventory'))
        except Exception as e:
            db.session.rollback()
            return str(e)
    return "Item not found."

@app.route('/sales/delete/<int:id>', methods=['POST'])
def delete_sales(id):
    sale = Sales.query.get(id)
    if sale:
        db.session.delete(sale)
        try:
            db.session.commit()
            return redirect(url_for('sales'))
        except Exception as e:
            db.session.rollback()
            return str(e)
    return "Sale not found."

@app.route('/employees/delete/<int:id>', methods=['POST'])
def delete_employee(id):
    employee = Employee.query.get(id)
    if employee:
        db.session.delete(employee)
        try:
            db.session.commit()
            return redirect(url_for('employees'))
        except Exception as e:
            db.session.rollback()
            return str(e)
    return "Employee not found."

@app.route('/suppliers/delete/<int:id>', methods=['POST'])
def delete_supplier(id):
    supplier = Supplier.query.get(id)
    if supplier:
        db.session.delete(supplier)
        try:
            db.session.commit()
            return redirect(url_for('suppliers'))
        except Exception as e:
            db.session.rollback()
            return str(e)
    return "Supplier not found."

@app.route('/support/delete/<int:id>', methods=['POST'])
def delete_support_ticket(id):
    ticket = SupportTicket.query.get(id)
    if ticket:
        db.session.delete(ticket)
        try:
            db.session.commit()
            return redirect(url_for('support'))
        except Exception as e:
            db.session.rollback()
            return str(e)
    return "Ticket not found."

if __name__ == '__main__':
    app.run(debug=True)
