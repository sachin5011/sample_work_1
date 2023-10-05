from flask import Blueprint, request, render_template
from models.models import Student
from connections.sqlite import db
from utils.data import create_df, analysis
import json
import plotly
import plotly.express as px


std = Blueprint("std", __name__)




@std.route("/")
def home():
    df = create_df()
    # Graph1
    fig = px.bar(df, x="nationality", y="name")
    graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # graph2
    fig1 = px.scatter_3d(df, x="gender", y="nationality", z="name", color="id")
    graph2 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("./index.html", 
                           graph=graph,
                           graph2=graph2)


@std.route("/test")
def test():
    create_df()
    student1 = db.Table("student1", db.metadata, autoload_with=db.engine)
    std_data = db.session.query(student1).all()
    return render_template("./test.html", std_data=std_data)

@std.route("/test1")
def test1():
    df = create_df()
    return render_template('./dataframe.html',  tables=[df.to_html(classes='data', index=0)], titles=df.columns)

@std.route("/add-new-data", methods=["GET", "POST"])
def addstudent():
    if request.method == "POST":
        try:
            first_name = request.form.get("f_name")
            last_name = request.form.get("l_name")
            email = request.form.get("email")

            std = Student(first_name=first_name, last_name=last_name, email=email)
            db.session.add(std)
            db.session.commit()
        except Exception as e:
            raise

        finally:
            db.session.close()

    return render_template("./student.html")
