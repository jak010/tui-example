import urwid

## 표출 데이터 정의
palette = [('I say', 'default,bold', 'default', 'bold'), ]
ask = urwid.Edit(('I say', u"What is your name?\n"))
reply = urwid.Text(u"")
div = urwid.Divider()
button = urwid.Button(u'Exit')

## 화면 표출
pile = urwid.Pile([ask, div, reply, div, button])
top = urwid.Filler(pile, valign='top')


def on_ask_change(edit, new_edit_text):
    reply.set_text(('I say', u"Nice to meet you, %s" % new_edit_text))


def on_exit_clicked(button):
    raise urwid.ExitMainLoop()


urwid.connect_signal(ask, 'change', on_ask_change)
urwid.connect_signal(button, 'click', on_exit_clicked)

urwid.MainLoop(top, palette).run()
