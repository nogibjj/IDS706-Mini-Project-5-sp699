# ETL-Query script
from library.load import load_database
from library.query import create_CRUD, read_CRUD, update_CRUD, delete_CRUD

db_file_path = "subsetDB.db"  # SQLite DB 파일 경로
record_id = 12
delete_id = 13
data = (13, 1, 3, "female", 25)
new_data = (1, 2, "male", 35)



if __name__ == "__main__":
    load_database()
    create_CRUD("subsetDB.db", data)
    read_CRUD(db_file_path)
    update_CRUD("subsetDB.db", record_id, new_data)
    delete_CRUD(db_file_path, delete_id)
