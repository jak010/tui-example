import urwid


def on_ask_change(edit, new_edit_text):
    reply.set_text(('I say', u"Nice to meet you, %s" % new_edit_text))


def on_exit_clicked(button):
    raise urwid.ExitMainLoop()


# palette = [('I say', 'default,bold', 'default', 'bold'), ]

ask = urwid.Edit(('I say', u"What is your name?\n"))
reply = urwid.Text(u"")
button = urwid.Button(u'Exit', on_press=on_exit_clicked)
button2 = urwid.Button(u'Exit', on_press=on_exit_clicked)
button3 = urwid.Button(u'Exit', on_press=on_exit_clicked)

div = urwid.Divider(top=10,bottom=10)
inout_pile = urwid.Pile([ask, div, reply])

lined_container = urwid.LineBox(inout_pile)
cols = urwid.Columns([lined_container, (9, button), (8, button2)])
top = urwid.Filler(cols, valign='middle')
urwid.connect_signal(ask, 'change', on_ask_change)
urwid.MainLoop(top).run()
