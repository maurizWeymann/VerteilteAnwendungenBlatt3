# Stand: 09.10.21
# Beispiele für Variablen mit einfachen Datentypen
# und verschiedene Ausgabemöglichkeiten

from datetime import datetime


# Globale Variablen, werden nach Style Guide groß geschrieben
A_INT = 10                          # Integer
B_FLOAT = 6.252                     # Float
C_BOOLEAN = True                    # Boolean 
D_STRING = "Hallo Welt"             # Strings
E_INT_BIG_NUMBER = 100_000_000_000  # Große Konstanten
NOW = datetime.utcnow()


# Anlegen lokaler Variable
def my_func():
    A_INT = 100 # Lokale Variablen
    print(f"Ausgabe my_func: {A_INT}")

# Veränderung globaler Variablen
def other_func():
    global A_INT
    A_INT = 200
    print("Ausgabe other_func:", A_INT)

# main program
def main():
    # In Python sind alle Datentypen Klassen
    e_string_lokal = "Das ist Text"
    print(type(e_string_lokal))
    print(type(B_FLOAT))

    print("1. Ausgabe main " + str(A_INT))
    
    # Keine Veränderung
    my_func()
    print("2. Ausgabe main %s" % (A_INT))

    # Veränderung
    other_func()
    print("3. Ausgabe main {}".format(A_INT))

    print(f"Große Zahlen: {E_INT_BIG_NUMBER}")
    print(f"Andere Ausgabe: {E_INT_BIG_NUMBER = }")
    print(f"Formatierung {B_FLOAT:.2f}")
    print(f"Datum: {NOW}")
    now_format = f"{NOW:%d.%m.%Y}"
    print(f"Datum formatiert: {now_format}")

if __name__ == "__main__": 
    main()