import sqlite3
with sqlite3.connect("C:\pythonSQl\my.db") as connection:
    cursor = connection.cursor()
    update="update student set name =? where id= ?"
    cursor.execute(update,("Raju123",2))
  
    connection.commit()
