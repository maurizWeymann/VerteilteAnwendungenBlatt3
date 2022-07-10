import threading
from time import sleep
from random import randint

i = 0

def tfunc():
    global i # Datenaustauch über globale Variable 
    i += 1
    name = threading.currentThread().getName()
    print(f"Run: {name}")
    sleep(randint(2, 4))
    print(f"Done: {name}")

# Thread mit Parameter
def tfunc_1(name):
    print(f"Run: {name}")
    sleep(randint(2, 4))
    print(f"Done: {name}")

def main():
    print(f"Threadname: {threading.currentThread().getName()}")
    t1 = threading.Thread(target=tfunc)
    # Thread mit Parameter
    t2 = threading.Thread(target=tfunc_1, args=("Mein Name",)) 
    #t1.setDaemon(True)
    t1.start()
    t2.start()
    
    #t1.join()
    #t2.join()
    print(f"Main Ende, Wert von {i=}")

if __name__ == '__main__':
    main()