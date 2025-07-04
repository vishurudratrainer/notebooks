import sqlite3
import pandas as pd
with sqlite3.connect("C:\pythonSQl\my.db") as connection:
    connection.row_factory=sqlite3.Row
    selectquery="select * from student"
    df=pd.read_sql_query(selectquery,connection)
    print(df)
