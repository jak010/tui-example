import libtmux

server = libtmux.Server()
session = server.new_session(session_name="session_test", kill_session=True, attach=False)
session.attached_pane.split_window()

# 의사 코드로 이해하기 위해 pythonic 배제
panes = [pane for pane in session.attached_window.panes]

for index, pane in enumerate(panes, 0):
    if index == 0:
        pane.send_keys("python3 graph.py")
    elif index == 1:
        pane.send_keys("ls -al")

server.attach_session(target_session="session_test")

# pkill -f tmux
