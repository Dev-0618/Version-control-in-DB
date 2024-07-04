from time import sleep
from rich.console import Console

console = Console()

def loading_animation():
    with console.status("Loading...", spinner="dots"):
        sleep(3)

def welcome_animation():
    console.print("[bold magenta]Welcome to the CLI Application![/bold magenta]")
    sleep(1)
