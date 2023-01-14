import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO albums (title, artist, is_recommended) VALUES (?, ?, ?)", ("Revolver", "The Beatles", 1))
cur.execute("INSERT INTO albums (title, artist, is_recommended) VALUES (?, ?, ?)", ("Station to Station", "David Bowie", 1))

connection.commit()
connection.close()