from flask import Blueprint, request, render_template, session
from models.models import Blog, User, Profile, Contact
from datetime import datetime
from dbconnection.sqlite_conn import db


home = Blueprint("home", __name__)

@home.route("/", methods=["GET"])
def home_page():
    blog = Blog.query.join(User, Blog.author_id==User.id).add_columns(User.id, User.first_name, User.last_name, Blog.id, Blog.title, Blog.category) 
    return render_template("./index.html", bolg = blog)

@home.route("/test")
def test_page():
    data = ["Jhon", "Carl", "Samantha", "Rose"]
    return render_template("./test.html", data=data)

@home.route("/home/category")
def category():
    return render_template("./category.html")

@home.route("/home/archive")
def archive():
    return render_template("./archive.html")

@home.route("/home/blog-post", methods=["GET", "POST"])
def blog():
    # user = session["user"]
    blog = Blog.query.all()
    return render_template("./single-blog.html", blog=blog)

@home.route("/home/add-blog-post", methods=["GET", "POST"])
def addblog():
    if request.method == "POST": 
        title = request.form.get("title")
        content = request.form.get("body")
        category = request.form.get("cat")
        posted_at = datetime.now()
        image = request.files["img"]
        unique_name = str(datetime.now().timestamp()).replace(".","")
        file_path = f"./media/{unique_name}_{image.filename}"
        image.save(file_path)  
        # print(title, content, category, posted_at, file_path)
        author = session["user_id"]
        print(author)
        blog = Blog(author_id=author, title=title, body=content, category=category, posted_at=posted_at, images=file_path)
        db.session.add(blog)
        db.session.commit()
    return render_template("./post-blog.html")


@home.route('/home/blog-post/blog-detail')
def blogdetail():
    return render_template("./blog-detail.html")


@home.route("/home/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        pass
    return render_template("./profile.html")

@home.route("/home/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subj")
        message = request.form.get("message")

        cont = Contact(name=name, email=email, subject=subject, message=message)
        db.session.add(cont)
        db.session.commit()
    return render_template("./contact.html")

