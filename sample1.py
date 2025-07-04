import sqlite3
connection=sqlite3.connect("C:\pythonSQl\my.db")
cursor = connection.cursor()
create_table ='''
create table student(
id integer primary key autoincrement,
name text,
age integer)
'''
cursor.execute(create_table)
connection.commit()
