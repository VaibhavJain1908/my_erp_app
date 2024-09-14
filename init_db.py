from app import app, db

with app.app_context():
    db.drop_all()   # Optional: Use this if you want to drop existing tables before creating new ones
    db.create_all()

def init_db():
    with app.app_context():
        db.create_all()
        print("Database initialized successfully!")

if __name__ == '__main__':
    init_db()
