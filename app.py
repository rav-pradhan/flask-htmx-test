import sqlite3

from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection


@app.route('/')
def hello_world():
    connection = get_db_connection()
    albums = connection.execute("SELECT * FROM albums").fetchall()
    connection.close()

    return render_template("index.html", albums=albums)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7777, debug=True)
