from flask import Flask
from connections.sqlite import db
from controllers.student_controller import std


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///student.db"



db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(std)

if __name__ == "__main__":
    app.run(debug=True)