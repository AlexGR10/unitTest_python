from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hola carlos tontin </p>"

if __name__ == "__main__":
    app.run(debug=True)


#base de datos 
from app import app,db

with app.app_context():
    db.create_all()
    print("Database created ready!")