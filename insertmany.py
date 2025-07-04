import sqlite3
with sqlite3.connect("C:\pythonSQl\my.db") as connection:
    cursor = connection.cursor()
    insert="insert into student(name,age) values(?,?)"
    students=[("Raju",14),("Vikram",10)]
    cursor.executemany(insert,students)
    connection.commit()
