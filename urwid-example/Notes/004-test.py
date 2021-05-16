import urwid
import numpy as np

# Grpah Example isn' it?
palette = [
    ('inverse', 'black', 'dark magenta'),
]

from random import randint

number = randint(1, 5)
bardata = [(number,), (2,), (4,), (8,), (16,), (32,)]

graph = urwid.BarGraph(
    ['pink', 'inverse'],
    ['normal', 'inverse'],
    {(1, 0): 'normal', },
)
lines = [10]


def refersh_data(*args):
    from random import randint

    number01 = randint(1, 25)
    number02 = randint(1, 25)
    number03 = randint(1, 25)
    number04 = randint(1, 25)
    number05 = randint(1, 25)
    bardata = [(number01,), (number02,), (number03,), (number04,), (number05,)]

    graph.set_data(bardata, 50, lines)


def refresh_handler(key):
    if key in ('q', "Q"):
        raise urwid.ExitMainLoop()


if __name__ == "__main__":
    import time

    loop = urwid.MainLoop(graph, palette, unhandled_input=refresh_handler)
    for x in np.arange(1, 100, 0.2):
        loop.set_alarm_at(time.time() + x, refersh_data, user_data=1)

    loop.run()
