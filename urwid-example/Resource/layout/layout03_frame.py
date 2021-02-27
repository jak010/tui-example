import urwid

# Tuples of (Key, font color, background color)
palette = [
    ('titlebar', 'dark red', ''),
    ('refresh button', 'dark green,bold', ''),
    ('quit button', 'dark red', ''),
    ('getting quote', 'dark blue', ''),
    ('headers', 'white,bold', ''),
    ('change ', 'dark green', ''),
    ('change negative', 'dark red', '')]
# header
header_text = urwid.Text("Hell urwid World")
header = urwid.AttrMap(header_text, "titlebar")

# body
quote_text = urwid.Text("press to Get Your first quote!")
quote_filer = urwid.Filler(quote_text, valign="top", top=1, bottom=1)
v_padding = urwid.Padding(quote_filer, left=1, right=1)
quote_box = urwid.LineBox(v_padding)

# footer
menu = urwid.Text([
    u'Press (', ('refresh button', u'R'), u') to manually refresh. ',
    u'Press (', ('quit button', u'Q'), u') to quit.'
])

layout = urwid.Frame(header=header, body=quote_box, footer=menu)


# Handle key presses
def handle_input(key):
    if key == 'Q' or key == 'q':
        raise urwid.ExitMainLoop()


# main loop
main_loop = urwid.MainLoop(layout, palette=palette, unhandled_input=handle_input)
main_loop.run()
