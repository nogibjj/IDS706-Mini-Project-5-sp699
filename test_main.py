# Test main.py
from library.load import load_database
from library.query import read_CRUD, update_CRUD

import sqlite3


def test_load_database():
    data = load_database()
    if data:
        print("데이터베이스 불러오기 성공:")
        for row in data:
            print(row)
    else:
        print("데이터베이스 불러오기 실패")


def test_create_CRUD():
    data = (13, 1, 3, "female", "25")
    # 삽입한 데이터 확인 (선택사항)
    conn = sqlite3.connect("subsetDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subset WHERE id = ?", (13,))
    result = cursor.fetchone()
    conn.close()

    if result:
        print("삽입한 데이터 확인:")
        print(result)

        # 데이터 검증을 위한 assert 구문
        assert result == data, "삽입한 데이터와 일치하지 않음"
    else:
        print("데이터를 확인할 수 없습니다.")



def test_read_CRUD():
    # 데이터베이스 파일 경로
    database = "subsetDB.db"  # 실제 파일 경로로 변경해야 합니다.
    # read_CRUD 함수 호출
    data = read_CRUD(database)

    if data:
        print("데이터 조회 결과:")
        for row in data:
            print(row)

        # 데이터 검증을 위한 assert 구문
        assert len(data) > 0, "데이터가 비어 있음"
    else:
        print("데이터 조회 실패")


def test_update_CRUD():
    # 데이터베이스 파일 경로
    db_file = "subsetDB.db"  # 실제 파일 경로로 변경해야 합니다.

    # 업데이트된 데이터 확인
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM subset")
    all_records = cursor.fetchall()
    print("데이터베이스 내용:")
    for row in all_records:
        print(row)

    new_data = (1, 2, "male", 35)  # 업데이트할 데이터 (survived, pclass, sex, age)
    record_id = 12  # 업데이트할 레코드의 ID
    update_CRUD(db_file, record_id, new_data)  # 함수 호출

    # 업데이트된 데이터를 다시 검색
    cursor.execute("SELECT * FROM subset WHERE id = ?", (record_id,))
    updated_result = cursor.fetchone()

    # 업데이트된 결과와 예상 결과를 출력
    expected_data = (1, 2, 'male', 35)
    print("업데이트된 결과:", updated_result)
    print("예상 결과:", expected_data)

    # 업데이트된 결과와 예상 결과를 비교하여 assert 사용
    assert updated_result == expected_data, "데이터 업데이트 확인 실패"

'''
def test_delete_CRUD():
    # 데이터베이스 파일 경로
    db_file = "subsetDB.db"  # 실제 파일 경로로 변경해야 합니다.

    # 삭제할 레코드의 ID
    record_id = 13  # 삭제할 레코드의 ID (실제 데이터베이스 내 레코드 ID와 일치해야 함)

    # 레코드 삭제 후 데이터 조회하여 해당 레코드가 없는지 확인하는 assert 구문
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subset WHERE id = ?", (record_id,))
    deleted_result = cursor.fetchone()
    conn.close()
    
    assert deleted_result is None, "데이터 삭제 실패"

'''

if __name__ == "__main__":
    test_load_database()
    test_create_CRUD()
    test_read_CRUD()
    test_update_CRUD()
    # test_delete_CRUD()