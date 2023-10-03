# Query the database
import sqlite3

def create_CRUD(data):
    dataset = "subsetDB"
    table_name = "subset"
    
    conn = sqlite3.connect(dataset)
    cursor = conn.cursor()

    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id,survived,pclass,sex,age)")

    query = f"INSERT INTO {table_name} VALUES (? ,?, ?, ?, ?)"
    cursor.execute(query, data)

    conn.commit()
    conn.close()

def read_CRUD():
    dataset = "subsetDB"
    table_name = "subset"

    conn = sqlite3.connect(dataset)
    cursor = conn.cursor()

    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def update_CRUD(record_id, column_name, new_value):
    dataset = "subsetDB"
    table_name = "subset"

    conn = sqlite3.connect(dataset)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER, survived INTEGER, pclass INTEGER, sex TEXT, age TEXT)")

    # Create a dynamic SQL query to update the specified column for a record
    query = f"UPDATE {table_name} SET {column_name}=? WHERE id=?"
    cursor.execute(query, (new_value, record_id))

    # Read the updated value from the database
    cursor.execute(f"SELECT {column_name} FROM {table_name} WHERE id=?", (record_id,))
    updated_value = cursor.fetchone()[0]

    conn.close()

    # Read the updated value from the database
    cursor.execute(f"SELECT {column_name} FROM {table_name} WHERE id=?", (record_id,))
    updated_row = cursor.fetchone()
    if updated_row is not None:
        updated_value = updated_row[0]
        # Compare the updated value with the new_value
        if updated_value == new_value:
            print(f"The {column_name} was successfully updated to {updated_value}.")
        else:
            print(f"Failed to update {column_name}.")
    else:
        print(f"Record with PassengerId {record_id} does not exist.")

def delete_CRUD(record_id):
    dataset = "subsetDB"
    table_name = "subset"

    conn = sqlite3.connect(dataset)
    cursor = conn.cursor()

    query = f"DELETE FROM {table_name} WHERE id = ?"
    cursor.execute(query, (record_id,))

    conn.commit()

    cursor.close()
    conn.close()

    print(f"Record with ID {record_id} has been deleted.")