import threading
from rich.progress import Progress
from rich import print
import os

from file_stuff import read_data_file
import file_stuff

file_change = False

def check_file_change():
    cached_stamp = 0
    global file_change
   
    while True:
        stamp = os.stat(file_stuff.DATA_FILE_NAME).st_mtime
        if stamp != cached_stamp:
            cached_stamp = stamp
            file_change = True


def main():
    global file_change
    progress_data = [0, 0, 0, 0]
    names = [f"Taskbar{x}" for x in range(1, 5)]
    colors = ["red", "green", "cyan", "yellow"]
    taskbars = []

    background_check = threading.Thread(target=check_file_change)
    background_check.daemon = True
    background_check.start()
   
    print("[red bold]Progress Demo [green] (Press STRG+c to exit)")
    with Progress() as progress:
        for name, color in zip(names, colors):
            taskbar = progress.add_task(f"[{color}]{name}...", total=100)
            taskbars.append(taskbar)
        
        while True:
            if file_change:
                file_change = False
                progress_data = read_data_file()
                for count, taskbar in enumerate(taskbars):
                    progress.update(taskbar, completed=progress_data[count])

if __name__ == '__main__':
    main()