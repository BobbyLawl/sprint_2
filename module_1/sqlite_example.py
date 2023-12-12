import sqlite3
import queries as q

#step 1 - Connect to the database
#triple-check the spelling of your database filename
connection = sqlite3.connect("rpg_db.sqlite3")

#step 2 - make the "cursor"
#the cursor is used to fetch data from a database, it is allowed because it has \
#strict commands as to what it can and can't do in order to preserve the integrity of the data.
cursor = connection.cursor()

#step 3 - write a query 
#a query is the list of things which you would like the cursor to fetch and the location to get them
#See queries.py file

#step 4 - Execute the query on the cursor and fetch the results
#"pulling the results" from the cursor
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == "__main__":
    print(results[:5])

    