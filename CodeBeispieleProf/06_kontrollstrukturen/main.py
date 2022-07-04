# Stand: 10.10.21
# Beispiele für Kontrollstrukturen

import sys

# If / Else Funktion
def if_func(value : int):
    if value == 3:
        print("Richtig")
    elif value == 5:
        print("Fast Richtig")
    elif 5 < value < 10: # mehrfache Bedingungen
        print("So Mittel :-)")
    elif value > 100 and value < 1000 or value == 6666: # mehrfache Bedingungen mit logischen Operatoren 
         print("Nett aber kalt")
    else:
        print("Falsch!")

# Switch Case kleiner Python 3.10
def switch_func(argument : int):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print(switcher.get(argument, "Invalid month"))


# main program
def main():
    value = input("Wert eingeben: ")
    
    #if_func(value) # Fehler! Weil falscher Typ
    if_func(int(value)) # Übergabe mit Typenkonvertierung
    switch_func(int(value))
    
    # Ab hier nur mit Python 3.10
    
    if sys.version_info[1] < 10 or sys.version_info[0] < 3:
        raise Exception("Must be using Python 3.10 or higher")
    else:
        import kontrollstrukturen310 as p310
    
    p310.struct_pattern_func(500)
    p310.struct_pattern_func1((2, 3))
    
if __name__ == "__main__":
    main()
    