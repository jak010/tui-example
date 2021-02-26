from progress.bar import Bar
import psutil

import urwid

from time import sleep
from tqdm import tqdm
# for i in tqdm(range(1000)): sleep(0.2)

# statusbar = Bar('Loading',max=100, fill='@', suffix='%(percent).3f%%')
# statusbar.index = 2

div2 = urwid.ProgressBar('pg normal', 'pg complete', 3, 100, 'pg smooth')
def keypress(key):
    if key in ('q',"q"):
        urwid.ExitMainLoop()
    if (div2.current == 100) or (div2.current > 100):
        div2.current = 0
    div2.current += 5

div1 = urwid.Divider("---",)
div3 = urwid.Divider("~~~~")

pile = urwid.Pile([div1, div2, div3])
top = urwid.Filler(pile, valign='top')

a = urwid.MainLoop(top, unhandled_input=keypress)
a.run()


# linebox = urwid.LineBox()
#
# with Bar('Loading',max=100, fill='@', suffix='%(percent).3f%%') as cpu_bar:
#     while True:
#         displayed = psutil.Process(10374).as_dict()['memory_percent']
#         cpu_bar.index = displayed -1
#
#         cpu_bar.next()

