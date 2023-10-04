import sqlite3

def create_CRUD(database, data):
    # Connect to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
        
    # Insert data into the database
    cursor.execute(
        "INSERT INTO subset (id, survived, pclass, sex, age) VALUES (?, ?, ?, ?, ?)", 
        data
        )
    
    conn.commit()

    cursor.execute("SELECT * FROM subset")
    all_records = cursor.fetchall()
    print("Database content:")
    for record in all_records:
        print(record)

    conn.close()
        
    print("Records have been successfully retrieved.")


def read_CRUD(database):
    # Connect to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
        
    # Query data from the database
    cursor.execute("SELECT * FROM subset")
    results = cursor.fetchall()
        
    # Close the connection
    conn.close()
    print("Records have been successfully read.")

    return results


def update_CRUD(database, record_id, new_data):
    # Connect to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Update data
    cursor.execute("UPDATE subset SET survived=?, pclass=?, sex=?, age=? WHERE id=?",
    (*new_data, record_id))

    conn.commit()
    conn.close()

    print("Records have been successfully updated.")


def delete_CRUD(database, record_id):
    # Connect to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Delete data
    cursor.execute("DELETE FROM subset WHERE id=?", (record_id,))

    conn.commit()
    conn.close()

    print("Records have been successfully deleted.")
