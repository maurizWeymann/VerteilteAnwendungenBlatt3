from threading import Thread
import threading
from time import sleep
from random import randint

class MyThread(Thread):
    def __init__(self, thread_ID):
        Thread.__init__(self)
        self.thread_ID = thread_ID
    
    def run(self):
        name = threading.currentThread().getName()
        print(f"Run: {name} - {self.thread_ID}")
        sleep(randint(2, 4))
        print(f"Done: {name}")

def main():
    print(f"Threadname: {threading.currentThread().getName()}")
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()
    
    for i in range(3):
        print(i)
        sleep(1)
    
    print("Main Ende")

if __name__ == '__main__':
    main()