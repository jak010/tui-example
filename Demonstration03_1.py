import urwid

PALETTE = [
    ('normal', 'black', 'light gray'),
    ('complete', 'black', 'dark red'),
]
p = urwid.ProgressBar(normal='a', complete=100,
                      current=20, done=100, satt="b")


def progress_handler(key):
    if key in ('q', "q", 'enter'):
        raise urwid.ExitMainLoop()
    p.current += 1


fill = urwid.Filler(p, valign="middle")

a = urwid.MainLoop(fill, unhandled_input=progress_handler)

a.run()
