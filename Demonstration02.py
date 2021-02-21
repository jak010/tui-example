import urwid

ask = urwid.Edit(('I say', u"What is your name?\n"))
div = urwid.Divider()
reply = urwid.Text(u"")

inout_pile = urwid.Pile([ask, div, reply])
lined_container = urwid.LineBox(inout_pile)

top = urwid.Filler(lined_container, valign="top")

urwid.MainLoop(top).run()