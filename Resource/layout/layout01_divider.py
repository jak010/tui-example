"""
@ Note
Divider는 화면을 가로로 분할함

"""

import urwid

div1 = urwid.Divider("---",)
div2 = urwid.Divider("====")
div3 = urwid.Divider("~~~~")

pile = urwid.Pile([div1, div2, div3])
top = urwid.Filler(pile, valign='top')

a = urwid.MainLoop(top)
a.run()

