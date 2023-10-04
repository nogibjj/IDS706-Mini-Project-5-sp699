# Test main.py
from library.load import load_database
from library.query import create_CRUD, read_CRUD, update_CRUD, delete_CRUD

import sqlite3


def test_load_database():
    data = load_database()
    if data:
        print("Database loading successful:")
        for row in data:
            print(row)
    else:
        print("Failed to load the database")


def test_create_CRUD():
    data = (13, 1, 3, "female", 25)

    create_CRUD("subsetDB.db", data)

    # Check the inserted data (optional)
    conn = sqlite3.connect("subsetDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subset WHERE id = ?", (13,))
    result = cursor.fetchone()
    conn.close()

    if result:
        print("Inserted data:")
        print(result)

        # Assert statement for data validation
        assert result == data, "Inserted data does not match"
    else:
        print("Unable to verify the data.")


def test_read_CRUD():
    # Database file path
    database = "subsetDB.db"  # Replace with the actual file path.
    
    # Call the read_CRUD function
    data = read_CRUD(database)

    if data:
        print("Data retrieval result:")
        for row in data:
            print(row)

        # Assert statement for data validation
        assert len(data) > 0, "Data is empty"
        print("Test read_CRUD passed successfully.")
    else:
        print("Failed to retrieve data")


def test_update_CRUD():
    # Database file path
    db_file = "subsetDB.db"  # Replace with the actual file path.

    # Check the updated data
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM subset")
    all_records = cursor.fetchall()

    print("Database contents:")
    for row in all_records:
        print(row)

    new_data = (1, 1, "female", 58)  # Data to update (survived, pclass, sex, age)
    record_id = 12  # ID of the record to update
    update_CRUD(db_file, record_id, new_data)  # Function call

    # Retrieve the updated data
    cursor.execute("SELECT * FROM subset WHERE id = ?", (record_id,))
    updated_result = cursor.fetchone()

    # Print the updated and expected results
    expected_data = (record_id,) + new_data
    print("Updated result:", updated_result)
    print("Expected result:", expected_data)

    # Assert statement to compare the updated result with the expected result
    assert updated_result == expected_data, "Data update failed"


def test_delete_CRUD():
    # Database file path
    db_file = "subsetDB.db"  # Replace with the actual file path.

    # ID of the record to delete
    record_id = 13

    delete_CRUD(db_file, record_id)

    # After deleting the record, check if the record exists in the data
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subset WHERE id = ?", (record_id,))
    deleted_result = cursor.fetchone()
    conn.close()
    
    assert deleted_result is None, "Data deletion failed"


if __name__ == "__main__":
    test_load_database()
    test_create_CRUD()
    test_read_CRUD()
    test_update_CRUD()
    test_delete_CRUD()
