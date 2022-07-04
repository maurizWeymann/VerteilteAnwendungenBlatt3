# Stand: 27.04.22
# Beispiel für Dateifunktionen mit JSON
# und Exceptions

import json

def read_my_jsonfile(filename: str):
    """ Read Json-Object from file

    Args:
        filename str: path of file

    Raises:
        FileNotFoundError: if file is not readable

    Returns:
        result: list  from json obj
    """
    try:
        with open(filename) as f:
            result = json.load(f)
    except FileNotFoundError: 
        return "Datei nicht da"

    return result

def write_my_jsonfile(filename: str, data):
    try:
        with open(filename, mode="w") as f:
            f.write(json.dumps(data, indent=2) + "\n")
    except Exception as e:
        print(e)

def main():
    jso = read_my_jsonfile("jsonfile.json")
    print(jso)
    
    jso[0]['name'] = "Peter"
    print(jso)

    write_my_jsonfile("jsonfile1.json", jso)

if __name__ == "__main__":
    main()