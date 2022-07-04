# Einfaches Modul und Demonstration vom Kontextswitch 

class myClass():
    def wieder_hallo_welt(self):
        print(f"Hallo Welt Modul {__name__}")


if __name__ == "__main__":
    print("Program")
    m = myClass()
    m.wieder_hallo_welt()