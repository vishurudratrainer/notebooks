

import requests
import sqlite3

todosData=requests.get("https://jsonplaceholder.typicode.com/todos/").json()
todosList =[]
for todos in todosData:
    todosList.append((todos['id'],todos['userId'],todos['title'],todos['completed']))

with sqlite3.connect("C:\pythonSQl\my.db") as connection:
    cursor = connection.cursor()
    insert="insert into todos(id,userId,title,completed) values(?,?,?,?)"
    cursor.executemany(insert,todosList)
    connection.commit()
