# Stand: 12.10.21
# Beispiele für Funktionen

# Einfache Übergabe
def my_func(wert : float) -> float:
    print(f"Ausgabe {wert}")
    return wert + 2

# Mehrfache Übergabe mit optionalen Parametern    
def other_func(wert1 = None, wert2 : str = None):
    print(f"Ausgabe Wert1: {wert1} -- Wert2: {wert2}")

# Mehrfache Parameter
def multivalue_func(*values):
    print(values)

def do_nothing() -> None:
    pass # Platzhalter für "leere" Blöcke wie Funktionen, Bedingungen, Klassen, Exeptions

# Rückgabe mehrerer Werte
def multireturn_func(a : float, b : float) -> tuple[float]:
    add = a + b
    mul = a * b
    return (add, mul)

# main program
def main():
    wert = 45
    # Einfache Übergabe und Rückgabe
    wert = my_func(wert)
    print("Returnvalue: ", wert)

    # Übergabe mit Angabe des Parameters
    other_func(wert2 = "Hallo")
    
    # Übergabe unbenannter Parameter
    multivalue_func(4, 2, 5, "werte")
    
    # mehrere Rückgabewerte
    value1, value2 = multireturn_func(4, 6)
    print(f"Value1: {value1}, Value2: {value2}")

    do_nothing()

    
if __name__ == "__main__": 
    main()