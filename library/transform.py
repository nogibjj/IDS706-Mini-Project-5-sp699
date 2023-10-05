# Transform .csv file to .db file
import sqlite3
import csv


# load the csv file and transform it to db file
def load_database(dataset="Data/subset.csv", encoding="utf-8"):
    subset_data = csv.reader(open(dataset, newline="", encoding=encoding), delimiter=",")
    # skips the header of csv
    next(subset_data)
    conn = sqlite3.connect("subsetDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS subset")
    c.execute(
        """
        CREATE TABLE subset (
            id INTEGER,
            survived INTEGER,
            pclass INTEGER,
            sex TEXT,
            AGE INTEGER
        )
    """
    )
    # insert
    c.executemany(
        """
        INSERT INTO subset (
            id,
            survived,
            pclass,
            sex,
            age
            ) 
            VALUES (?, ?, ?, ?, ?)""",
        subset_data,
    )
    conn.commit()
    conn.close()
    return "subsetDB.db"
