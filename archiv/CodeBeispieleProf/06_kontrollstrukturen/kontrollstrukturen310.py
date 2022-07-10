# "switch", korrekt Structural Pattern Matching ab Python 3.10
# ohne Python 3.10 nicht lauffähig !!!
def struct_pattern_func(value : int):
    match value:
        case 200:
            print("nur 200 erlaubt")
        case 301 | 302:
            print("301 oder auch 302 erlaubt")
        case unknow: # _ wenn der Wert nicht benötigt wird
            print(f"Alles was nicht eingeordnet werden kann: {unknow=}")

def struct_pattern_func1(value):
    match value:
        case (4, y):
            print("Fall 1")
        case (x, 2) | (x, 3):
            print("Fall 2")
        case (x, y):
            print("Fall 3")
        case _: 
            print(f"Alles was nicht eingeordnet werden kann.")