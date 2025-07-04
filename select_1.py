import sqlite3
with sqlite3.connect("C:\pythonSQl\my.db") as connection:
    connection.row_factory=sqlite3.Row
    cursor = connection.cursor()
    selectquery="select * from student"
    cursor.execute(selectquery)
    data=cursor.fetchall()
    for student in data:
        print(dict(student))
