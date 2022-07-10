import time
import threading
import random

# Zusatz Modul Rich für graphische Ausgaben
# python -m rich #Demoausgabe
# python -m pip install rich #Installation mit Python
from rich.progress import Progress
from rich import print



names = [f"Thread{x}" for x in range(1, 5)]
colors = ["red", "green", "cyan", "yellow"]

def fupdate(progress, taskname, speed):
    while not progress.finished:
        progress.update(taskname, advance=speed)
        time.sleep(0.004)

def main():
    tlist = []
    print("[red bold]Thread Demo")
    with Progress() as progress:
        for name, color in zip(names, colors):
            taskbar = progress.add_task(f"[{color}]{name}...", total=1000)
            task = threading.Thread(target=fupdate, args=(progress, taskbar, random.randint(1, 5),))
            task.start()
            tlist.append(task)
        
        for t in tlist:
            t.join()

if __name__ == '__main__':
    main()