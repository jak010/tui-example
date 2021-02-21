import urwid as uw
from urwid_timed_progress import TimedProgressBar
import time


def tbar(*args):
    global bar1
    global loop
    for i in range(1, 100,1):
        bar1.add_progress(i)
        loop.draw_screen()
        time.sleep(0.4)


def keypress(key):
    if key in ('q', 'Q'):
        raise uw.ExitMainLoop()


palette = [
    ('normal', 'white', 'white', 'standout'),
]

bar1 = TimedProgressBar('normal', 'complete', label='Current Input', label_width=200, done=100)

footer = uw.Text('q to exit, any other key adds to progress')
progress = uw.Frame(uw.ListBox([bar1, uw.Divider()]), footer=footer)

btn = uw.Button('Go', on_press=tbar)
frame = uw.Frame(uw.Filler(uw.Pile([bar1, btn])))
loop = uw.MainLoop(frame)

loop.run()
