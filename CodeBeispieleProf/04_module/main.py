# Stand: 22.04.21
# Beispiele für Module

# Einfügen von gesamten Modulen / Bibliotheken
import sys
import math

# Einfügen von spezifischen Teilen eines Modulen / Bibliotheken
from psutil import cpu_count # PSUTIL muss mit PIP installiert werden

# Einfügen von spezifischen Teilen eines Modulen / Bibliotheken mit Alias
from math import factorial as fakultaet

# Eigenes Modulen
from simplemodul import myClass


# main program
def main():
    print("Number of CPU's " + str(cpu_count()))  # Ausgabe mit zusammengesetzten String und Typenkonvertierung
    print("Fakultät 5: {}".format(fakultaet(5)))
    
    m = myClass()
    m.wieder_hallo_welt()
    

# Stellt sicher, dass das Programm nur ausgeführt wird wenn es direkt aufgerufen
# wird und nicht als Modul
if __name__ == "__main__": 
 # Einrückungen werden statt Klammern verwendet, sie müssen in einem Block immer gleich sein
 main() 
 sys.exit(0) # Exit Code 