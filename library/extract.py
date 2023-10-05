# Extract csv file through link
import requests

def extract(url="https://github.com/suim-park/Mini-Project-5/blob/main/Data/subset.csv", 
            file_path="Data/subset.csv", timeout=None):
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path