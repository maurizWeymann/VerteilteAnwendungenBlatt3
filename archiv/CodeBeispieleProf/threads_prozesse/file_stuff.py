import json
import sys

DATA_FILE_NAME = "test.data"

def write_data_file(value : list) -> None:       
    try:
        with open(DATA_FILE_NAME, "w") as f:
            f.write(json.dumps(value))
    except Exception as e:
        print(f"Error write_data_file: {e}")
        sys.exit(1)

def read_data_file() -> list:       
    try:
        with open(DATA_FILE_NAME, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error read_data_file: {e}")
        data = [0, 0, 0, 0]
        #sys.exit(1)
    
    return data