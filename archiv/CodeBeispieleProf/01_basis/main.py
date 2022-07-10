#Stand: 13.10.21
# Einfügen von gesamten Modulen / Bibliotheken
import sys

# Einzeilige Kommentare
   # print ....
"""
Mehrzeiliger 
        Kommentar

mit viel Text
"""

# main program
def main():
    print("Hallo Welt"); print("=")
    print("=========\
=========")

# Stellt sicher, dass das Programm nur ausgeführt wird wenn es direkt aufgerufen
# wird und nicht als Modul
if __name__ == "__main__": 
 # Einrückungen werden statt Klammern verwendet, sie müssen in einem Block immer gleich sein
 main() 
 sys.exit(3) # Exit Code 