from connections.sqlite import db

    

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(255))

# using existing table from sqlite databse
# student1 = db.Table("student1", db.metadata, autoload=True, autoload_with=db.engine)

