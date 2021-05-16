import urwid

from urwid import Button
from urwid import Pile

# Basic Widget
# : Text, Edit, Button etc,  SolidFill, Divider
btn01 = urwid.Button("Button01")
# btn02 = urwid.Button("Button02")
# btn03 = urwid.Button("Button02")
# btn04 = urwid.Button("Button02")
# btn05 = urwid.Button("Button02")

# Decoration Widget

BtnLine = urwid.LineBox(btn01)

# Container Widget : Columns, Pile, Frame, ListBox, GridFlow

body = urwid.Columns(BtnLine)

urwid.MainLoop(body).run()
