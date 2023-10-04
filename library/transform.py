# Transform .csv file to .db (SQLite) file
import sqlite3
import csv


# Load the .csv file and transform it for SQLite
def load_database():
    conn = sqlite3.connect("subsetDB.db")
        
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subset")
    results = cursor.fetchall()
        
    conn.close()
        
    return results