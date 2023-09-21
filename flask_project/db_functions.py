import sqlite3

from flask import g
from settings import app


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


# def add_data():
#     con = connect_db()
#     cur = con.cursor()
#     cur.executemany("INSERT INTO mainmenu (title, url) VALUES (?, ?)", data)
#     con.commit()
#     con.close()
