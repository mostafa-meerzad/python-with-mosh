import json
from pathlib import Path
import sqlite3

movies = json.loads(Path("../Json/movies.json").read_text())

# print(movies)
# for movie in movies:
    # print(movie)
    # print(tuple(movie.values()))
# with sqlite3.connect("user.sqlite3") as conn:
with sqlite3.connect("movies.db") as conn:

    cursor = conn.cursor()
    # command = """
    #     CREATE TABLE IF NOT EXISTS users(
    #         id INTEGER PRIMARY KEY,
    #         name TEXT,
    #         age INTEGER
    #     )
    #     """
    # cursor.execute(command)
    # command = """
    #     INSERT INTO users (id, name, age)
    #         VALUES( ?, ?, ?)
    #     """

    # cursor.execute(
    #     command,
    #     (3, "John", 24),
    # )

    # cursor.execute(
    #     "CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, name VARCHAR(50), year INTEGER)"
    # )

    # for movie in movies:
    #     cursor.execute(
    #         "INSERT INTO movies(id, name, year) VALUES(?, ?, ?)", tuple(movie.values())
    #     )
        
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    conn.commit()

# print(movies)


