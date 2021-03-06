import urwid

PALETTE = [
    ('normal', 'black', 'light gray'),
    ('complete', 'black', 'dark red'),
]
p = urwid.ProgressBar(normal='a', complete=100,
                      current=20, done=100, satt=None)


def progress_handler(key):
    if key in ('q', 'quit'):
        raise urwid.ExitMainLoop()
    p.current += 1
    p.render(size=(10,))

fill = urwid.Filler(p, valign="middle")
a = urwid.MainLoop(fill, unhandled_input=progress_handler)
a.run()
