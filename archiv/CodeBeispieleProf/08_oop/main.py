# Stand: 22.04.21
# Beispiel für einfache OOP

# Namenskonventionen für Methoden und Variablen in Python 
# public : name, 
# protected : _name 
# private : __name  
# Private Methoden und Variablen lassen sich nur 
# aufrufen innerhalb der Klasse aufrufen

from dataclasses import dataclass
from pprint import pprint

class Basis():
    # Klassenvariable, über alle Instanzen gleich
    # und auch bei Veränderung, wenn mutable
    variable = "Ein Wert"

    # Konstruktor
    def __init__(self, wert, wert1):
        self.wert = wert
        self.wert1 = wert1 + 3

    # Methodenfunktion
    def ausgabe(self):
        print(f"Klasse Basis:  {self.wert} : {self.wert1}")
        self.__ausgabe1()
    
    # private Methode
    def __ausgabe1(self):
        print(f"PRIVATE Klasse Basis:  {self.wert} : {self.wert1}")


# Abgeleitet von Basis 
class Geerbt1_von_Basis(Basis):
    # Überschreibt Methode von der Basisklasse
    def ausgabe(self):
        print(f"Klasse Geerbt1:  {self.wert} : {self.wert1}")

class Geerbt2_von_Basis(Basis):
    def __init__(self, wert, wert1):
        super().__init__(wert, wert1) # Aufruf von Methoden der Basisklasse
        self.wert1 -= 1

    def ausgabe(self):
        print(f"Klasse Geerbt2:  {self.wert} : {self.wert1}")

    # Überschreiben von "magic methods" für Vergleiche
    def __eq__(self, other):
        if self.wert == other.wert and self.wert1 == other.wert1:
            return True
        else:
            return False 
    
    # Überschreiben von "magic methods" für Stringausgabe
    def __str__(self):
        return "Hallo"

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class MyData():
    x : int
    y : int


def main():
    myclass = Basis("Hallo Klasse", 3)
    myclass.ausgabe()
    
    try:
        myclass.__ausgabe1()
    except Exception as e:
        print(f"ERROR: {e}")

    myclass1 = Geerbt1_von_Basis("Hallo Geerbt1 von Basis", 4)
    
    pprint(help(myclass1))

if __name__ == "__main__": 
    main()