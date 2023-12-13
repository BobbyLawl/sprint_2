import sqlite3
import queries as q
import pandas as pd


#DB connect function
def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)

#creating a function which will accept the DB connection made above and query it
def execute_q(conn, query):
    #make the cursor
    curs = conn.cursor()
    #execute the query
    curs.execute(query)
    #pull (and return) the results
    return curs.fetchall()

if __name__ == "__main__":
    conn = connect_to_db()
    results = execute_q(conn, q.SELECT_ALL)[:5]
    df = pd.DataFrame(results)
    df.columns = ["name", "average_item_weight"]
    df.to_csv("rpg_db.csv", index = False)

'''
step 1 - Connect to the database
triple-check the spelling of your database filename
Ex: connection = sqlite3.connect("rpg_db.sqlite3")

step 2 - make the "cursor"
the cursor is used to fetch data from a database, it is allowed because it has \
strict commands as to what it can and can't do in order to preserve the integrity of the data.
Ex: cursor = connection.cursor()

step 3 - write a query 
a query is the list of things which you would like the cursor to fetch and the location to get them
See queries.py file

step 4 - Execute the query on the cursor and fetch the results
"pulling the results" from the cursor
Ex: results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == "__main__":
    print(results[:5])

'''
