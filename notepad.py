import urwid
import psutil
from progress.bar import Bar

bar = Bar("Processing", max=100, suffix="%(index).1f%% - %(max)d%% cpu  ")

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

reply = urwid.Text(u"")

ask = urwid.Edit(('I say', u"What is your name?\n"))

def on_status_bar(edit, new_edit_text):
    p=psutil.cpu_percent()
    bar.index = p
    reply.set_text((
        "%s", bar
    ))

urwid.connect_signal(ask, "change",on_status_bar)
inout_pile = urwid.Pile([ask, reply])
lined_container = urwid.LineBox(inout_pile)

top = urwid.Filler(lined_container, valign="top")

urwid.MainLoop(top).run()
