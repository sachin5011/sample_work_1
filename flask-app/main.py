from flask import Flask
from dbconnection.sqlite_conn import db
from controller.home_page_controller import home
from controller.authentication import auth
from utils.password_encrypter import bcrypt

app = Flask(__name__)

app.secret_key = "mytestapp"

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///demo.db"

db.init_app(app)

bcrypt.init_app(app)


with app.app_context():
    db.create_all()



app.register_blueprint(home)
app.register_blueprint(auth)


if __name__ == "__main__":
    app.run(debug=True)

