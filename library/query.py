# Query the database
import sqlite3

def create_CRUD(database, data):
    # 데이터베이스 연결
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
        
    # 데이터베이스에 데이터 삽입
    cursor.execute(
        "INSERT INTO subset (id, survived, pclass, sex, age) VALUES (?, ?, ?, ?, ?)", 
        data
        )
    
    conn.commit()

    cursor.execute("SELECT * FROM subset")
    all_records = cursor.fetchall()
    print("데이터베이스 내용:")
    for record in all_records:
        print(record)

    conn.close()
        
    print("레코드가 성공적으로 생성되었습니다.")


def read_CRUD(database):
    # 데이터베이스 연결
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
        
    # 데이터베이스에서 데이터 조회
    cursor.execute("SELECT * FROM subset")
    results = cursor.fetchall()
        
    # 연결 종료
    conn.close()
    return results


def update_CRUD(database, record_id, new_data):
    # 데이터베이스 연결
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # 데이터 업데이트
    cursor.execute("UPDATE subset SET survived=?, pclass=?, sex=?, age=? WHERE id=?",
    (*new_data, record_id))

    conn.commit()
    conn.close()

    print("레코드가 성공적으로 업데이트되었습니다.")


def delete_CRUD(database, record_id):
    # 데이터베이스 연결
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # 데이터 삭제
    cursor.execute("DELETE FROM subset WHERE id=?", (record_id,))

    conn.commit()
    conn.close()

    print("레코드가 성공적으로 삭제되었습니다.")