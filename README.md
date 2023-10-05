![SQL Database](https://github.com/nogibjj/IDS706-Mini-Project-5-sp699/actions/workflows/main.yml/badge.svg)
# IDS-706-Data-Engineering :computer:

## Mini Project 5 :page_facing_up: 

## :ballot_box_with_check: Requirements
* Connect to a SQL database</br>
* Perform CRUD operations</br>
* Write at least two different SQL queries

## :ballot_box_with_check: To-do List
* __Understanding database connection__: To understand the datbase basics and know how to use them.</br>

## :ballot_box_with_check: Dataset
* `Titanic Subset`
  - The data is a subset of the dataset related to the survivors of the __Titanic__.</br>
* `Brief Description`</br>
  - `id`: integer (1-12 assigned)
  - `survived`: integer (1: survived, 0: not survived)
  - `pclass`: integer (1: 1st class, 2: 2nd class, 3: 3rd class)
  - `sex`: text (male, female)
  - `age` integer
![image](https://github.com/nogibjj/IDS706-Mini-Project-5-sp699/assets/143478016/7efd6350-8578-4323-80ad-5d4986d8473f)</br>

## :ballot_box_with_check: In progress
__`Step 1`__ : Set up the environment to install multiple Python versions in GitHub Actions.
- `requirements.txt`: Add `pandas`(version=2.1.0).</br>
<img src="https://github.com/suim-park/Mini-Project-5/assets/143478016/6e8d500a-fa80-4430-a018-38f1827cf5f0.png" width="160" height="200"/></br>
- `main.yml`: Build the multiple Python versions in __main.yml__ file.  </br>
<img src="https://github.com/nogibjj/IDS706-Mini-Project-5-sp699/assets/143478016/8c62477c-5acc-4c94-873d-414da92313d2.png" width="350" height="620"/></br>
- `Makefile`: Include the functions for install, test, lint, and format to automate the build. </br>
<img src="https://github.com/nogibjj/IDS706-Mini-Project-5-sp699/assets/143478016/57b59ef1-1a4b-447a-838e-d3e795980e86.png" width="430" height="230"/></br>
- `Dockerfile`: Create a Dockerfile that builds an image to create a container in Codespace.</br>
- `devcontainer.json`: Define and set up a development environment.

__`Step 2`__ : Add SQL CRUD operations to the __libarary/query.py__ file. Utilize the libarary/load.py file to load the database in this case.</br>
* `library/extract.py`</br>
```Python
# Extract csv file through link
import requests

def extract(url="https://github.com/suim-park/Mini-Project-5/blob/main/Data/subset.csv", 
            file_path="Data/subset.csv"):
    with requests.get(url, timeout=10) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path
```
* `library/transform.py`</br>
```Python
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
```
* `libarart/query.py`</br>
```Python
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
    print("Database content (create):")
    for record in all_records:
        print(record)

    conn.close()
        
    print("Records have been successfully created.")

def read_CRUD(database):
    # Connect to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
        
    # Query data from the database
    cursor.execute("SELECT * FROM subset")
    results = cursor.fetchall()
        
    # Close the connection
    conn.close()

    print("Database content (read):")
    for record in results:
        print(record)

    print("Records have been successfully retrieved.")
    
    return results

def update_CRUD(database, record_id, new_data):
    # Connect to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Update data
    cursor.execute("UPDATE subset SET survived=?, pclass=?, sex=?, age=? WHERE id=?",
    (*new_data, record_id))

    conn.commit()

    cursor.execute("SELECT * FROM subset")
    all_records = cursor.fetchall()
    print("Database content (update):")
    for record in all_records:
        print(record)

    conn.close()

    print("Records have been successfully updated.")

def delete_CRUD(database, record_id):
    # Connect to the database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Delete data
    cursor.execute("DELETE FROM subset WHERE id=?", (record_id,))

    conn.commit()

    cursor.execute("SELECT * FROM subset")
    all_records = cursor.fetchall()
    print("Database content (delete):")
    for record in all_records:
        print(record)

    conn.close()

    print("Records have been successfully deleted.")
```
* `main.py`</br>
```Python
# ETL-Query script
from library.extract import extract
from library.transform import load_database
from library.query import create_CRUD, read_CRUD, update_CRUD, delete_CRUD

db_file_path = "subsetDB.db"  # SQLite DB file path
record_id = 13
delete_id = 13
data = (13, 1, 3, "female", 25)
new_data = (1, 1, "female", 40)

if __name__ == "__main__":
    extract(url="https://github.com/suim-park/Mini-Project-5/blob/main/Data/subset.csv", 
            file_path="Data/subset.csv")
    load_database()
    create_CRUD("subsetDB.db", data)
    read_CRUD(db_file_path)
    update_CRUD("subsetDB.db", record_id, new_data)
    delete_CRUD(db_file_path, delete_id)
```
* `test_main.py`</br>
```Python
# Test main.py
from library.extract import extract
from library.transform import load_database
from library.query import create_CRUD, read_CRUD, update_CRUD, delete_CRUD

import sqlite3

def test_extract():
    result = extract(url="https://github.com/suim-park/Mini-Project-5/blob/main/Data/subset.csv", 
            file_path="Data/subset.csv")
    assert result is not None

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

    new_data = (1, 1, "female", 40)  # Data to update (survived, pclass, sex, age)
    record_id = 13  # ID of the record to update
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
    test_extract()
    test_load_database()
    test_create_CRUD()
    test_read_CRUD()
    test_update_CRUD()
    test_delete_CRUD()
```
__`Step 3`__ : Verify if SQL runs correctly.
* __Test__ </br>
![image](https://github.com/nogibjj/IDS706-Mini-Project-5-sp699/assets/143478016/261a988d-a2fc-4ee7-8543-d01f5096c23a)</br>
* __Lint__ </br>
<img src="https://github.com/nogibjj/IDS706-Mini-Project-5-sp699/assets/143478016/55ab2d8f-f095-491b-8851-3cb9839cf5b2.png" width="580" height="90"/></br>
* __Format__ </br>
<img src="https://github.com/nogibjj/IDS706-Mini-Project-5-sp699/assets/143478016/66cbd0f3-e9dd-4cfb-826a-c57373cd7e3c.png" width="580" height="110"/></br>

__`Step 4`__ : Check whether GitHub Action has different multiple Python versions.</br>
* __SQL__ </br>
:exclamation: __`update CRUD`__: Since the tests are happening __simultaneously__, the results may appear to have no changes in the data values. However, the update_CRUD() function is functioning correctly.</br>
<img src="https://github.com/nogibjj/IDS706-Mini-Project-5-sp699/assets/143478016/a76699b0-9a15-4542-be98-651a2b4dd9ed.png" width="250" height="500"/></br>
<img src="https://github.com/nogibjj/IDS706-Mini-Project-5-sp699/assets/143478016/8d95eaf7-46ca-44af-9bcb-39222fe3be73.png" width="250" height="500"/></br>
