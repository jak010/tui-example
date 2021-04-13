#!/usr/bin/env python
"""
Horizontal split example.
"""
from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout

import plotext as plt
import numpy as np

def test():
    l = 1000
    n = 2
    f = n * np.pi / l
    x = np.arange(0, l)
    xticks = np.linspace(0, l - 1, 5)
    xlabels = [str(i) + "π" for i in range(5)]
    frames = 500

    for i in range(frames):
        y = np.sin(n * f * x + 2 * np.pi / frames * i)

        plt.clp()
        plt.clt()
        plt.scatter(x, y)
        plt.ylim(-1, 1)
        plt.xticks(xticks, xlabels)
        plt.yticks([-1, 0, 1])
        plt.title("plotext - streaming data")
        plt.nocolor()
        plt.sleep(0.001)
        plt.show()
# 1. The layout
left_text = "test"
right_text = "\n(bottom pane.)"

body = HSplit(
    [
        Window(FormattedTextControl(left_text)),
        Window(height=1, char="-"),  # Horizontal line in the middle.
        Window(FormattedTextControl(right_text)),
    ]
)

# 2. Key bindings
kb = KeyBindings()


@kb.add("q")
def _(event):
    event.app.exit()


# 3. The `Application`
application = Application(layout=Layout(body), key_bindings=kb, full_screen=True)


def run():
    application.run()


if __name__ == "__main__":
    run()
