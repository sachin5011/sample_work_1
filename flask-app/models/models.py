from dbconnection.sqlite_conn import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(250))
    password = db.Column(db.String(250))
    post = db.relationship("Blog", backref="auther_id")
    profile = db.relationship("Profile")

    def __repr__(self) -> str:
        return self.email


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    title = db.Column(db.String(300))
    body = db.Column(db.String(10000))
    category = db.Column(db.String(500))
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)
    images = db.Column(db.String(1000))


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    about = db.Column(db.String(1000))
    avatar = db.Column(db.String(500))
    facebook = db.Column(db.String(300))
    twitet = db.Column(db.String(300))
    github = db.Column(db.String(300))

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    subject = db.Column(db.String(500))
    message = db.Column(db.String(1000))
                     




