import sqlite3
import pandas as pd

connection = sqlite3.connect("test.db")

df = pd.read_sql_query("SELECT * FROM survey_answers", connection)

print(df)

connection.execute(
    "INSERT INTO students(name, course_name) VALUES ('Vincent', 'Ruby')")
connection.commit()
