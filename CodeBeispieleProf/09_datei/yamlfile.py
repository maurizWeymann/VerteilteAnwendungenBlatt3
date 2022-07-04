# Stand: 27.04.22
# Beispiel für Dateifunktionen mit JSON
# und Exceptions

#Es wird das Modul pyyaml benötig!

import yaml

def read_my_yamlfile(filename: str):
    """ Read Yaml-Object from file

    Args:
        filename str: path of file

    Raises:
        FileNotFoundError: if file is not readable

    Returns:
        result: dict 
    """
    try:
        with open(filename) as f:
            result = yaml.full_load(f)
    except FileNotFoundError: 
        return "Datei nicht da"

    return result

def write_my_yamlfile(filename: str, data):
    try:
        with open(filename, mode="w") as f:
            f.write(yaml.dump(data) + "\n")
    except Exception as e:
        print(e)

def main():
    ymo = read_my_yamlfile("yamlfile.yml")
    print(ymo)
    
    ymo['Data'] = "Hello World"
    print(ymo)

    write_my_yamlfile("yamlfile1.yml", ymo)

if __name__ == "__main__":
    main()