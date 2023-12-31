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
