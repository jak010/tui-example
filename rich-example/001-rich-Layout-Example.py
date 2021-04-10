""" 화면 분리 예제 """

from rich import print
from rich.layout import Layout

layout = Layout()

# 화면 나누기
layout.split(
    Layout(name="상단"),
    Layout(name="하단")
)
# 화면 영역별 사이즈 조정
layout['상단'].size = 5
layout['하단'].size = 5

# 하단 레이아웃의 영역을
# `left`, `right`의 변수로 다시 나눕니다
layout['하단'].split(
    Layout(name="left"),
    Layout(name="right"),
    direction="horizontal"
)

# left
layout["left"].update(
    "하단 레이아웃 왼쪽 글 입니다."
)

# right
layout["right"].update(
    "하단 레이아웃 오른쪽 글 입니다."
)

print(layout)
