
from rich.prompt import Prompt, Confirm
name = Prompt.ask("Enter your name", choices=["Paul", "Jessica", "Duncan"], default="Paul")

is_rich_great = Confirm.ask("Do you like rich?")

assert is_rich_great