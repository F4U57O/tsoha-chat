from db import db
from sqlalchemy.sql import text
import users

def get_list():
    sql = text("SELECT M.title, M.content, U.username, M.sent_at FROM messages M, users U WHERE M.user_id=U.id ORDER BY M.id")
    result = db.session.execute(sql)
    return result.fetchall()

def send(title, content):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO messages (title, content, user_id, sent_at) VALUES (:title, :content, :user_id, NOW())")
    db.session.execute(sql, {"title":title, "content":content, "user_id":user_id})
    db.session.commit()
    return True

def result_query(query):
    sql = text("SELECT M.title, M.content, U.username, M.sent_at FROM messages M, users U WHERE M.user_id=U.id AND M.content LIKE :query ORDER BY M.id")
    result = db.session.execute(sql, {"query": "%" +query + "%"})
    messages = result.fetchall()
    return messages

def get_threads():
    sql = text("SELECT * FROM threads")
    result = db.session.execute(sql)
    threads = result.fetchall()
    return threads

def get_latest():
    sql = text("SELECT * FROM messages WHERE sent_at = (SELECT MAX(sent_at) FROM messages)")
    result = db.session.execute(sql)
    latest_message = result.fetchone()
    return latest_message
