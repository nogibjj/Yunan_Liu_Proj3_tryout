import sqlite3
from addName import AddName


conn = sqlite3.connect("dbcreationtest.db")

connectCursor = conn.cursor()

# connectCursor.execute("""CREATE TABLE scores (
#     first text,
#     last text,
#     score integer
#     )""")

# connectCursor.execute("INSERT INTO scores VALUES ('Yunan', 'Liu', 100)")

# connectCursor.execute("INSERT INTO scores VALUES ('Louis', 'Liu', 100)")

# conn.commit()

student_1 = AddName('John', 'Wick', 100)

print(student_1.first)
print(student_1.last)
print(student_1.score)

connectCursor.execute("INSERT INTO scores VALUES (?, ?, ?)", (student_1.first, student_1.last, student_1.score))

conn.commit()

connectCursor.execute("SELECT * FROM scores WHERE last = ?", ('Wick',))

print(connectCursor.fetchall())

connectCursor.execute("SELECT * FROM scores WHERE last = 'Liu'")

print(connectCursor.fetchall())

conn.commit()

conn.close()