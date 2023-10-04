# Transform .csv file to .db (SQLite) file
import sqlite3
import csv


# Load the .csv file and transform it for SQLite
def load_file(csv_file_path, db_file_path, table_name):
    # SQLite DB 연결
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    # create table (id, survived, pclass, sex, age)
    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER,
            survived INTEGER,
            pclass INTEGER,
            sex TEXT,
            age TEXT
        )
    """
    )

    # open CSV file
    with open(csv_file_path, "r", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            cursor.execute(
                f"""
                INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?)
            """,
                tuple(row),
            )

    # 변경사항 커밋 및 연결 닫기
    conn.commit()
    conn.close()
