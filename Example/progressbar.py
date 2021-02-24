
import urwid

from progress.bar import Bar
from time import sleep
from random import randint

bar = Bar("Processing", max=20, suffix="%(index)d/%(max)d cpu")

for i in range(20):
    bar.index = randint(1,20)
    bar.next()
    sleep(0.8)

bar.finish()

# ask = urwid.Edit(('I say', u"What is your name?\n"))
# div = urwid.Divider().render((10,)).text[1].decode()
# reply = urwid.Text(u"")
#
# inout_pile = urwid.Pile([ask, div, reply])
# lined_container = urwid.LineBox(inout_pile)
#
# top = urwid.Filler(lined_container, valign="top")
#
# urwid.MainLoop(top).run()
