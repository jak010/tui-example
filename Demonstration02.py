import psutil
import urwid
from progress.bar import Bar

bar = Bar("Processing", max=100, suffix="%(index).1f%% - %(max)d%% cpu  ")


def calling():
    while True:
        p = psutil.cpu_percent()
        bar.index = float(p)
        bar.next()


ask = urwid.Edit(('I say', u"What is your name?\n"))
div = urwid.Divider()
reply = urwid.Text(u"")

input_pile = urwid.Pile([ask, div, reply])
lined_container = urwid.LineBox(input_pile)

top = urwid.Filler(lined_container, valign="top")

urwid.MainLoop(top, unhandled_input=calling).run()
