'''
This is Part 2 of the Sprint 10, Module 1 project
'''
import sqlite3
import pandas as pd

conn = sqlite3.connect("buddymove_holidayiq.sqlite3")
curs = conn.cursor()

df = pd.read_csv("buddymove_holidayiq.csv")

if __name__ == "__main__":
    df.to_sql("review", conn, if_exists="replace")

    curs.execute(''' SELECT * FROM review;''')

NATURE_SHOPPING = '''
SELECT COUNT(*) AS greater_100
FROM review
WHERE Nature >= 100 AND Shopping >= 100
'''
