import psutil, os

import urwid as uw
from urwid_timed_progress import TimedProgressBar

if __name__ == '__main__':
    p = psutil.Process(1509)
    print(p.as_dict()['memory_percent'])

    palette = [
        ('normal', 'white', 'white', 'standout'),
    ]

    bar1 = TimedProgressBar('normal', 'complete', label='Current Input',
                            label_width=100, done=5)

    footer = uw.Text('q to exit, any other key adds to progress')
    progress = uw.Frame(uw.ListBox([bar1, uw.Divider()]), footer=footer)


    def keypress(key):
        if key in ('q', 'Q'):
            raise uw.ExitMainLoop()

        p = psutil.Process(1509)
        memory = p.as_dict()['memory_percent']
        bar1.add_progress(memory)


    loop = uw.MainLoop(progress, palette, unhandled_input=keypress)
    loop.run()
