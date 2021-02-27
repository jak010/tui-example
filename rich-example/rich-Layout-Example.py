from rich import print
from rich.layout import Layout

layout = Layout()
# 1 depth
layout.split(
    Layout(name="upper"),
    Layout(name="lower")
)
layout['upper'].size = 5
layout['upper'].ratio = 1
layout['lower'].size = 5

# 2 depth
layout['lower'].split(
    Layout(name="left"),
    Layout(name="right"),
    direction="horizontal"  # horizontal 속성을 지정해 `lower`를 수평으로 분리시킴
)

# 3 depth
layout["left"].update(
    "The mystery of life isn't a problem to solve, but a reality to experience."
)

print(layout)
