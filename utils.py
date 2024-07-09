from rich.console import Console
from rich.align import Align
from rich.table import Table
from rich.text import Text
import time

console = Console()

def clear_screen():
    console.clear()

def print_box(headers, data):
    table = Table(show_header=True, header_style="bold magenta")
    for header in headers:
        table.add_column(header)
    
    for row in data:
        str_row = [Text(str(item), style="bold green") for item in row]  # Convert all items to strings with cyan color
        table.add_row(*str_row)
    
    console.print(Align.center(table))

def loading_animation(duration=1.5):
    with console.status("Loading..."):
        time.sleep(duration)
