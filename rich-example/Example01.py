"""

Demonstrates a dynamic Layout, Example, 

"""

from datetime import datetime
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from time import sleep
from rich.layout import Panel
from rich.align import Align
from rich.console import Console, RenderGroup
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich.table import Table

console = Console()
layout = Layout()
job_progress = Progress(
    "{task.description}",
    SpinnerColumn(),
    BarColumn(),
    "{task.percentage:<2.2f}%",
)
job_progress.add_task("[green]CPU Usage")
job_progress.expand = True


progress_table = Layout(
    Panel.fit(job_progress, title="[b]Resource Usage", border_style="red")
)

layout.split(
    Layout(name="header", size=10),
    Layout(ratio=2, name="main"),
    Layout(ratio=1, name="footer"),
)

layout["main"].split(
    Layout(name="body"),
    direction="horizontal"
)
layout['footer'].split(
    Layout(Panel(job_progress, title="[b]Resource Usage", border_style="red",expand=True))
)

with Live(layout, screen=True, redirect_stderr=False) as live:
    try:
        while True:
            sleep(1)
            import psutil
            cpu = psutil.cpu_percent()
            job_progress.update(task_id=0, advance=float(cpu))
            sleep(3)
            job_progress.reset(task_id=0)

    except KeyboardInterrupt:
        pass