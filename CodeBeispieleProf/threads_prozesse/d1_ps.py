import time
from rich.progress import Progress
from rich import print
import random
from file_stuff import write_data_file

def main():
    progress_data = [0, 0, 0, 0]
    names = [f"Taskbar{x}" for x in range(1, 5)]
    colors = ["red", "green", "cyan", "yellow"]
    taskbars = []

    print("[red bold]Progress Demo [green] (Press STRG+c to exit)")
    with Progress() as progress:
        for name, color in zip(names, colors):
            taskbar = progress.add_task(f"[{color}]{name}...", total=100)
            taskbars.append(taskbar)
        
        while True:
            for count, taskbar in enumerate(taskbars):
                progress_data[count] = random.randint(0,100)
                progress.update(taskbar, completed=progress_data[count])
            
            write_data_file(progress_data)
            time.sleep(0.1)

if __name__ == '__main__':
    main()