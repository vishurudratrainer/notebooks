from flask import Flask,jsonify

import sqlite3
app=Flask(__name__)

@app.route("/student")
def retrive():
    with sqlite3.connect("C:\pythonSQl\my.db") as connection:
        connection.row_factory=sqlite3.Row
        cursor = connection.cursor()
        selectquery="select * from student"
        cursor.execute(selectquery)
        data=cursor.fetchall()
        dataLst=[]
        for student in data:
            dataLst.append(dict(student))
        return jsonify(dataLst)



app.run(host="0.0.0.0",port=5000)




