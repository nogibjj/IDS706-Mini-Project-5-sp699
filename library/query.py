# Query the database
import sqlite3

def create_CRUD(data):
    dataset = "subsetDB"
    table_name = "subset"
    
    conn = sqlite3.connect(dataset)
    cursor = conn.cursor()

    try:
       # 데이터 유효성 검사 (예: 데이터 타입)
        if not isinstance(data[0], int):
            raise ValueError("ID must be an integer")
        if not isinstance(data[1], int):
            raise ValueError("Survived must be an integer")
        if not isinstance(data[2], int):
            raise ValueError("Pclass must be an integer")
        if not isinstance(data[3], str):
            raise ValueError("Sex must be a string")
        if not isinstance(data[4], int):
            raise ValueError("Age must be a integer")

        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER, survived INTEGER, pclass INTEGER, sex TEXT, age INTEGER)")

        query = f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, data)

        conn.commit()
    except Exception as e:
        # 예외 처리: 데이터베이스 작업 중 문제가 발생하면 여기서 예외를 처리할 수 있습니다.
        print(f"An error occurred: {e}")
        conn.rollback()  # 롤백하여 이전 상태로 되돌릴 수도 있습니다.
    finally:
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

    try:
        # Create the table if it doesn't exist
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER, survived INTEGER, pclass INTEGER, sex TEXT, age INTEGER)")

        # Create a dynamic SQL query to update the specified column for a record
        query = f"UPDATE {table_name} SET {column_name}=? WHERE id=?"
        cursor.execute(query, (new_value, record_id))

        # Read the updated value from the database
        cursor.execute(f"SELECT {column_name} FROM {table_name} WHERE id=?", (record_id,))
        updated_value = cursor.fetchone()[0]

        # Commit the changes to the database
        conn.commit()

        return updated_value
    
    finally:
        conn.close()


def delete_CRUD(record_id):
    dataset = "subsetDB"
    table_name = "subset"

    conn = sqlite3.connect(dataset)
    cursor = conn.cursor()

    try:
        query = f"DELETE FROM {table_name} WHERE id = ?"
        cursor.execute(query, (record_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"Record with ID {record_id} has been deleted.")
        else:
            print(f"No record found with ID {record_id}. Nothing deleted.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()