from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import app



app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


@app.route("/")
def index():
    try:
        result = db.session.execute(text("SELECT title, content FROM messages"))
        messages = result.fetchall()
        return render_template("index.html", count=len(messages), messages=messages)
    except Exception as e:
        return "Virhe: " +str(e)


@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    if not user:
        return redirect("/")
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["username"] = username
            return redirect("/")
        else:
            return redirect("/")




@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 20:
            return render_template("error.html", message="Tunnuksessa tulee olla 1-20 merkkiä")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if password1 == "":
            return render_template("error.html", message="Salasana on tyhjä")
        else:
            hash_value = generate_password_hash(password1)
            sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
            db.session.execute(sql, {"username":username, "password":hash_value})
            db.session.commit()

            return redirect("/")

@app.route("/send", methods=["POST"])
def send():
    try:

        content = request.form["content"]
        title = request.form["title"]
        sql = text("INSERT INTO messages (content, title) VALUES (:content, :title)")
        db.session.execute(sql, {"content":content, "title":title})
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return "Virhe: " +str(e)

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/result", methods=["GET"])
def result():
    query = request.args["query"]
    sql = text("SELECT content FROM messages WHERE content LIKE :query")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    messages = result.fetchall()
    return render_template("index.html", messages=messages)
