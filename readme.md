## Urwid Note

#### Resource

- urwid widget class
  - http://urwid.org/manual/widgets.html

- urwid progress bar
  - https://github.com/mgk/urwid_timed_progress

#### Module
- Divider() : 화면 구분자
  - Usage : Demonstration01.py
  
- LinBox() : 이 모듈에 넘겨진 인자들은 표현될 때 박스로 감싸져서 표현됨
  - Usage : Demonstration02.py
  
- TimedProgressBar()
  - Usage : Demonstration03.py
  
- ProgressBar()
  - Usage : Demonstration03_1.py

#### point

urwidㅈ 만으로 여러 ㅈ정보를 표현하기 힘들지 않을까 생각(활용할 수 있는 예제가 생각보다 적고 분석하는데
시간이 많이 들어감 URWID와 RICH 적당히 배합해서 써야 CUI 수준의 대시보드를 효과적으로 표현 가능할ㄱ듯
```python
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

```