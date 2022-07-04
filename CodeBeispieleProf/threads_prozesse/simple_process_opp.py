from multiprocessing import Process
import multiprocessing
from time import sleep
from random import randint

class MyProcess(Process):
    def __init__(self, process_ID):
        Process.__init__(self)
        self.process_ID = process_ID
    
    def run(self):
        name = multiprocessing.current_process().name       
        print(f"Run: {name} - {self.process_ID}")
        sleep(randint(2, 4))
        print(f"Done: {name}")

def main():
    print(f"Processname: {multiprocessing.current_process().name}")
    p1 = MyProcess(1)
    p2 = MyProcess(2)
    p1.start()
    p2.start()
    
    for i in range(3):
        print(i)
        sleep(1)
    
    print("Main Ende")

if __name__ == '__main__':
    main()