"""
rich 라이브러리의 progressbar를 이용해  cpu 사용량를 보여줍니다.
"""
import psutil
from rich.progress import Progress, SpinnerColumn, BarColumn
from time import sleep
from rich.layout import Panel
from rich.console import Console
from rich.layout import Layout
from rich.live import Live

console = Console()
layout = Layout()

progress_bar = Progress(
    "{task.description}",  # progress bar의 설명을 나타내주는 필드입니다.
    SpinnerColumn(),
    BarColumn(bar_width=100),  # bar_width 속성은 bar의 가로 폭을 지정합니다.
    "{task.percentage:<2.2f}%",  # percent의 형식을 지정합니다.
)
progress_bar.add_task("[green]Current CPU Usage", total=100)
progress_bar.expand = True  # 화면의 사이즈 변경 시 자동으로 사이즈가 조절됩니다.

progress_table = Layout(
    Panel.fit(progress_bar, border_style="red")
)

layout.split(
    Layout(name="header", size=10),
)

layout['header'].split(
    Layout(Panel(progress_bar, title="[b]Cpu Usage", border_style="red"))
)

with Live(layout, screen=True, redirect_stderr=False) as live:
    try:
        while True:
            cpu_value = psutil.cpu_percent()
            progress_bar.update(task_id=0, advance=float(cpu_value))
            sleep(1)
            if cpu_value != psutil.cpu_percent():
                progress_bar.reset(task_id=0)

    except KeyboardInterrupt:
        pass
