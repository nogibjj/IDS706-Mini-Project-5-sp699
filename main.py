# ETL-Query script
from library.load import load_database
from library.query import create_CRUD, read_CRUD

db_file_path = "subsetDB.db"  # SQLite DB 파일 경로


# Load db file
load_database()


# Create from CRUD
data = (13, 1, 3, "female", 25)
create_CRUD("subsetDB.db", data)


# Read from CRUD
read_CRUD(db_file_path)

'''
# update from CRUD
new_data = (1, 2, "male", 35)
update_CRUD("subsetDB.db", 13, new_data)


# delete from CRUD
delete_CRUD(13)
'''