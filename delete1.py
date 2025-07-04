import sqlite3
with sqlite3.connect("C:\pythonSQl\my.db") as connection:
    cursor = connection.cursor()
    delete="delete from student where id =?"
    cursor.execute(delete,(1,))
    connection.commit()