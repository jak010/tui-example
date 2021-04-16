"""
 @ Date: 2021.04.16(금)
 @ Note
    터미널을 분리한 뒤 각 스크립트에 적어진 동작을 수행하는 형태
"""

import libtmux

server = libtmux.Server()
session = server.new_session(session_name="session_test", kill_session=True, attach=False)
session.attached_pane.split_window()

panes = [pane for pane in session.attached_window.panes]

for index, pane in enumerate(panes, 0):
    if index == 0:
        # 첫 번째 화면에서는 그래프를 보여줌
        pane.send_keys("python3 graph.py")
    elif index == 1:
        # 두 번쨰 화면에서는 특정 명령을 실행
        pane.send_keys("ls -al")

server.attach_session(target_session="session_test")

# pkill -f tmux
