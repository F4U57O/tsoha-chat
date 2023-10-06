from db import db
from flask import session
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = text("SELECT id, password, role FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    if not user:
        return False
    else:
        hash_value = user.password
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["user_role"] = user.role
            return True
        else:
            return False


def logout():
    del session["user_id"]
    del session["user_role"]

def register(username, password, role):
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username,password, role) VALUES (:username,:password,:role)")
        db.session.execute(sql, {"username":username, "password":hash_value, "role": role})
        db.session.commit()
    except:
        return False
    return login(username, password)

def user_id():
    return session.get("user_id", 0)

def get_user_role(user_id):
    sql = text("SELECT role FROM users WHERE id = :user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    role = result.scalar()

    return role
