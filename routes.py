from app import app
from flask import render_template, request, redirect
import messages, users
from messages import result_query
from db import db
from sqlalchemy.sql import text

@app.route("/")
def index():
    list = messages.get_list()
    return render_template("index.html", count=len(list), messages=list)

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST"])
def send():
    title = request.form["title"]
    content = request.form["content"]
    if messages.send(title, content):
        return redirect("/")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "" or password == "":
            return "Käyttäjänimi ja/tai salasana on tyhjä"
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if username == "" or password == "":
            return "Käyttäjänimi ja/tai salasana on tyhjä"
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

@app.route("/result", methods=["GET"])
def result():
    query = request.args.get("query")
    if query is None:
        return "Haku on tyhjä"

    messages = result_query(query)
    return render_template("index.html", messages=messages, count=len(messages))

@app.route("/areas")
def areas():
    sql = text("SELECT * FROM areas")
    result = db.session.execute(sql)
    areas = result.fetchall()
    return render_template("areas.html", areas=areas)

@app.route("/threads/<int:area_id>")
def threads(area_id):
    sql = text("SELECT * FROM threads WHERE area_id = :area_id")
    result = db.session.execute(sql, {"area_id": area_id})
    threads = result.fetchall()
    return render_template("threads.html", area_id=area_id, threads=threads)

@app.route("/create_area")
def create_area():
    return render_template("create_area.html")

@app.route("/create_area", methods=["POST"])
def save_area():
    name = request.form["name"]
    sql = text("INSERT INTO areas (name) VALUES (:name)")
    db.session.execute(sql, {"name": name})
    db.session.commit()
    return redirect("/areas")

@app.route("/create_thread/<int:area_id>")
def create_thread(area_id):
    return render_template("create_thread.html", area_id=area_id)

@app.route("/create_thread/<int:area_id>", methods=["POST"])
def save_thread(area_id):
    title = request.form["title"]
    content = request.form["content"]
    sql = text("INSERT INTO threads (title, content, area_id, sent_at) VALUES (:title, :content, :area_id, NOW())")
    db.session.execute(sql, {"title": title, "content": content, "area_id": area_id})
    db.session.commit()
    return redirect("/threads/{}".format(area_id))

@app.route("/view_thread/<int:thread_id>")
def view_thread(thread_id):
    sql = text("SELECT * FROM threads WHERE id = :thread_id")
    sql2 = text("SELECT * FROM messages WHERE thread_id = :thread_id ORDER BY sent_at")
    result = db.session.execute(sql, {"thread_id": thread_id})
    result2 = db.session.execute(sql2, {"thread_id": thread_id})
    thread = result.fetchone()
    messages = result2.fetchall()
    return render_template("view_thread.html", thread=thread, messages=messages)

@app.route("/create_message/<int:thread_id>", methods=["POST"])
def create_message(thread_id):
    content = request.form["content"]
    user_id = users.user_id()
    if user_id == 0:
        return "Käyttäjän on oltava kirjatunut lisätäkseen viestin."

    sql = text("INSERT INTO messages (content, user_id, thread_id, sent_at) VALUES (:content, :user_id, :thread_id, NOW())")
    db.session.execute(sql, {"content": content, "user_id": user_id, "thread_id": thread_id})
    db.session.commit()
    return redirect("/view_thread/{}".format(thread_id))
