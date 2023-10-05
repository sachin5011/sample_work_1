from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db  = SQLAlchemy(app)


with app.app_context():
    db.create_all()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        std = Student(name=name, email=email)
        db.session.add(std)
        db.session.commit()
    return render_template("./index.html")

@app.route("/about")
def about():
    return  "about page"


if __name__ == "__main__":
    app.run(debug=True)
