import itertools
from rich.console import Console
from rich.align import Align
import time
from threading import Thread
from utils import clear_screen

console = Console()

clear_screen()
def welcome_animation():
    print()

console.print(Align.center(r"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$", style="bold green"))
time.sleep(0.2)
console.print(Align.center(r"$   ____   _   ____    _   _   _____   ____    $", style="bold green"))
time.sleep(0.2)
console.print(Align.center(r"$  / ___| (_) |  _ \  | | | | |___ /  |  _ \   $", style="bold green"))
time.sleep(0.2)
console.print(Align.center(r"$  | |    | | | |_) | | |_| |   |_ \  | |_) |  $", style="bold green"))
time.sleep(0.2)
console.print(Align.center(r"$  | |___ | | |  __/  |  _  |  ___) | |  _ <   $", style="bold green"))
time.sleep(0.2)
console.print(Align.center(r"$  \____| |_| |_|  ___|_| |_| |____/  |_| \_\  $", style="bold green"))
time.sleep(0.2)
console.print(Align.center(r"$  | | | |  _   _  | __ )                      $", style="bold green"))
time.sleep(0.2)
console.print(Align.center(r"$  | |_| | | | | | |  _ \                      $", style="bold green"))
time.sleep(0.2)
console.print(Align.center(r"$  |  _  | | |_| | | |_) |                     $", style="bold green"))
time.sleep(0.2)
console.print(Align.center(r"$  |_| |_|  \__,_| |____/                      $", style="bold green"))
time.sleep(0.2)
console.print(Align.center(r"$                                              $", style="bold green"))
time.sleep(0.2)
console.print(Align.center(r"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$", style="bold green"))
time.sleep(0.2)

def loading_animation(duration=1.5):
    for _ in range(int(duration * 10)):
        print("Loading...", end="\r")
        time.sleep(0.1)
def loading_animation(duration=1.5):
    
    spinner = itertools.cycle(['-', '/', '|', '\\'])
    end_time = time.time() + duration

    def animate():
        while time.time() < end_time:
            print(f'\rLoading... {next(spinner)}', end='', flush=True)
            time.sleep(0.1)
        print('\rLoading... Done!', end='', flush=True)

    thread = Thread(target=animate)
    thread.start()
    thread.join()
