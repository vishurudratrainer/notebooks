import sqlite3
connection=sqlite3.connect("C:\pythonSQl\my.db")
cursor = connection.cursor()
create_table ='''
create table todos(
id integer,
userId integer,
title text,
completed boolean)
'''
cursor.execute(create_table)
connection.commit()
