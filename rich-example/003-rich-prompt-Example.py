from rich.prompt import Prompt, Confirm

name = Prompt.ask("Enter your name", choices=["A", "B", "C"], default="_")

if name == "A":
    print("Access_granted")

is_rich_great = Confirm.ask("Do you like rich?")
