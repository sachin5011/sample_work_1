from flask import Blueprint, render_template, request, redirect, session
from utils.password_encrypter import passwordencriptor, decryptpassword
from dbconnection.sqlite_conn import db
from models.models import User


auth = Blueprint("auth", __name__)

@auth.route("/user/registration", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        f_name = request.form.get("f-name")
        l_name = request.form.get("l-name")
        email = request.form.get("email")
        password = request.form.get("pwd")
        conf_password = request.form.get("conf-pwd")
        
        if password == conf_password:
            user = User.query.filter_by(email=email).first()
            if user:
                return render_template("./registration.html")
            else:
                user = User(first_name=f_name, last_name=l_name, email=email, password=passwordencriptor(password))
        db.session.add(user)
        db.session.commit()

        return redirect("/user/login")
    return render_template("./registration.html")


@auth.route("/user/login", methods=["GET", "POST"])
def userlogin():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("pwd")

        user = User.query.filter_by(email=email).first()

        if user is None:
            return redirect("/user/registration")
        
        if decryptpassword(user.password, password):
            session["user_id"] = user.id
            session["user"] = user.first_name
            
            print("Login Successful.....")
            return redirect("/")
        
    return render_template("./login.html")


@auth.route("/user/logout")
def userlogout():
    session.pop("user", None)
    return redirect("/")