import sqlite3
with sqlite3.connect("C:\pythonSQl\my.db") as connection:
    cursor = connection.cursor()
    insert="insert into student(name,age) values(?,?)"
    cursor.execute(insert,("Raj",14))
    connection.commit()
