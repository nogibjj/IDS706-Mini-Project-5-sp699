# Transform .csv file to .db (SQLite) file
import sqlite3


# Load the .csv file and transform it for SQLite
def load_database():
    conn = sqlite3.connect("subsetDB.db")
        
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subset")
    results = cursor.fetchall()

    # age 열의 데이터 형식을 정수로 변경
    cursor.execute("PRAGMA foreign_keys = 0")  # 외래 키 비활성화
    cursor.execute("ALTER TABLE subset RENAME TO subset_old")  # 현재 테이블을 이름 변경
    cursor.execute("CREATE TABLE subset (id INTEGER PRIMARY KEY, survived INTEGER, pclass INTEGER, sex TEXT, age INTEGER)")  # 새로운 테이블 생성
    cursor.execute("INSERT INTO subset (id, survived, pclass, sex, age) SELECT id, survived, pclass, sex, CAST(age AS INTEGER) FROM subset_old")  # 데이터 복사
    cursor.execute("DROP TABLE subset_old")  # 이전 테이블 삭제
    cursor.execute("PRAGMA foreign_keys = 1")  # 외래 키 다시 활성화

    # 변경사항 커밋
    conn.commit()  
    conn.close()
        
    return results