import psutil, os
import time
import urwid as uw
from urwid_timed_progress import TimedProgressBar

if __name__ == '__main__':
    palette = [
        ('normal', 'white', 'white', 'standout'),
    ]

    bar1 = TimedProgressBar('normal', 'complete', label='Current Input',
                            label_width=100, done=100)

    footer = uw.Text('q to exit, any other key adds to progress')
    # progress = uw.Frame(uw.ListBox([bar1, uw.Divider()]), footer=footer)


    def keypress(key):
        if key in ('q', 'Q'):
            raise uw.ExitMainLoop()

    def press_test(*args):
        p = psutil.Process(1509)
        memory = p.as_dict()['memory_percent']
        print(memory)
        bar1.add_progress(memory)
        time.sleep(0.2)
        


    btn = uw.Button("Go", on_press=press_test)
    frame = uw.Frame(uw.Filler(uw.Pile([bar1, btn ])))

    loop = uw.MainLoop(frame, unhandled_input=keypress)
    loop.run()
