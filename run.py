from app import create_app,db
from app.models import Student
app = create_app()
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)