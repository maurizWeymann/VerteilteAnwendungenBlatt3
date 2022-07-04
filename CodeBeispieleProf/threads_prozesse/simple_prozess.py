import multiprocessing
from time import sleep
from random import randint

g_text = "Hallo Welt"

def tfunc():
    name = multiprocessing.current_process().name
    #name = ""
    print(f"Run: {name}")
    sleep(randint(2, 6))
    print(f"Done: {name}")


def main():
    print(f"Processname: {multiprocessing.current_process().name}")
    p1 = multiprocessing.Process(target=tfunc)
    p2 = multiprocessing.Process(target=tfunc)
    p1.start()
    p2.start()
    print("Main Ende")

if __name__ == '__main__':
    main()