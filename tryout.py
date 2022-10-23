import sqlite3

conn = sqlite3.connect("dbcreationtest.db")

connectCursor = conn.cursor()

# connectCursor.execute("""CREATE TABLE scores (
#     first text,
#     last text,
#     score integer
#     )""")

# connectCursor.execute("INSERT INTO scores VALUES ('Yunan', 'Liu', 100)")

connectCursor.execute("INSERT INTO scores VALUES ('Louis', 'Liu', 100)")

conn.commit()

connectCursor.execute("SELECT * FROM scores WHERE last = 'Liu'")

print(connectCursor.fetchall())

conn.commit()

conn.close()