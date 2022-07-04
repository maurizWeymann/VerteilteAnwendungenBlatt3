# Stand: 13.10.21
# Beispiele für Schleifen

# Tuples
my_tuple = (2, 5, 4, 8)

# Dictionary
my_dict = {
    "entry" : 64,
    "other" : 88,
    "name"  : "Name"
} 

# Listen
my_list = ["Wert1", "Wert2", "WertN"]

# For-Schleifen
def forloop_func():
    
    for mt in my_tuple:
        print(f"Tuple Wert: {mt}")
    
    for ml in my_list:
        print(f"List Wert: {ml}")

    for md in my_dict:
        print(f"Dict: {md}")

    # For-Schleife für Dictionary mit Key->Value
    for kmd, vmd in my_dict.items():
        print(f"K: {kmd} -> V: {vmd}")

    # range (start, stop, schrittweite)
    # oder kurz einfach der Stopwert wird als kleiner gezählt range(10)
    for i in range(0, 10, 1):
        if i == 4:
            continue  # Springt wieder zum Schleifenkopf und "ignoriert" folgende Anweisungen
        print(i)

    for _ in range(5):
        print("Ohne die Zählervariable")
   

def short_forloop_func():
    x = [i for i in range(10)]
    print(x)

    y = [i * 2 for i in range(10)]
    print(y)

    # 1. weg
    z = []
    for i in range(10):
        if i % 2 == 0:
            z.append(i)
    print(z)
    
    # 2. weg, mehr "Pythonic"
    z = [i for i in range(10) if i % 2 == 0]
    print(z)


# While-Schleifen
def whileloop_func():
    # Python kennt nur while, keine do while

    # "Endloschleife" mit Abbruchbedingung 
    i = 0
    while True:
        i += 1
        print("While Wert : ", i)
        if i >= 3:
            break # Schlüsselwort zum Abbruch von Funktionsblöcken

# Ab Python 3.8 mit Walrus-Operator
def whileloop_with_walrus_func():
    # while mit Walrus Operator
    while (indata := input("Eingabe (exit fuer beenden): ")) != "exit":
        print(f"Eingabe: {indata}")

# main program
def main():
    forloop_func()
    whileloop_func()
    short_forloop_func()
    # whileloop_with_walrus_func()

if __name__ == "__main__":
    main()