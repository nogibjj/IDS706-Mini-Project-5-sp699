# Test main.py
from library.load import load_database
from library.query import create_CRUD, read_CRUD, update_CRUD, delete_CRUD

import sqlite3


def test_load_database():
    data = load_database()
    if data:
        print("데이터베이스 불러오기 성공:")
        for row in data:
            print(row)
    else:
        print("데이터베이스 불러오기 실패")

test_load_database()

'''
def test_create_CRUD():
    data = (13, 1, 3, "female", 25)
    # Connect to the database and check if the data was inserted
    conn = sqlite3.connect("subsetDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subset WHERE id = 13")
    result = cursor.fetchone()

    assert result == data

    # Clean up by deleting the inserted data
    cursor.execute("DELETE FROM subset WHERE id = 13")
    conn.commit()
    conn.close()

def test_read_CRUD():
    result = read_CRUD()

    # Check if the result is a list (assuming it contains multiple rows)
    assert isinstance(result, list)
    
    # Check if the result is not empty
    assert len(result) > 0

def test_update_CRUD():
    # Insert test data
    test_data = (13, 1, 1, "female", 19)
    create_CRUD(test_data)

    # Call the update_CRUD function to update a specific column
    record_id = 13
    column_name = "age"
    new_value = 18

    update_CRUD(record_id, column_name, new_value)

    # Fetch the updated data from the database
    updated_data = read_CRUD()

    # Create the expected data with the updated age value
    expected_data = (13, 1, 1, "female", 18)

    # Compare the fetched data with the expected data
    assert updated_data == expected_data

def test_delete_CRUD():
    # Call the delete_CRUD function to delete a record
    record_id = 13
    delete_CRUD(record_id)

    # Connect to the database and check if the record was deleted
    conn = sqlite3.connect("test_subsetDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_subset WHERE id = ?", (record_id,))
    result = cursor.fetchone()

    # Check if the result is None, indicating the record was deleted
    assert result is None

if __name__ == "__main__":
    test_extract_file()
    test_load_file()
    test_create_CRUD()
    test_read_CRUD()
    test_update_CRUD()
    test_delete_CRUD()
'''