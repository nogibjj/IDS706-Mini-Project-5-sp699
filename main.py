# ETL-Query script
from library.extract import extract_file
from library.transform import load_file
from library.query import create_CRUD, read_CRUD, update_CRUD, delete_CRUD

csv_file_path = "Data/subset.csv"  # CSV 파일 경로
db_file_path = "subsetDB.db"  # SQLite DB 파일 경로
table_name = "subset"  # 테이블 이름

# Extract .csv file
extract_file()


# Transform .csv file to .db file
load_file(csv_file_path, db_file_path, table_name)


# Create from CRUD
data = (13, 1, 3, "female", 25)
create_CRUD(data)


# Read from CRUD
read_CRUD()


# update from CRUD
update_CRUD(13, "age", 18)



# delete from CRUD
delete_CRUD(1)
