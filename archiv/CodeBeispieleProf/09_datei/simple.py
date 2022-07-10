# Stand: 22.04.21
# Beispiel für Dateifunktionen
# und Exceptions

import os.path

# Textdatei lesen
def read_my_file(filename):
    # Einfaches Zeilebasiertes einlesen ohne Fehlerbehandlung
    f = open(filename)
    content1 = f.readlines()
    f.close()

    # Einfaches Zeilebasiertes einlesen ohne Fehlerbehandlung
    # und entfernen der Zeilenumbrüche
    with open(filename) as f1:
        content2 = f1.read().splitlines()
    

    return content1, content2

# Textdatei lesen und Daten verändern mit Exeptions
def read_my_file1(filename):
    result = list()
    try:
        if not os.path.isfile(filename):
            raise FileNotFoundError # Nutzerspezifischen Fehler auslösen

        with open(filename) as f:
            content = f.read().splitlines()
    
    except FileNotFoundError: 
        return "Datei nicht da"

    for c in content:
        try:
            result.append(int(c))
        except ValueError:
            print("Übergehe Kommentar")        
    
    return result

def write_my_file(filename, data):
    try:
        with open(filename, mode="a") as f:
            f.write(str(data) + "\n")
    except Exception as e:
        print(e)

def main():
    pass

if __name__ == "__main__":
    main()