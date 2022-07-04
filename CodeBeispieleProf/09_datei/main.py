# Beispiel für Dateifunktionen
# und Exceptions

import simple as sf
import jsonfile as jf
import yamlfile as yf

def main():
    # Fehler können getestet werden, wenn der Dateiname geändert ist
    try:
        value, value1 = sf.read_my_file("simplefile.txt")
    except Exception as e:
         print(e)
    finally: 
        # wird immer aufgerufen am Ende des Try/Expept Blocks
        # aufgerufen, auch wenn kein Fehler vorliegt
        print("Ich werde immer als letztes angezeigt")

    print(value, value1)
    print(sf.read_my_file1("simplefile.txt"))
    #sf.write_my_file("simplefile.txt", random.randint(0, 9999))

    ## JSON example
    jso = jf.read_my_jsonfile("jsonfile.json")
    print(jso)
    
    jso[0]['name'] = "Peter"
    print(jso)

    jf.write_my_jsonfile("jsonfile1.json", jso)

    ## YAML example
    ymo = yf.read_my_yamlfile("yamlfile.yml")
    print(ymo)
    
    ymo['Data'] = "Hello World"
    print(ymo)

    yf.write_my_yamlfile("yamlfile1.yml", ymo)

if __name__ == "__main__":
    main()