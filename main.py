# ETL-Query script
from library.extract import extract_file
from library.transform import load_file
from library.query import create_CRUD, read_CRUD, update_CRUD, delete_CRUD

csv_file_path = "Data/titanic.csv"  # CSV 파일 경로
db_file_path = "titanic_passengersDB.db"  # SQLite DB 파일 경로
table_name = "titanic"  # 테이블 이름

# Extract .csv file
extract_file()


# Transform .csv file to .db file
load_file(csv_file_path, db_file_path, table_name)

# Create from CRUD
data = (892, 1, 1, "Rose, Miss. DeWitt Bukater", "female", 19, 0, 1, 12, 100, 2, "Q")
create_CRUD(data)

# Read from CRUD
read_CRUD()
print(read_CRUD())


# update from CRUD
update_CRUD(892, "Age", 18)

# delete from CRUD
delete_CRUD(892)