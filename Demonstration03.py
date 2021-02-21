import urwid as uw
from urwid_timed_progress import TimedProgressBar

if __name__ == '__main__':

    palette = [
        ('normal', 'white', 'white', 'standout'),
    ]

    bar1 = TimedProgressBar('normal', 'complete', label='Current Input',
                            label_width=200, units='MB', done=5)

    footer = uw.Text('q to exit, any other key adds to progress')
    progress = uw.Frame(uw.ListBox([bar1, uw.Divider()]), footer=footer)


    def keypress(key):
        if key in ('q', 'Q'):
            raise uw.ExitMainLoop()
        bar1.add_progress(1)

    loop = uw.MainLoop(progress, palette, unhandled_input=keypress)
    loop.run()
