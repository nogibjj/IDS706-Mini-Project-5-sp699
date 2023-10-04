# Transform .csv file to .db (SQLite) file
import sqlite3

# Load the .csv file and transform it for SQLite
def load_database():
    conn = sqlite3.connect("subsetDB.db")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subset")
    results = cursor.fetchall()

    # Change the data type of the 'age' column to integer
    cursor.execute("PRAGMA foreign_keys = 0")  # Disable foreign keys
    cursor.execute("ALTER TABLE subset RENAME TO subset_old")  # Rename the current table
    cursor.execute("""
    CREATE TABLE subset (
        id INTEGER PRIMARY KEY,
        survived INTEGER,
        pclass INTEGER,
        sex TEXT,
        age INTEGER
        )
    """)
    # Copy the data
    cursor.execute("""
        INSERT INTO subset (id, survived, pclass, sex, age)
        SELECT id, survived, pclass, sex, CAST(age AS INTEGER) FROM subset_old
    """)

    cursor.execute("DROP TABLE subset_old")  # Delete the old table
    cursor.execute("PRAGMA foreign_keys = 1")  # Re-enable foreign keys

    # Commit the changes
    conn.commit()
    conn.close()

    return results
