import urwid

blank = urwid.Divider()

text_left = u"Left Urwid"
text_center = u"Left Urwid"
text_right = u"Left Urwid"

# listbox_content = [
#     blank,
#     urwid.LineBox(urwid.Text(text_center, align="center")),
#     blank,
#     urwid.LineBox(urwid.Text(text_right, align="right"))
# ]
#
# listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))

# pile = urwid.Pile(Menus)
#
# filer = urwid.Filler(pile)

btn01 = urwid.Button("Menu01")
btn02 = urwid.Button("Menu02")
btn03 = urwid.Button("Menu03")


def signal_example_btn01(*args):
    _text = "Change Label"
    current_label = btn01.get_label()
    print(current_label)
    if current_label != _text:
        return btn01.set_label(_text)
    if current_label == _text:
        return btn01.set_label(current_label)


urwid.connect_signal(btn01, "click", signal_example_btn01)

top_menu_btn01 = urwid.LineBox(btn01)
top_menu_btn02 = urwid.LineBox(btn02)
top_menu_btn03 = urwid.LineBox(btn03)

top_menus = [top_menu_btn01, top_menu_btn02, top_menu_btn03]

container_widgets = urwid.Columns(
    top_menus
)

Container01 = urwid.Filler(container_widgets)
Container02 = urwid.Filler(container_widgets)

piles = urwid.Pile([Container01, Container02])
urwid.MainLoop(piles).run()
