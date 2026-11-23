import os
from util import change_table_name, tsql_to_duckdb

class Database:
    def __init__(self, data_path: str):
        self.tables = []
        for root, dirs, files in os.walk(data_path):
            for f in files:
                if f.endswith(".csv"):
                    self.tables.append({f: os.path.join(root, f)})
        self.curr_results = ""
        self.errors = ""